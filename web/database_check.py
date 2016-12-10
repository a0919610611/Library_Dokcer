#!/usr/bin/env python3
import os
import sys
import MySQLdb

def database_check():
    dbname = os.environ.get('MYSQL_DATABASE')
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
    host = "db"
    port = 3306

    print("HOST: {host}:{port}, DB: {dbname}, USER: {user}".format(
        dbname=dbname,
        user=user,
        host=host,
        port=port))

    try:
        MySQLdb.connect(
            db=dbname,
            user=user,
            passwd=password,
            host=host,
            port=port)
    except:
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    database_check()
