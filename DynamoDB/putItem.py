import boto3
def lambda_handler(event, context):
        client = boto3.resource('dynamodb')

        table = client.Table('test-table1')
        response= table.put_item( Item={
                'name': 'Sanjog',
                'title': 'Paralegal',
                'info': {
                    'plot':"Nothing happens at all.",
                    'rating': 10
                }
            })


        print(response["Items"][0])
