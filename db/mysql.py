# This file contains primary functions that handles mysql query executions
import pymysql
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def connectDB():
    """
    This function connect mysql db and returns connect instance or None if fails
    """
    DB_HOST = os.environ['DBHOST']
    DB_USER = os.environ['DBUSER']
    DB_PASS = os.environ['DBPASS']
    DB_NAME = os.environ['DBNAME']
    try:
        return pymysql.connect(host=DB_HOST, port=3306, user=DB_USER, password=DB_PASS, db=DB_NAME)
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        return None

def closeConnection(conn):
    """
    Close the connection
    """
    conn.close()

def executeQuery(conn, query):
    """
    Execute query and returns True if success and False if failed
    """
    try:
        with conn.cursor() as cur:
            cur.execute(query)
        conn.commit()
        return True
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not execute sql query.")
        logger.error(e)
        return False

