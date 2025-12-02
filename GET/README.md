# AWS Serverless Users API (Python)

This project implements a serverless REST API for user management using AWS Lambda (Python), API Gateway, and DynamoDB. It allows creating and retrieving users with fully managed, scalable backend infrastructure — no servers required.

---

## 🚀 Features

- `POST /users` — Create a new user  
- `GET /users` — Retrieve all users  
- DynamoDB database persistence  
- UUID user identifiers  
- Secure IAM-based access  
- Fully serverless & scalable  
- Low cost — AWS Free Tier friendly  

---

## 🧰 Technologies Used

- AWS Lambda (Python)
- API Gateway
- DynamoDB
- IAM roles
- boto3 AWS SDK

---

## 🌐 API Endpoint

https://oekboky8h9.execute-api.ap-south-1.amazonaws.com/prod/users



### Supported Methods
| Method | Description |
|---------|------------|
| POST | Create user |
| GET | Fetch all users |

---

# 📦 Example Usage

## 🔹 POST /users

### Request
```json
{
  "name": "Balaram",
  "email": "test@gmail.com"
}

Response
{
  "message": "User added",
  "userId": "c3282940-3c45-41a7-a1c2-c34680424fb6"
}

🔹 GET /users

Response
[
  {
    "userId": "c3282940-3c45-41a7-a1c2-c34680424fb6",
    "name": "Balaram",
    "email": "test@gmail.com"
  }
]

🗄 DynamoDB Table Structure

| Field  | Type   | Key           |
| ------ | ------ | ------------- |
| userId | String | Partition Key |
| name   | String | -             |
| email  | String | -             |


🧠 Architecture

Client
  ↓
API Gateway
  ↓
Lambda (Python)
  ↓
DynamoDB

🐍 Lambda Code Location

| Action      | Lambda File   |
| ----------- | ------------- |
| POST /users | POST/index.py |
| GET /users  | GET/index.py  |

🔐 IAM Permissions

{
  "Effect": "Allow",
  "Action": [
    "dynamodb:PutItem",
    "dynamodb:Scan"
  ],
  "Resource": "arn:aws:dynamodb:*:*:table/Users"
}

