#connecton with sqlite

#create the database
import sqlite3
con=sqlite3.connect('data.db') 

#create the table
# con.execute('CREATE TABLE stud (ENR INTEGER,NAME VARCHAR)')

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

delete='''DELETE FROM stud'''
con.execute(delete)
con.commit()
cursor=con.execute('SELECT * FROM stud')
for i in cursor:
	print(i)