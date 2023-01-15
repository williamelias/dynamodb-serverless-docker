import boto3
import os

REGION = os.getenv('REGION',"eu-west-1")
TABLE_NAME= os.getenv('TABLE_NAME','Cats-local')

def get_source_attrs():
    attrs = {
        'region_name':REGION,
    }
    if os.getenv('STAGE') not in ['staging','production']:
        attrs.update(
            {
                'endpoint_url':'http://dynamodb-local:8000'
            }
        )
    
    print(attrs)
    return attrs


def get_client():
    dyn_resource = boto3.client(
        "dynamodb",
        **get_source_attrs()
    )

    return dyn_resource
    
def get_table(table_name=TABLE_NAME):
    dynamodb = boto3.resource(
        "dynamodb",
        **get_source_attrs()
    )
    return dynamodb.Table(table_name)