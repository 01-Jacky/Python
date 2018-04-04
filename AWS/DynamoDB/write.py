import boto3    # pip install boto3
import json
from decimal import *

# Configs
DYNAMODB_PARAMS = {
    'region_name' : 'us-west-2',
    'aws_access_key_id' : 'AKIAJK2D4VY67U2AJETA',
    'aws_secret_access_key' : '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',
}
ROUTE_TABLE_NAME = 'Routes'

# Prep mock item
MOCK_ITEM = json.load(open('mock_item.json'))
coordinates = MOCK_ITEM['coordinates']

coordinates_decimal = []
for coordinate in coordinates:
    lat  = Decimal(str(coordinate[0]))
    long = Decimal(str(coordinate[1]))
    coordinates_decimal.append([lat, long])
MOCK_ITEM['coordinates'] = coordinates_decimal


# write record to db
def insert_route(table):
    print('Attempting to write item')
    try:
        response = table.put_item(
            Item=MOCK_ITEM
        )

    except Exception as e:
        print("Exception")
        print(e)
    else:
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:  # If item exist
            print('Inserted')
        else:
            print('Failed to insert')


dynamodb = boto3.resource('dynamodb', **DYNAMODB_PARAMS)
route_table = dynamodb.Table(ROUTE_TABLE_NAME)

insert_route(route_table)