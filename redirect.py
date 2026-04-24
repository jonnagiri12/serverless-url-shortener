import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url-shortener')

def lambda_handler(event, context):
    short_code = event['pathParameters']['short_code']

    result = table.get_item(Key={'short_code': short_code})

    if 'Item' not in result:
        return {'statusCode': 404, 'body': 'URL not found'}

    long_url = result['Item']['long_url']

    return {
        'statusCode': 301,
        'headers': {'Location': long_url},
        'body': ''
    }
