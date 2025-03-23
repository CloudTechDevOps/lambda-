import boto3
import json
from datetime import datetime

# Hardcoded CloudFront Distribution ID
CLOUDFRONT_DISTRIBUTION_ID = "E2J0IIVEQJMGIQ"  #give your cloudfront id

# Initialize CloudFront client
cloudfront_client = boto3.client("cloudfront")

def lambda_handler(event, context):
    try:
        # Create an invalidation request
        response = cloudfront_client.create_invalidation(
            DistributionId=CLOUDFRONT_DISTRIBUTION_ID,
            InvalidationBatch={
                "Paths": {
                    "Quantity": 1,
                    "Items": ["/*"]  # Invalidate all files
                },
                "CallerReference": str(datetime.utcnow().timestamp())  # Unique reference
            }
        )

        # Convert response to JSON-serializable format
        invalidation_id = response["Invalidation"]["Id"]
        create_time = response["Invalidation"]["CreateTime"].isoformat()  # Convert datetime to string

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Invalidation request sent successfully",
                "InvalidationId": invalidation_id,
                "CreateTime": create_time
            })
        }

    except Exception as e:
        print(f"Error creating invalidation: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": "Failed to create invalidation",
                "message": str(e)
            })
        }
