import configparser
import mysql.connector
from mysql.connector import Error
import os

def get_config():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config

connect_config = {
    'host' : get_config()['SQL']['host'],
    'database' : get_config()['SQL']['database'],
    'user' : get_config()['SQL']['user'],
    'password' : os.getenv('MYSQL_PASSWORD')
}

def get_connection():
    try:
        connection = mysql.connector.connect(**connect_config)
        if connection.is_connected():
            print("Successfully connected to MySQL database")
            return connection
    except Error as e:
        print(e)