import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
  #user="root",  # this is the user name on my windows laptop
  #passwd="password" # for my windows laptop
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")