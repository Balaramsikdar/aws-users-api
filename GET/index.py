import json
import boto3

# Create DynamoDB resource
dynamo = boto3.resource('dynamodb')
table = dynamo.Table('Users')  # Make sure DynamoDB table name = Users

def lambda_handler(event, context):
    print("GET event:", event)

    try:
        # Scan gets all items from the table
        response = table.scan()
        items = response.get('Items', [])

        return {
            "statusCode": 200,
            "body": json.dumps(items)
        }

    except Exception as e:
        print("ERROR:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Server Error", "error": str(e)})
        }
