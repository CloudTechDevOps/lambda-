import boto3
client=boto3.client('s3')
response = client.create_bucket(
    Bucket='qwertyuioasdfgh',

    CreateBucketConfiguration={
        'LocationConstraint': "ap-south-1",
}
)
