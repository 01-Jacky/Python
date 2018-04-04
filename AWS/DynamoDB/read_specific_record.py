import boto3    # pip install boto3
import logging
import os

# Configs
DYNAMODB_PARAMS = {
    'region_name' : 'us-west-2',
    'aws_access_key_id' : 'AKIAJK2D4VY67U2AJETA',
    'aws_secret_access_key' : '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',
}
ROUTE_TABLE_NAME = 'Routes'

# Get all
def get_route(table, routeID='999'):
    print('Attempting to get item')
    try:
        response = table.get_item(
            Key={
                'routeID': '999',           # dummy entry in DB with routeID '999' for testing
            }
        )

    except Exception as e:
        print(e)
    else:
        if 'Item' in response:  # If item exist
            item = response['Item']
            print(item)
        else:
            print('No item matching the key')

dynamodb = boto3.resource('dynamodb', **DYNAMODB_PARAMS)
route_table = dynamodb.Table(ROUTE_TABLE_NAME)

get_route(route_table)