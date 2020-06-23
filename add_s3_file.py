import json
import boto3


def lambda_handler(event, context):
    s3 = boto3.client("s3")
    if event:
        print("Event : ", event)
        file_name = str(event["Records"][0]['s3']['object']['key'])
        print("Filename is ", file_name)
        fileobj = s3.get_object(Bucket="aws-druk-test", Key=file_name)
        filecontent = fileobj['Body'].read().decode('utf-8')
        print(filecontent)

    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
