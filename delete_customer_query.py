import mysql.connector
from utilities.configurations import *

connection = get_connection()
curser = connection.cursor()

delete_query = "delete from CustomerInfo where CourseName = %s"
data = ("selenium",)
curser.execute(delete_query, data)
connection.commit()
connection.close()