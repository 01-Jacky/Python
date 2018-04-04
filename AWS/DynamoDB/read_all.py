import boto3    # pip install boto3
from boto3.dynamodb.conditions import Key, Attr
import logging
import os

# Config variables
DYNAMODB_PARAMS = {
    'region_name' : 'us-west-2',
    'aws_access_key_id' : 'AKIAJK2D4VY67U2AJETA',
    'aws_secret_access_key' : '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',
}
ROUTE_TABLE_NAME = 'Routes'

# Get dynamoDB objects to work with
dynamodb = boto3.resource('dynamodb', **DYNAMODB_PARAMS)
table = dynamodb.Table(ROUTE_TABLE_NAME)

# Scan the whole table
print('Attempting to scan the table')
try:

    # Uncomment filtering expression if you want to filter down to a subset
    # fe = Key('popularity').between(3, 6)

    response = table.scan(
        # FilterExpression=fe,
    )

except Exception as e:
    print(e)
else:
    if response['Count'] > 0:  # If item exist
        for item in response['Items']:
            print(item)
    else:
        print('No items')
