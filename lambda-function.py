import boto3

lambda_client = boto3.client('lambda', region_name='us-east-1')

response = lambda_client.create_function(
    Code={
        'S3Bucket': 'nareshawsdev',
        'S3Key': 'lambda.zip',  # Use the name of your ZIP file
    },
    Description='Process image objects from Amazon S3.',
    FunctionName="check-lambda",
    Handler='lambda-function.lambda_handler',
    Publish=True,
    Role='arn:aws:iam::703671931980:role/lambda-admin',
    Runtime='python3.12'
)
