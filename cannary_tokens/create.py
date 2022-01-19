# Name: notdankenoughq
# File: create_cannary_token_handler.py
# Description: Generate Cannary Tokens

import os
import time
import uuid
import boto3 

table_name = os.environ['DYNAMODB_TABLE']
dynamodb = boto3.resource('dynamodb')


# Event (Dictionary): Contains the contents of the event invoking the lambda handler 
# Context (Dictionary) : Lambda function context: information about the handler itself 
def lambda_handler(event, context):
    token = str(uuid.uuid4())
    timestamp = str(time.time())
    table = dynamodb.Table(table_name)
    response = table.put_item(Item={
        'token': token
        'createdAt': timestamp,
        'updatedAt': timestamp
    })

    return {
        'statusCode': 200,
        'body': token
    }


# EOF