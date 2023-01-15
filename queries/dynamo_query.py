from boto3.dynamodb.conditions import Key,Attr

table_name = "Cats-local"

# Get Item Example
def get_item(client,color):
    key = {"color_eyes":{"S":color},"age": {"N":12}}
    return client.get_item(TableName=table_name,Key=key)

# Count Example - 1
def count(table):
    response = table.query(
        Select='COUNT',
        KeyConditionExpression=Key("color_eyes").eq("Blue")
    )

#Count Example - 2
def count(table):
    response = table.item_count
   
# Query 1:  only color_eyes - all atributes
def get_by_color(table):
    return  table.query(
        Select='ALL_ATTRIBUTES',
        KeyConditionExpression=Key("color_eyes").eq("Black")
    )

# Query 2: color_eyes and age (sk and pk) - all atributes
def get_by_pk(table):
    return  table.query(
        Select="ALL_ATTRIBUTES",
        Limit=123,
        KeyConditionExpression=Key('color_eyes').eq("Orange") & Key('age').between(1,5)
    )


# Query 3:
def get_by_attrs(table):    
    return  table.query(
        Select="ALL_ATTRIBUTES",
        Limit=123,
        KeyConditionExpression=Key('color_eyes').eq("Blue") & Key('age').between(1,3),
        FilterExpression=Attr('body_color').is_in(["Black","Orange"])
    )
