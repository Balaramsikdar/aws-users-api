import json
import uuid
import boto3

dynamo = boto3.resource('dynamodb')
table = dynamo.Table('Users')  # make sure your table is named 'Users'

def lambda_handler(event, context):
    print("Event:", event)

    # 1) Try to get body like API Gateway sends it
    body = {}
    if isinstance(event, dict) and "body" in event:
        try:
            if isinstance(event["body"], str):
                body = json.loads(event["body"] or "{}")
            elif isinstance(event["body"], dict):
                body = event["body"]
        except Exception as e:
            print("Error parsing event['body']:", e)
            body = {}
    else:
        # 2) If no 'body', maybe test event sent JSON directly
        if isinstance(event, dict):
            body = event

    name = body.get("name")
    email = body.get("email")

    if not name or not email:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "name and email are required"})
        }

    user_id = str(uuid.uuid4())

    table.put_item(
        Item={
            "userId": user_id,
            "name": name,
            "email": email
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "User added", "userId": user_id})
    }
