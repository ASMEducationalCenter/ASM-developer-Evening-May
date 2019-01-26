# Steps
1) Create an IAM role with EC2 permissions and also Cloudwatch permissions for logging.
2) Create a lambda function and attach this newly created role
3) Copy the contents of lambda_function.py to the code box
4) create a test event. **Contents of the test event not important.**
5) Start 2 EC2 Instances 
6) Run the Lambda function
7) Check your EC2 Instance
8) Start your EC2 Instances
9) Open Cloudwatch Dashboard and click on events.
10) Create a event rule to stop ec2 at the current time +5 minutes CRON schedule. Associate the rule to the lambda funciton
11) Wait a few mins
12) Check your EC2 Instances. They should be stopped

## Optional steps
1) Look up boto3 documentation
2) Start the instances with boto3 code changes to the Lambda function
3) Terminate the instance with Lambda function



