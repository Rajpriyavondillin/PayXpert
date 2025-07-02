import mysql.connector
from util.DBPropertyUtil import DBPropertyUtil

def get_connection():
    props = DBPropertyUtil.get_db_properties()
    return mysql.connector.connect(
        host=props["host"],
        user=props["user"],
        password=props["password"],
        database=props["database"]
    )
