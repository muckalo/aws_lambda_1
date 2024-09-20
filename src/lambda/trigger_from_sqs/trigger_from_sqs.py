import json
import logging

from aws_xray_sdk.core import xray_recorder


logger = logging.getLogger()
logger.setLevel("INFO")


@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    logger.info('Start processing messages (SQS)')
    for message in event['Records']:
        process_message(message)
    logger.info('Finished processing messages (SQS)')


@xray_recorder.capture('process_message')
def process_message(message):
    try:
        msg = message['body']
        logger.info(f'msg: {type(msg)} - {msg}')
        msg_json = json.loads(msg)
        logger.info(f'msg_json: {type(msg_json)} - {msg_json}')
        first_name = msg_json['first_name']
        last_name = msg_json['last_name']
        full_name = f'First name: {first_name} - Last name: {last_name}'
        result = {'result': full_name}
        logger.info(f'result: {result}')
        return result
    except Exception as err:
        logger.error(f'exception: {err}')
        raise err
