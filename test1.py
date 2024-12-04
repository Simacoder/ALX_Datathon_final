import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyodbc
from sqlalchemy import create_engine

# Replace these variables with your database connection details
db_user = 'Administrator'
db_password = 'B1b9915'
db_host = '10.2.60.26/MSSQLSERVER01'  
db_port = '1433'  # Default SQL Server port is 1433,
db_name = 'Datathon2024'

# Create the connection string for SQLAlchemy using pyodbc
connection_string = f'mssql+pyodbc://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?driver=ODBC+Driver+17+for+SQL+Server'

# Create the database engine
engine = create_engine(connection_string)

# Query to get all table names in the database (optional step)
table_query = """
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_CATALOG = 'Datathon2024'
"""
# Fetch table names
tables_df = pd.read_sql(table_query, engine)
print("List of Tables:")
print(tables_df)

# Query to select all data from the 'Person' table
query = 'SELECT * FROM Person'

# Read data into a pandas DataFrame
df = pd.read_sql(query, engine)

# Display the first few rows of the DataFrame
print("First few rows of the 'Person' table:")
print(df.head())
