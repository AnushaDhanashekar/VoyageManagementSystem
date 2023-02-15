import boto3
import json


def handler(event, context):
    http_method = event['httpMethod']
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Vms')
    if http_method == 'GET':
        vesselId = event['queryStringParameters']['vesselId']
        result = table.get_item(Key={'vesselId': vesselId})
        if 'Item' in result:
            response = {
                'statusCode': 200,
                'body': json.dumps(result['Item'])

            }
        else:
            response = {
                'statusCode': 200,
                'body': json.dumps(result)

            }
    elif http_method == 'POST':
        data = json.loads(event["body"])
        table.put_item(
            Item={
                'vesselId': data['vesselId'],
                'vesselName': data['vesselName'],
                'speed': data['speed'],
                'latitude': data['latitude'],
                'longitude': data['longitude']
            }
        )
        request_body = json.loads(event['body'])
        response = {
            'statusCode': 200,
            'body': json.dumps(
                {'message': f'This is a POST request with data: {request_body}. Data stored successfully.'})
        }
    else:
        response = {
            'statusCode': 400,
            'body': json.dumps({'message': f'Unsupported HTTP method: {http_method}'})
        }
    return response

