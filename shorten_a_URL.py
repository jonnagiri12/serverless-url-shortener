import json
import boto3
import string
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    long_url = body['long_url']

    chars = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(chars, k=6))

    table.put_item(Item={
        'short_code': short_code,
        'long_url': long_url
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'short_code': short_code})
    }
