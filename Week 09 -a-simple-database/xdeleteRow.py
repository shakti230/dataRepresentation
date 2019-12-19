import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  #user="root",  # this is the user name on my windows
  #passwd="password" # for my windows
  database="datarepresentation"
)

cursor = db.cursor()
sql="delete from student where id = %s"
values = (1,)

cursor.execute(sql, values)

db.commit()
print("delete done")