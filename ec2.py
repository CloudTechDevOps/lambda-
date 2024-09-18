import boto3
#def lambda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instances(
    ImageId='ami-001843b876406202a',
    InstanceType='t2.micro',
    KeyName='jenkin',
    MaxCount=1,
    MinCount=1
)
