import pymysql

# RDS Database connection details
RDS_HOST = 'my-rds-instance.cru0eyk6ukru.us-east-1.rds.amazonaws.com'
RDS_USER = 'admin'
RDS_PASSWORD = 'Cloud123'
NEW_DB_NAME = 'test'
TABLE_NAME = 'employees'

def create_database_and_table():
    connection = None  # Initialize the connection variable
    try:
        # Connect to MySQL server (without specifying a database)
        connection = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            connect_timeout=10  # Set a timeout for the connection
        )
        print("Connected to MySQL server.")

        with connection.cursor() as cursor:
            # Create a new database if it doesn't exist
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {NEW_DB_NAME};"
            cursor.execute(create_db_query)
            print(f"Database '{NEW_DB_NAME}' checked/created successfully.")

            # Use the new database
            cursor.execute(f"USE {NEW_DB_NAME};")
            print(f"Switched to database '{NEW_DB_NAME}'.")

            # Create a new table if it doesn't exist
            create_table_query = f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                age INT,
                department VARCHAR(100)
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
            print(f"Table '{TABLE_NAME}' checked/created successfully.")

    except pymysql.MySQLError as e:
        print(f"Error: {str(e)}")

    finally:
        # Close the connection only if it was established successfully
        if connection:
            connection.close()
            print("Connection closed.")

# Call the function to create the database and table
create_database_and_table()
