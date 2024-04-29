# Customer Account Details API Service
---

`Customer service` is used for updating customer details on the database. If Customer details updates in this service it automatically relase message queue to update in the `account service`.

## Requirements
1. Python
2. Django
3. Mysql
4. Docker

FYI - Run `pip install -r requirements.txt` to install python library in the python virtual environment 

## Steps of run
1. Install Docker
2. Run `docker-compose up` to start docker container
    * Default host 0.0.0.0:8000
3. Run Python Migration command to migrate database inside docker containers backend service
4. After successful migration restart the container
5. Use postman to check the api (Postman files provided) 



