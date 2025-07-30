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


# class Car:
#     def __init__(self, name, max_speed):
#         # Encapsulated attributes (private)
#         self.__name = name
#         self.__max_speed = max_speed
#         self.__current_speed = 0

#     # Public method to set the car's speed (setter)
#     def set_speed(self, speed):
#         if 0 <= speed <= self.__max_speed:
#             self.__current_speed = speed
#             print(f"The {self.__name}'s speed is now {self.__current_speed} km/h.")
#         else:
#             print(f"Error: Speed must be between 0 and {self.__max_speed} km/h.")

#     # Public method to get the current speed (getter)
#     def get_speed(self):
#         return self.__current_speed
        
#     # Public method to get the car's name (getter)
#     def get_name(self):
#         return self.__name

# # --- Main part of the script ---
# if __name__ == "__main__":
#     # Create an instance of the Car class
#     my_car = Car("Sedan", 180)

#     print(f"Car Name: {my_car.get_name()}")
    
#     # Use the public method to change the speed
#     my_car.set_speed(90)  # This will work
#     my_car.set_speed(200) # This will show an error

#     # Now, let's try to access the private attribute directly
#     try:
#         print(my_car.__current_speed)
#     except AttributeError as e:
#         print(f"\nDirect access failed: {e}")
#         print("This shows encapsulation is working!")

#     # The correct way to get the speed is using the getter method
#     print(f"Current speed fetched via getter: {my_car.get_speed()} km/h")

# class Backpack:
#     def __init__(self):
#         # This list of items is "private" and safe inside the backpack.
#         self.__items = []

#     # This is a "public" tool (method) to add an item.
#     def add_item(self, item):
#         print(f"Adding '{item}' to the backpack.")
#         self.__items.append(item)

#     # This is a "public" tool to see what's inside.
#     def show_items(self):
#         if not self.__items:
#             print("The backpack is empty.")
#         else:
#             print("The backpack contains:")
#             for item in self.__items:
#                 print(f"- {item}")

# # --- Let's use the backpack ---
# if __name__ == "__main__":
#     my_backpack = Backpack()

#     # We use the public methods to interact with the backpack.
#     my_backpack.add_item("Math Book")
#     my_backpack.add_item("Lunch Box")
#     my_backpack.add_item("Pencil")
    
#     print("-" * 20) # A separator line

#     # See what's inside using the provided method.
#     my_backpack.show_items()

    # If you try to access the items directly, you'll get an error.
    # This line would fail: print(my_backpack.__items)
    # This protects the data from being changed by accident!

# import pandas as pd
# import matplotlib.pyplot as plt
# x=range(1,8)
# y=[2,7,6,9,4,5,1]
# plt.fill_between(x,y)
# plt.title('area plot')
# plt.show()

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    current = head
    
    while current:
        next_temp = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev one step forward
        current = next_temp       # Move current one step forward
        
    return prev # `prev` is now the new head

# --- Example ---
ll = create_linked_list([1, 2,12s, 6, 5])
print("Original:")
print_linked_list(ll)

reversed_ll = reverse_list(ll)
print("\nReversed:")
print_linked_list(reversed_ll)