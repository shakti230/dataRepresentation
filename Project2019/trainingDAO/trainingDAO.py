from application import trainingDAO.py

import mysql.connector

class trainingDAO:
    db = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="datarep"
        )

    cursor = db.cursor()
    sql="CREATE TABLE courses (id INT AUTO_INCREMENT PRIMARY KEY, course_name VARCHAR(200), description VARCHAR(400)"
    cursor.execute(sql, values)
    db.commit()

    def create(values):
        cursor = db.cursor()
        sql="insert into training (course_name, id, price) values (%s,%s,%s)"
        cursor.execute(sql, values)
        db.commit()


    def getAll():
        cursor = db.cursor()
        sql="select * from training"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(id):
        cursor = db.cursor()
        sql="select * from training where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        return convertToDictionary(result)

    def update(values):
        cursor = db.cursor()
        sql="update training set course_name= %s, id=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        db.commit()
    def delete(id):
        cursor = db.cursor()
        sql="delete from training where id = %s"
        values = (id)

        cursor.execute(sql, values)

        db.commit()
        print("delete complete")

trainingDAO = trainingDAO()