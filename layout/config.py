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