Steps
1) Go to IAM and create a role for lambda with DynamoDB access
2) Create a lambda function and Attach the new role
3) Paste code for createTable.py and Run/Test the Function. Create a simple test case( we don't care about the contents).
4) At this point the table is created. Paste the code for Put Item in the code box. And Run/Test your function.
3) Check your DynamoDB Console. You should see that the table is updated. 
5) Replace the code with contents of GetItem.py file . Retrive the file and print the logs as output. 
6) Work with Cloudwatch logs to view outputs. 

-----

## OPTIONAL STEPS: 

7) Create an Alarm and notify if function fails X times. 
