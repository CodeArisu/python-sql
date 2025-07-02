import mysql.connector
from layout.config import config
from common.queries import query_select, query_insert

def main():
    # Get database configuration from environment variables
    db_config = config()
    # Create a connection to the database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to the database")

        query_select("colors", connection)
        # query_insert("colors", "color", "Orange", connection)
        
        connection.close()
    else:
        print("Failed to connect to the database")
        return


main()