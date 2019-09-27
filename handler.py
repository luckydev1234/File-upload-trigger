import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def readAndWriteS3File(event, context):
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('aws_access_key_id'),
        aws_secret_access_key=os.getenv('aws_secret_access_key')
    )
    # retrieve bucket name and file_key from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    logger.info('Reading {} from {}'.format(file_key, bucket_name))
    # get the object
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    # get lines inside the csv
    file = obj['Body'].read()
    file_name = file_key[file_key.find('/') + 1:]
    logger.info('Got {} from s3: '.format(file_name))
    logger.info('Printing file...')
    print(file)
    logger.info('Ended printing file!')
    processed_file_key = 'Processed/' + file_name
    s3.put_object(Bucket=bucket_name, Key=processed_file_key, Body=file)
    logger.info('Writing {} from {}'.format(processed_file_key, bucket_name))
    s3.delete_object(Bucket=bucket_name, Key=file_key)
    logger.info('Deleting {} from {}'.format(file_key, bucket_name))
