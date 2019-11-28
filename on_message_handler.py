import json
import boto3
import os

dynamodb = boto3.client('dynamodb')

def handle(event, context):
    message = event['message']
    
    paginator = dynamodb.get_paginator('scan')
    
    connectionIds = []
    
    # Retrieve all connectionIds from the database
    for page in paginator.paginate(TableName=os.environ['SOCKET_CONNECTIONS_TABLE_NAME']):
        connectionIds.extend(page['Items'])

    # Emit the recieved message to all the connected devices
    for connectionId in connectionIds:
        apigatewaymanagementapi = boto3.client('apigatewaymanagementapi', 
        endpoint_url = connectionId['WebSocketEndpointURL']['S'])

        apigatewaymanagementapi.post_to_connection(
            Data=message + ' | ConnectionID: ' + connectionId['connectionId']['S'],
            ConnectionId=connectionId['connectionId']['S']
        )

    return {}


## Run this Code in the required lambda
# import boto3
# import json
# lambda_client = boto3.client('lambda')

# def LogAWSWebSocketMessage(message):
#     lambda_client.invoke(
#         FunctionName="AWSWebSocketLogger-dev-onMessageHandler",
#         InvocationType='Event',
#         Payload=json.dumps({'message': message})
#     )