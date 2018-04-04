import boto3
import os

DYNAMODB_PARAMS = {
    'region_name' : 'us-west-2',
    'aws_access_key_id' : os.environ['aws_access_key_id'],
    'aws_secret_access_key' : os.environ['aws_secret_access_key'],
}

dynamodb = boto3.resource('dynamodb', **DYNAMODB_PARAMS)
table = dynamodb.Table('JobInternships')

try:
    response = table.get_item(
        Key={
            'date': '2018-01-29',
            'jobID': 'AASKITechnology_EngineeringIntern',
        }
    )

except Exception as e:
    print(e)
else:
    if 'Item' in response:  # If item exist
        item = response['Item']