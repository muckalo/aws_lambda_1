import json
import logging

from aws_xray_sdk.core import xray_recorder


logger = logging.getLogger()
logger.setLevel("INFO")


@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    logger.info('Start processing messages (SQS)')
    logger.info(f'event: {type(event)} - {event}')
    query_string_params = event['queryStringParameters']
    logger.info(f'query_string_params: {type(query_string_params)} - {query_string_params}')
    result = process_message(query_string_params)
    logger.info('Finished processing messages (SQS)')
    return {
        'statusCode': 200,
        'body': json.dumps(result),
    }


@xray_recorder.capture('process_message')
def process_message(query_string_params):
    try:
        first_name = query_string_params['first_name']
        last_name = query_string_params['last_name']
        full_name = f'First name: {first_name} - Last name: {last_name}'
        result = {'result': full_name}
        logger.info(f'result: {type(result)} - {result}')
        return result
    except Exception as err:
        logger.error(f'exception: {err}')
        raise err
