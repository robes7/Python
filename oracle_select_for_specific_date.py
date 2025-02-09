import cx_Oracle
import pandas as pd
from datetime import datetime

# Connection details
dsn_tns = cx_Oracle.makedsn('hostname', 'port', service_name='servicename')
conn = None

# Accept user input for the date
user_date = input("Enter the date to check (format DD.MM.YYYY): ")

try:
    # Establish the connection
    conn = cx_Oracle.connect(user='user', password='password', dsn=dsn_tns)
    print("Successfully connected to the database")

    # Prepare the SQL queries with placeholders for the date
    sql_queries = [
        """
        PASTE SQL QUERY HERE
        """
    ]

    records_found = False

    for sql_query in sql_queries:
        # Use the parameter in the query execution
        df = pd.read_sql(sql_query, conn, params={'user_date': user_date})
        print(df.columns)  # Debugging line to check column names

        # Since we are directly querying for the user-specified date, the logic below is adjusted
        if df.empty:
            print("No records found for the specified date.")
        else:
            records_found = True
            print(f"Records for {user_date} found.")
            break

    if not records_found:
        print(f"No records for {user_date} were found.")

except cx_Oracle.DatabaseError as e:
    print(f"Database connection failed: {e}")

finally:
    if conn is not None:
        conn.close()
        print("Database connection closed")
