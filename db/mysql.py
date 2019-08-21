import pymysql
import logging
import os
import config

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def connectDB():
    """
    This function connect mysql db
    """
    DB_HOST = config.DB['MYSQLHOST']
    DB_USER = config.DB['MYSQLUSER']
    DB_PASS = config.DB['MYSQLPASS']
    DB_NAME = config.DB['MYSQLDATABASE']
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
    Execute query
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

