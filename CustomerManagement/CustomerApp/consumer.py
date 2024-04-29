import pika, json, os, django
from dotenv import load_dotenv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CustomerApp.settings")
django.setup()

# Load .env file
load_dotenv()

from customers.models import CustomerDetails


params = pika.URLParameters(os.getenv("RABBITMQ_API_KEY"))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in customer app')
    print(body)
    data = json.loads(body)


    if properties.content_type == 'account_delete':
        print("Delete customer details for account no ==> ", data)
        CustomerDetail = CustomerDetails.objects.get(account_no=data)
        CustomerDetail.delete()
        print('Customer detail Deleted.')
    elif properties.content_type == 'update_balance':
        CustomerDetail = CustomerDetails.objects.get(account_no=data["account_no"])
        CustomerDetail.balance = data["balance"]
        CustomerDetail.save()
        print('Customer Balance updated.')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming at customer service...')

channel.start_consuming()

channel.close()
