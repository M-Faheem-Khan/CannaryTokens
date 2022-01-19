# Name: notdankenoughq
# File: cannary_handler.py
# Description: Cannary Token Handler

import os
import boto3
import requests

table_name = os.eviron['DYNAMODB_TABLE']


def getIPGeoLocation(ip_addr):
    geo_location = {}
    base_url = 'http://ipinfo.io/'
    fmt = '/json'

    fields_to_ignore = ['readme', 'ip']

    # Getting IP Geo Location from ipinfo.io
    r = requests.get(f'{base_url}{ip_addr}{fmt}').json()    

    for key in r:
        if key not in fields_to_ignore:
            geo_location[key] = r[key]   
    
    return geo_location

    

# Event (Dictionary): Contains the contents of the event invoking the lambda handler 
# Context (Dictionary) : Lambda function context: information about the handler itself 
def lambad_handler(event, context):
    # Request & Parameters
    request = event['requestContext']
    parameters = event['queryStringParameters']

    token = parameters['token']

    ip_profile = {}
    user_agent = request['http']['userAgent']
    ip = request['http']['sourceIP']
    timestamp = request['time']
    geo_location = getIPGeoLocation(ip)

    # populating ip profile
    ip_profile['ip'] = ip
    ip_profile['timestamp'] = timestamp
    ip_profile['user_agent'] = user_agent

    ip_profile = {**ip_profile, **geo_location}

    # Find & Update token document
    dynamodb = boto3.resouce('dynamodb')
    table = dynamodb.Table(table_name)

    response = table.update_item(
        Key={
            'token': token
        },
        ExpressionAttributeNames={
            '#UA': 'user_agent',
            '#IP': 'ip'
        },
        ExpressionAttributeValues={
            ':ua': {
                'S': "{}".format(user_agent)
            },
            ':ip': {
                'S': "{}".format(ip)
            }
        },
        UpdateExpression="ADD #UA=:ua, #IP=:ip",
        ReturnValues="UPDATED_NEW"
    )

    print(response)
    
    # If the token paramters is not given in the GET request
    if 'token' not in parmaters:
        return {
            'statusCode': 200,
            'body': "No token sent!!"
        }
    
    
    return 'Hello Twitch'




# EOF