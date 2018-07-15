## Dynamo Lab Steps Part 1

1) Go to IAM and create a role for Lambda with Full DynamoDB access
2) Create a Lambda funtion from scratch.
3) Add createtable.py code found in this folder.
4) Add a test event. The test event can include anything for now. We just need this to invoke our Lamba funtion manually.
5) After creating the test event, click save and Test.
6) If you get a successful message, check your DynamoDB dashboard. There should be a table created.


## Dynamo Lab Steps Part 2

1) Remove the code from the function and add some new code from putItem.py file that's included in this repo.
2) Make some changes to the data if you want -- This step is optional
3) Save and Click Test. 
4) Check your DynamoDB table. There should be some new data.

# Dynamo Lab Steps Part 3

1) Remove the code from the function and add some new code from getItem.py file that's included in this repo.
2) Save and Click Test. 
3) You will be able to retrieve the data you stored in the table earlier.






