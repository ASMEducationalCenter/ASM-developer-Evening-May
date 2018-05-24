import boto3

client = boto3.resource('dynamodb')

table = client.Table('test-table1')

response=table.scan()

#print everything the scan returns
print (response)


for i in response["Items"]:
    print i["title"]
