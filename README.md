# AWS Websocket Messaging

> This repo contains Serverless Framework project for a simple AWS Websocket chat app

### Setup

> Install required npm packages first

```shell
$ npm install
```

> Install Serverless Framework globally

```shell
$ npm install -g serverless@1.48.2
```

> Install required Python packages

```shell
$ pip install -r python-packages.txt -t ./lib/python
```

> Deploy into AWS

```shell
$ serverless deploy --stage dev
```

Make sure to add 'AdministratorAccess' for Lambda Role
Use Following Code to Send Log messagaes

```shell
import boto3
import json
lambda_client = boto3.client('lambda')

def LogAWSWebSocketMessage(message):
    lambda_client.invoke(
        FunctionName="AWSWebSocketLogger-dev-onMessageHandler",
        InvocationType='Event',
        Payload=json.dumps({'message': message})
    )
```