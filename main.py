import mysql.connector as conn


mydb = conn.connect(host="localhost", user="root", passwd="Scomm@2022")
cursor= mydb.cursor()
#cursor.execute("create database kader")
#cursor.execute("show databases")
#s = "create table kader.ineuron3(employe_id int(10), emp_name varchar(80) , emp_mailid varchar(20),emp_salary int(6) , emp_attendence int(3))"
#cursor.execute(s)
#print(cursor.fetchall())

s = ("insert into kader.ineuron3 values('101','shudh','su@gmail.com','30','10')")
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
cursor.execute(s)
mydb.commit()


