import pyodbc

def get_connection():
    conn =pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost,1433;"
    "DATABASE=flashyDB;"
    "UID=basmala;"
    "PWD=yellow0330;"
    "TrustServerCertificate=yes;"
    )
    return conn