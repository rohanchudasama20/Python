#unit 4
#mysql connectivity


# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='crud'
# )
# print(mydb)

# #creating the database
# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE crud')


#dispaly all the databases
# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')


#CREATING THE TABLE
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE stud(ENROL INT,NAME VARCHAR(20))')


#INSERT THE RECORDS
# insert = 'INSERT INTO stud (ENROL, NAME) VALUES (%s, %s)'
# records = [(1, 'rohan'), (2, 'dev')]

# mycursor = mydb.cursor()
# mycursor.executemany(insert, records)
# mydb.commit()

# mycursor.close()
# mydb.close()

#display all the table
# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM stud')
# result=mycursor.fetchall()
# for i in result:
#     print(i)


# updateing the data 
# mycursor=mydb.cursor()
# update='UPDATE stud SET NAME="drashti chudasama" WHERE ENROL=2'
# mycursor.execute(update)
# mydb.commit()
# print('the record update succesfully')


#delete the records

# mycursor=mydb.cursor()
# delete='DELETE FROM stud WHERE ENROL=1'
# mycursor.execute(delete)
# mydb.commit()
# print('delete the records')

# --------------------------------------------------------------------------------------------------------------------------------------


#connecton with sqlite

#create the database
# import sqlite3
# con=sqlite3.connect('data.db') 

# #create the table
# con.execute('CREATE TABLE real (ENR INTEGER,NAME VARCHAR)')

#inserting the record
# con.execute('''
# 	INSERT INTO stud VALUES
# 	(101,'ABC'),
# 	(102,'CDE'),
# 	(103,'DEF')
# ''')
# con.commit()

#display all the record
# cursor=con.execute('SELECT * FROM stud')
# for i in cursor:
# 	print(i)

#display specific record
# Display student whose ENR is 101.
# cursor=con.execute('SELECT * FROM stud WHERE ENR=101')
# for i in cursor:
# 	print(i)

#update the record
#update the name of the student whode enr is 102

# Update='''UPDATE stud SET NAME='XYZ' WHERE ENR=102'''
# con.execute(Update)
# con.commit()
# cursor=con.execute('SELECT * FROM stud')
# for i in cursor:
# 	print(i)

#update enr of the student whose name is xyz
# Update='''UPDATE stud SET ENR=100 WHERE NAME="XYZ" '''
# con.execute(Update)
# con.commit()
# cursor=con.execute('SELECT * FROM stud')
# for i in cursor:
# 	print(i)


#DELETE SPECIFIC RECORD
# delete='''DELETE FROM stud WHERE ENR=100'''
# con.execute(delete)
# con.commit()
# cursor=con.execute('SELECT * FROM stud')
# for i in cursor:
# 	print(i)

#deleting all records

# delete='''DELETE FROM stud'''
# con.execute(delete)
# con.commit()
# cursor=con.execute('SELECT * FROM stud')
# for i in cursor:
# 	print(i)

import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
df = pd.read_excel('store.xlsx')

# Extract columns as pandas Series (no tolist)
admissions = df['Admissions']
programs = df['Program']

# Define colors
colors = ['green', 'yellow', 'purple', 'blue', 'red']

# Plot pie chart
plt.pie(admissions, labels=programs, colors=colors, startangle=90)

plt.title('Admissions of Five Programs')
plt.legend()
plt.show()






