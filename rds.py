import boto3

# Initialize a session using your credentials
rds_client = boto3.client('rds')

# Parameters for the RDS instance
db_instance_identifier = 'my-rds-instance'  # RDS instance identifier
db_instance_class = 'db.t3.micro'  # Instance class (for smaller DBs)
engine = 'mysql'  # Database engine (e.g., 'mysql', 'postgres', 'oracle-se2', 'mariadb', etc.)
master_username = 'admin'  # Master username for the DB
master_user_password = 'Cloud123'  # Strong password
allocated_storage = 20  # Allocated storage in GB
db_name = 'mydb'  # Name of your initial database

try:
    response = rds_client.create_db_instance(
        DBInstanceIdentifier=db_instance_identifier,
        AllocatedStorage=allocated_storage,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_user_password,
        DBName=db_name,
        BackupRetentionPeriod=7,  # Optional: Retain backups for 7 days
        Port=3306,  # Default MySQL port
        MultiAZ=False,  # Single Availability Zone
        PubliclyAccessible=True,  # Whether to assign a public IP
        StorageType='gp2',  # General Purpose SSD storage
        Tags=[
            {'Key': 'Name', 'Value': 'MyRDSInstance'},  # Optional: Tags
        ]
    )
    print(f"RDS instance '{db_instance_identifier}' creation initiated. Status: {response['DBInstance']['DBInstanceStatus']}")
except Exception as e:
    print(f"Error creating RDS instance: {str(e)}")
