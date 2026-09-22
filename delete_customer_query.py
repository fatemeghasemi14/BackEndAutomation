import mysql.connector
import os

#host, database, user, password
connection = mysql.connector.connect(host='localhost',
                        database='PythonAutomation',
                        user='root',
                        password=os.getenv("MYSQL_PASSWORD"))
curser = connection.cursor()

delete_query = "delete from CustomerInfo where CourseName = %s"
data = ("selenium",)
curser.execute(delete_query, data)
connection.commit()
connection.close()