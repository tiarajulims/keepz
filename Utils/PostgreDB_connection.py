# Your Python script
import os
import psycopg2

# Load configuration from .env file

# Access database credentials
db_name = os.environ.get('DATABASE_NAME')
db_user = os.environ.get('DATABASE_USER')
db_password = os.environ.get('DATABASE_PASSWORD')
db_host = os.environ.get('DATABASE_HOST')
db_port = os.environ.get('DATABASE_PORT')

db_params = {
    'host': "dev-wallet-pg.cssbbqhvgpeu.eu-central-1.rds.amazonaws.com",
    'database': "sweeft_wallet",
    'user': "postgres",
    'password': "ODvs0u27eO0MjUpzHGPD",
    'port': 5432
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute('''SELECT * from "sweeft_wallet"."sweeft_wallet_common"."merchant_account"''')
    version = cursor.fetchall()
    print(version)

except psycopg2.Error as e:
    print("Unable to connect to the database:", )




