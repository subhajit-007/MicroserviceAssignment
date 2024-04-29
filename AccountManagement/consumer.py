import pika, json, os
# from main import db, app
from flask import current_app
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BASE_URL = "http://0.0.0.0:8001/api"

params = pika.URLParameters(os.getenv("RABBITMQ_API_KEY"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in Accounts Service')
    data = json.loads(body)

    print("Data received from customer service ===> \n", data)

    if properties.content_type == 'CustomerDetails_created':
        try:
            response = requests.get(f"{BASE_URL}/accountdetail")
            if response.status_code == 200:
                data = response.json()
                print('New Account Created.')
                print("Response: ", data)
            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", e)

    elif properties.content_type == 'CustomerDetails_deleted':
        try:
            print(data[0])
            response = requests.get(f"{BASE_URL}/accountdetail/{data[0]}")
            if response.status_code == 200:
                data = response.json()
                print('New Account Created.')
                print("Response: ", data)
            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", e)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming at account service...')

channel.start_consuming()

channel.close()
