import json
import boto3
import os
id = os.environ['image_id'] #ami-06b21ccaeff8cd686
instance_type = os.environ['type']
def lambda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instances(
   ImageId= id,
   InstanceType=instance_type,
   KeyName='eksk8s',
   MaxCount=1,
   MinCount=1
)
