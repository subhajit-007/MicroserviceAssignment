# Account Management API Service
---
`Account service` is used for updating customer account balance details on the database. If Account details updates or deleted using this service it automatically relase message queue to update the same for the `Customer service`.


## Requirements
1. Python
2. Flask
3. Mysql
4. Docker

FYI - Run `pip install -r requirements.txt` to install python library in the python virtual environment 

## Steps of run
1. Install Docker
2. Run `docker-compose up` to start docker container
    * Host 0.0.0.0:5000 on docker
    * Host 0.0.0.0:8001 on local
3. Run Python Migration command to migrate database inside docker containers backend service
    * `flask --app manager.py db init`
    * `flask --app manager.py db migrate`
    * `flask --app manager.py db upgrade`
4. After successful migration restart the container
5. Use postman to check the api (Postman files provided) 
   * Host 0.0.0.0:8001 on postman



