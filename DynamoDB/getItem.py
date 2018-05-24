import boto3

client = boto3.resource('dynamodb')


table= client.Table('test-table1')
response = table.get_item(
        Key={
            'name': 'Saurav'

        }
    )


print (response['Item']['info']['plot'])
