import urllib.parse
import json
import boto3


def lambda_handler(event, context):
    aws_region = "us-east-1"
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        region_name=aws_region
    )

    bucket = event['Records'][0]['s3']['bucket']['name']

    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:
        response = s3.get_object(Bucket=bucket, Key=key)

        text = response['Body'].read().decode()
        data = json.loads(text)

        transactions = data['transactions']
        for record in transactions:
            print(record['transType'])
        return 'Success!'

    except Exception as e:
        print(e)
        raise e
