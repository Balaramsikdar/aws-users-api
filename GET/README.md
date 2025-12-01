# AWS Serverless Users API (Python)

This project implements a serverless REST API on AWS for user management using:
- AWS Lambda (Python)
- API Gateway
- DynamoDB
- IAM roles & permissions

## Endpoints

### ✔ POST /users
Creates a new user in DynamoDB

Example Request:
```json
{
  "name": "Balaram",
  "email": "test@gmail.com"
}
✔ GET /users

Returns all users in DynamoDB

Example Response:

[
  {
    "userId": "c3282940...",
    "name": "Balaram",
    "email": "test@gmail.com"
  }
]

AWS Architecture

Client
→ API Gateway
→ Lambda (Python)
→ DynamoDB

No servers, fully serverless.

DynamoDB Table

Table name: Users
Partition key: userId (String)

Python Code
POST Lambda (CreateUserFunction)

See POST/index.py

GET Lambda (GetUsersFunction)

See GET/index.py

API URL
https://oekboky8h9.execute-api.ap-south-1.amazonaws.com/prod/users