# Project manual
## How to deploy this lambda function

### Set environment

Setup node.js

Run `npm install` in root folder

### 1. Configure AWS Credential in local side
Setup AWS Cli in local side

`npm install -g aws-cli`

Setup AWS access-key-id and secret-access-key in local side

`aws configure`

### 2. Configure serverless.yml

Set environment variables

`environment:`

`    aws_access_key_id: # Add aws_access_key_id here`

`    aws_secret_access_key: # Add aws_secret_access_key here`

Set bucket name

`bucket: uploads-11111 # Change into the bucket name you want`

Here, `uploads-11111` means bucket name

### 3. Run the command to deploy

`sls deploy`

Go to https://s3.console.aws.amazon.com/s3/home, and select the bucket.
You will be able to see new bucket name you set in this lambda function

## How to perform to test this project

### 1. Upload file to test this function

Go to the bucket(https://s3.console.aws.amazon.com/s3/home),
create new folder "Incoming".
And to test this lambda function, upload a file into the folder.

### 2. Monitor log of this function

Go to Cloud watch(https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logs:)
Search this lambda function with prefix, ie. "/aws/lambda/file.
And then you can see logs for this function.
