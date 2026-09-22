import mysql.connector
import os

#host, database, user, password
connection = mysql.connector.connect(host="localhost",
                                     database="PythonAutomation",
                                     user="root",
                                     password=os.getenv("MYSQL_PASSWORD"))

print(connection.is_connected())

cursor = connection.cursor()
cursor.execute("select * from CustomerInfo")

# first_row = cursor.fetchone()
# print(first_row) # return tuple

# all_row = cursor.fetchall()
# print(all_row) # return list of tuples

# return all records and calculate amount's sum
rows = cursor.fetchall()
sum = 0
for row in rows:
    sum = sum + row[2]
print(sum)

# update one row of CustomerInfo table
query = "update PythonAutomation.CustomerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
connection.commit()
connection.close()