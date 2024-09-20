import json
import logging

from aws_xray_sdk.core import xray_recorder


logger = logging.getLogger()
logger.setLevel("INFO")


@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):
    logger.info('Start processing messages (SNS)')
    logger.info(f'event: {type(event)} - {event}')
    for message in event['Records']:
        process_message(message)
    logger.info('Finished processing messages (SNS)')


@xray_recorder.capture('process_message')
def process_message(message):
    try:
        record_sns = message['Sns']
        logger.info(f'record_sns: {type(record_sns)} - {record_sns}')
        record_sns_subject = record_sns['Subject']
        logger.info(f'record_sns_subject: {type(record_sns_subject)} - {record_sns_subject}')
        record_sns_msg = record_sns['Message']
        logger.info(f'record_sns_msg: {type(record_sns_msg)} - {record_sns_msg}')
        record_sns_msg_json = json.loads(record_sns_msg)
        logger.info(f'record_sns_msg_json: {type(record_sns_msg_json)} - {record_sns_msg_json}')
        first_name = record_sns_msg_json['first_name']
        last_name = record_sns_msg_json['last_name']
        full_name = f'First name: {first_name} - Last name: {last_name}'
        result = {'result': full_name}
        logger.info(f'result: {result}')
        return result
    except Exception as err:
        logger.error(f'exception: {err}')
        raise err
