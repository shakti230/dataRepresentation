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
sql="CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)"

cursor.execute(sql)