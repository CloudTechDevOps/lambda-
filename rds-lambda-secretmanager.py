import json
import boto3
import pymysql
import os 
# Define DB and table
new_db_name = "test"
table_name = "mytable"

# Get RDS credentials from AWS Secrets Manager
def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)

    secret = response['SecretString']
    return json.loads(secret)

# Connect to RDS
def connect_to_rds(secret):
    connection = pymysql.connect(
        host=os.environ['host'],
        user=secret['username'],
        password=secret['password'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# Lambda handler
def lambda_handler(event, context):
    secret_name = "rds!db-b6e6b6a3-f337-4c9d-9ace-7de0a88e602b"  # Replace with your secret name
    try:
        secret = get_secret(secret_name)
        connection = connect_to_rds(secret)
        
        with connection.cursor() as cursor:
            # Create database if not exists
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {new_db_name};")
            cursor.execute(f"USE {new_db_name};")

            # Create table if not exists
            cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)

        return {
            'statusCode': 200,
            'body': f"Database '{new_db_name}' and table '{table_name}' created successfully."
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': str(e)
        }
    finally:
        if 'connection' in locals():
            connection.close()
