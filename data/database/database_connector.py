import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv('DB_HOST'),
  user=os.getenv('DB_NAME'),
  passwd=os.getenv('DB_PW'),
  database=os.getenv('DB')
)

def executeQuery(query: str, params:list = [], fetch: bool = False):
    """ Execute a query and return the result. """
    with mydb.cursor(dictionary=True, buffered=True) as mycursor:
        mycursor.execute(query, params)
        mydb.commit()
        return mycursor.fetchall() if fetch else None

def selectQuery(query: str, params:list = []):
    """ Select data from the database. """
    return executeQuery(query, params, True)

def insertQuery(query, params = []):
    """ Insert data into the database. """
    return executeQuery(query, params, False)