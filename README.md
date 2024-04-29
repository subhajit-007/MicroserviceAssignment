# Microservice Assignment
---

## Assumptions
1. Service name - `Customer Management`
   * Used for CRUD operation for Customer details with bank balance eg. name, acc_no, dob etc.
   * Tech used python - django 
   * DB used - Mysql ( Different instence from the another service )
2. Service name - `Account Management`
   * Used for Account Balance related CRUD operation
   * fields - account_no, balance
   * Tech used python - flask
   * DB Used - Mysql ( Different instence from the another service)
3. These two service uses RabbitMQ message queues to talk to each other
4. `.env` used for environment varriables
   
## Work Function

1. All `CRUD` operation avaliable on `Account management`Service
   * Accounts service `Update API` invoked it will update Customer Details Balance property as well using message queue
   * Account service `Delete API` invoked it will also delete customer details for the customer service as well using message queue.
  
2. All `CRUD` operation avaliable on `Customer Details Service`
    * If Customer details `Delete API` invoked it will send a message queue to delete the `Account Details` from the Account service as well.
    * Although due to DB integration issue only in Account details, only the deleting on accounts service through message queue is not working although app is getting delete user details on accounts service.

  
Note: 
* README aval for each service separately in the folder
* Also postman api files provided
* URLs are provided in the POSTMAN file - This can be directly imported in POSTMAN
---
