from boto3.dynamodb.conditions import Key,Attr

ROUTE = "#ORIGIN:Vitória da Conquista, BA - Rodoviaria#DESTINATION:São Paulo, SP - Tiete"
start="2022-11-30"
end= "2022-12-30"
table_name = "PublicPrices-local"

# Get Item Example
def get_item(client):
    key = {"route":{"S":ROUTE},"departure_date": {"S":"2022-11-30"}}
    return client.get_item(TableName=table_name,Key=key)

# Count Example - 1
def count(table):
    response = table.query(
        Select='COUNT',
        KeyConditionExpression=Key("route").eq(ROUTE)
    )

#Count Example - 2
def count(table):
    response = table.item_count
   
# Query 1:  only route - all atributes
def get_by_route(table):
    return  table.query(
        Select='ALL_ATTRIBUTES',
        KeyConditionExpression=Key("route").eq(ROUTE)
    )

# Query 2: route and departure_date (sk and pk) - all atributes
def get_by_route_and_departure(table):
    return  table.query(
        Select="ALL_ATTRIBUTES",
        Limit=123,
        KeyConditionExpression=Key('route').eq(ROUTE) & Key('departure_date').between(start,end)
    )


# Query 3: with PK and SK and attrs (rival and busclass) -EXACTLY
def get_by_rivals_and_busclasses(table):
    busclasses = ["Convencional","Semileito"]
    rivals = ["Gil Turismo","Águia Branca"]
    
    return  table.query(
        Select="ALL_ATTRIBUTES",
        Limit=123,
        KeyConditionExpression=Key('route').eq(ROUTE) & Key('departure_date').between(start,end),
        FilterExpression=Attr('busclass').is_in(busclasses) & Attr('rival').is_in(rivals)
    )
