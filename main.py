import mysql.connector
from common.queries import query_select, query_insert


def config():
    import os
    from dotenv import load_dotenv
    # Load environment variables from .env file
    load_dotenv()
    # Load environment variables from .env file
    # Ensure you have a .env file with the following variables:
    return {
        'host': os.getenv('DB_HOST', 'localhost'),
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', ''),
        'database': os.getenv('DB_NAME', 'testdb')
    }


def main():
    # Get database configuration from environment variables
    db_config = config()
    # Create a connection to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to the database")

        # query_select("SELECT * FROM", "colors", connection)
        query_insert("INSERT INTO", "colors", "color", "Violet", connection)
        
        connection.close()
    else:
        print("Failed to connect to the database")
        return


main()