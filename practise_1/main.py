# def stud(name,roll):
#     print('the name of student is :',name)
#     print('the roll number of studnt is :',roll)

# stud(name='abc',roll=1)
# stud(roll=1,name='abc')

# def stud(roll,name='abc'):
#      print('the name of student is :',name)
#      print('the roll number of studnt is :',roll)
# stud(name='hhsa',roll=69)
# stud(roll=69)

# def sum_all(*args):
#     return sum(args)

# print(sum_all(1, 2, 3))  
# print(sum_all(4, 5, 6, 7, 8)) 

# #optional function
# def optional_fun(name=None,age=None):
#     print(f"Name : {name} age :{age}")

# optional_fun('rohan chudasama',12)

# def simple_fun():
#     print("this is called simple function")
# simple_fun()

# simple_limbda=lambda a:a*a
# answer=simple_limbda(10)
# print(answer)

# simple_lim=lambda *val: sum(val)
# print("enter value")
# simple_lim([[a for a in input().split( )]])


# record_len = 15

# with open('restaurant.bin', 'wb') as f:
#     no = int(input('How many items do you want: '))
#     for i in range(no):
#         restaurant = input('Enter food item : ')
#         ln = len(restaurant)
#         restaurant = restaurant + (record_len - ln) * '*'  
#         restaurant = restaurant.encode()  
#         f.write(restaurant)  


# record_len = 15

# with open('restaurant.bin', 'rb') as f:
#     no=int(input('enter the records number to search:'))
#     f.seek(record_len*(no-1))
#     str=f.read(record_len)
#     print(str.decode())

# from zipfile import*
# f=zipfile('demo.zip','w',zip_deflated)
# f.write()
# f.write('abc.txt')
# f.close()



# my_list = ["don", "piyush", "krish", "oom", "dev"]
# search_string = input("Enter a string to search: ")

# if search_string in my_list:
#     print("'" + search_string + "' is available in the list.")
# else:
#     print("'" + search_string + "' is NOT available in the list.")


# def is_palindrom(number):
#     original=str(number)
#     reversed_number=0
#     if original==reversed_number:
#         return True
#     else:
#         return False
# user_input=input("enter the number:")
# if user_input.isdigit():
#     number=int(user_input)
#     if is_palindrom(number):
#         print("is palindrom ")
#     else:
#         print("is not palindrom ")
# else:
#     print("number is invalid")

# def is_palindrom(user):
#     return user==user[::-1]
# print(is_palindrom("welcome"))
# print(is_palindrom("bhagto tha"))



# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# print(mydb)

# mycursor=mydb.cursor()
# mycursor.execute('CREATE DATABASE mypy')

# mycursor=mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
#     print(i)

# import mysql.connector
# mydb=mysql.connector.connect(host='localhost',user='root',password='',database='mypy')
# print(mydb)
# mycursor=mydb.cursor()
# mycursor.execute('CREATE TABLE student(enroll int,name varchar(20))')

# insert='INSERT INTO student(enroll,name)VALUES(%s,%s)'
# records=[(1,'rohan'),(2,'drashti')]
# mycursor=mydb.cursor()
# mycursor.executemany(insert,records)
# mydb.commit()
# mydb.close()
# mycursor.close()


# mycursor=mydb.cursor()
# mycursor.execute('SELECT * FROM student')
# result=mycursor.fetchall()
# for i in result:
#     print(i)

# mycursor=mydb.cursor() 
# update='UPDATE student SET name="drashti" WHERE enroll=2'
# mycursor.execute(update)
# mydb.commit()
# print("print successfully")   


# mycursor=mydb.cursor() 
# delete='DELETE FROM student  WHERE enroll=1'
# mycursor.execute(delete)
# mydb.commit()
# print("delete successfully")  


# user_input = input("Enter some text to store in sample.txt: ")
# with open("sample.txt", "w") as file:
#     file.write(user_input)
# print("Data has been written to sample.txt")



# with open("sample.txt", "r") as file:
#     content = file.read()
# print('this is contain of the file')
# print(content)


# user_input = input("Enter some text to append to sample.txt: ")
# with open("sample.txt", "a") as file:
#     file.write("\n" + user_input)  

# print("Data has been added ")
# with open("sample.txt", "r") as file:
#     content = file.read()

# print("This is the content of the file:")
# print(content)



