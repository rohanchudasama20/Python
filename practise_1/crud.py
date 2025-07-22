#unit 4
#mysql connectivity with python

import mysql.connector
mydb=mysql.connector.connect(
	host='localhost',
	user='root',
	password='',
	database='mypy',
	)
print(mydb)

#creating the database
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')

#display all the database
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
# 	print(i)

#creating a table
# import mysql.connector
# mydb=mysql.connector.connect(
# 	host='localhost',
# 	user='root',
# 	password='',
# 	database='mypy'
# 	)
# print(mydb)
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE stud(ENROL INT,NAME VARCHAR(20))')

#inserting records.
# insert='INSERT INTO stud(ENROL,NAME) VALUES(%s,%s)'
# records=[(1,'abc'),(2,'cde')]
# mycursor=mydb.cursor()
# mycursor.executemany(insert,records)
# mydb.commit()
# mydb.close()
# mycursor.close()

#display all the record from the table
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM stud')
# result=mycursor.fetchall()
# for i in result:
# 	print(i)

#updating the record
# mycursor=mydb.cursor()
# update='UPDATE stud SET name="abc" WHERE ENROL=2'
# mycursor.execute(update)
# mydb.commit()


# print('the record updated successfully')

#deleting the record
mycursor=mydb.cursor()
delete='DELETE FROM stud WHERE ENROL=2'
mycursor.execute(delete)
mydb.commit()
print('the record deleted successfully')
