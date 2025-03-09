import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="employee"
)

mycursor = mydb.cursor()
crate_table = "CREATE TABLE IF NOT EXISTS emp (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, salary INT)"
mycursor.execute(crate_table)
class Sql:
    def __init__(self):
        pass

    def insert(self, name, age, salary):
        sql = "INSERT INTO emp (name, age, salary) VALUES (%s, %s, %s)"
        val = (name, age, salary)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def select(self):
        mycursor.execute("SELECT * FROM emp")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def update(self, name, age, salary):
        sql = "UPDATE emp SET age = %s, salary = %s WHERE name = %s"
        val = (age, salary, name)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")

    def delete(self, name):
        sql = "DELETE FROM emp WHERE name = %s"
        val = (name,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
if __name__ == "__main__":
    s = Sql()
    s.insert("John", 25, 25000)
    s.select()