import boto3

def lambda_handler(event, context):
 
    
    
    client = boto3.client('dynamodb')
    
    response = client.create_table(
    TableName='test-table1',
    #this is the attribute keys and type
    AttributeDefinitions=[
            {
            'AttributeName': 'name',
            'AttributeType': 'S'
            }
        ],
    #This is the primary key
    KeySchema=[
            {
            'AttributeName': 'name',
            'KeyType': 'HASH'
            }
        ],
            
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
            }
    )
