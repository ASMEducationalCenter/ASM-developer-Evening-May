import boto3

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
    ]
)
