import botocore
import os
from entities import Cat
import dynamodb

class DynamoDBRepository:
    def __init__(self):
        self.table_name = os.getenv('TABLE_NAME','Cats-local')
        self.table = self.get_or_create_table()

    def get_or_create_table(self):
        dyn_resource = dynamodb.get_client()
        print(self.table_name)
        existing_tables = dyn_resource.list_tables().get('TableNames')

        if self.table_name in existing_tables:
            return dynamodb.get_table(self.table_name)
        else:
            self.create_table(dyn_resource)

    def create_table(self,dyn_resource):
        try:
            self.table = dyn_resource.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {'AttributeName': 'eyes', 'KeyType': 'HASH'},
                    {'AttributeName': 'age', 'KeyType': 'RANGE'},
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'eyes', 'AttributeType': 'S'},
                    {'AttributeName': 'age', 'AttributeType': 'S'},
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 10,
                    'WriteCapacityUnits': 10,
                },
            )
        except botocore.exceptions.ClientError as err:
            print(
                "Couldn't create table %s. Here's why: %s: %s",
                self.table_name,
                err.response['Error']['Code'],
                err.response['Error']['Message'],
            )
            raise
        else:
            return self.table
        
    def add_item(self,cat:Cat):
        try:
            self.table.put_item(
                Item={
                    **cat.get_attributes()
                }
            )
            print(f"{cat.__dict__} Criado com sucesso")

        except botocore.exceptions.ClientError as err:
            print(err.response['Error']['Code'], err.response['Error']['Message'])
            raise