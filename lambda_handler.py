import json

def lambda_handler(event, context):
    # TODO implement
	print("these are the changes that need tpo be deployed")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
