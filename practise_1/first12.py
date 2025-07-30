# #Inside the formatted string
# # n1,n2,n3=2,3,4
# # print('The 1st number is {0}, the 2nd number is {1}, and the last number is {2}'.format(n2,n3,n1))
# # name,salary='ABC',10000
# # print('Hello {0}, your salary is {1}'.format(salary,name))
# #Input statements
# # a=input()
# # print(a)

# # name=input('Please enter your name: ')
# # print(name)

# # date=int(input('Enter todays date: '))
# # print(date)

# # price=float(input('Enter the price: '))
# # print(price)

# #Accepting the 1st character from the string
# # a=input(('Enter the string: '))[2]
# # print(a)

# #Finding sum and product of two integer values accepted from the users
# # a=int(input('Enter the 1st value: '))
# # print(a)
# # b=int(input('Enter the 1st value: '))
# # print(b)
# # print('The sum of {0} and {1} is {2}'.format(a,b,a+b))
# # print('The sum of {0} and {1} is {2}'.format(a,b,a*b))
# # print('The sum of {0} and {1} is {2} and the product is {3}'.format(a,b,a+b,a*b))

# #Use of split() method
# # n1,n2,n3=[int(no) for no in input('Enter three values by giving space in between: ').split(',')]
# # print('The sum of three values: ',n1+n2+n3)

# Use of eval() using eval
a,b=15,16
ans=eval('a+b')
print(ans)

# # a,b=7,16
# # ans=eval(input('Enter an expression'))
# # print('The result of your expression is: %d' %ans)

# # a=int(input('Enter the 1st value: '))
# # print(a)
# # b=int(input('Enter the 1st value: '))
# # print(b)
# # c=int(input('Enter the 1st value: '))
# # print(c)
# # print('The sum of {0}, {1} and {2} is {3}'.format(a,b,a+b+c))
# # # print('The sum of {0} and {1} is {2}'.format(a,b,a*b))
# # -# print('The sum of {0} and {1} is {2} and the product is {3}'.format(a,b,a+b,a*b))

# # #Using a while loop, make the program that accepts numeric values from the users until user press 0. 
# # Give the sum of all the inserted values.
# # sum=0
# # num=int(input('Enter the number: '))
# # while num !=0:
# # 	sum=sum+num
# # 	num=int(input('Enter the num: '))
# # print('The sum of all entered number is: ',sum)

# # #Using while loop display the table of 2
# # n=2
# # counter=1
# # print('The table of n is as follow: ')
# # while counter<=10:
# # 	ans=n*counter
# # 	print(n,'x',counter,'=',ans)
# # 	counter=counter+1

# # #Display even numbers between 1-10
# # a=2
# # while a>=1 and a<=10:
# # 	print(a)
# # 	a=a+2

# # #Display odd numbers between 1-10
# # a=1
# # while a>=1 and a<=10:
# # 	print(a)
# # 	a=a+2

# # #Ask user whether they want odd numbers or even numbers
# # n=int(input('Enter your choice: 1 for odd numbers and 2 for even numbers: '))
# # if n==1:
# # 	print('All the odd numbers between 1-10 are as follow:')
# # 	while n>=1 and n<=10:
# # 		print(n)
# # 		n=n+2
# # elif n==2:
# # 	print('All the even numbers between 1-10 are as follow:')
# # 	while n>=1 and n<=10:
# # 		print(n)
# # 		n=n+2

# # #Display numbers and their associated square.
# # n=1
# # while(n<=10):
# # 	print(n,'\t', n**2)
# # 	n=n+1

# # #To find only even numbers from the list
# # lst=[4,9,6,7,7,8,1,2]
# # a=0
# # while(a<len(lst)):
# # 	if lst[a]%2==0:
# # 		print(lst[a])
# # 	a=a+1

# # #len()
# # a='Welcome to the lab'
# # print(len(a))

# # a='Rajkot'
# # b=0
# # while(b<len(a)):
# # 	print(a[b])
# # 	b=b+1

# #Make a program to accept numbers from user until user press zero. Make the sum of all the numbers.
# # sum=0
# # num=int(input('Enter the number: '))
# # while num!=0:
# # 	sum=sum+num
# # 	num=int(input('Enter the num: '))
# # print('The sum of all the entered numbers is: ',sum)

# # #To display the table of the number
# # num=2
# # counter=1
# # print('The table of :',num)
# # while counter<=10:
# # 	answer=num*counter
# # 	print(num,'x',counter,'=',answer)
# # 	counter=counter+1 

# # #Display even numbers between 1 and 10
# # num=2  	
# # while num>=1 and num<=10:
# # 	print(num)
# # 	num=num+2
# # #Display odd numbers between 1 and 10
# # num=1	
# # while num>=1 and num<=10:
# # 	print(num)
# # 	num=num+2

# # #Take choice from the user whethere to print even numbers or odd numbers
# # num=int(input('Enter the 1 to get odd numbers or 2 to get even numbers between 1-10:'))
# # if num==1:
# # 	print('Program will print all odd numbers')
# # 	while num>=1 and num<=10:
# # 		print(num)
# # 		num=num+2
# # else:
# # 	print('Program will print all even numbers')
# # 	while num>=1 and num<=10:
# # 		print(num)
# # 		num=num+2

# # #Display number and its square (1-10)
# # num=1
# # while(num<=10):
# # 	print(num,'\t',num**2)
# # 	num=num+1

# # #Display odd numbers from the given list
# # a=[3,4,8,6,7,2,1,9]
# # b=0
# # while(b<len(a)):
# # 	if a[b]%1==0:
# # 		print(a[b])
# # 	b=b+1

# # #len()
# # val='Welcome to the lab'
# # print(len(val))

# # #Use of len()
# # val='Atmiya'
# # b=0
# # while(b<len(val)):
# # 	print(val[b])
# # 	b=b+1

# #for loop
# # -for loop can work with sequence like (string, tuple, list, range etc)
# #Syntax:
# # for var in sequence:
# # 	statements
# #Printing all the elemetns of the string
# # a='Rajkot'
# # for char in a:
# # 	print(char)

# #Same program as above with indexing
# # a='Rajkot'
# # b=len(a)
# # print(b)
# # for t in range(b):
# # 	print(a[t])

# #Program to display 1-10
# # for t in range(11):
# # 	print(t) #it will print 0-10, index starts with 0, and n-1

# #Program to display 1-10
# # for t in range(1,11):
# # 	print(t)

# # range(start, end, jump)
# #Program to display even numbers between 1-10
# # for t in range(2,11,2):
# # 	print(t)
# #Program to display odd numbers between 1-10
# # for t in range(1,11,2):
# # 	print(t)

# #Display numbers in reverse order from 10-1
# # for t in range(10,0,-1):
# # 	print(t)

# #Give the sum of all the elements of the list.

# # sum=0
# # lst=[4,5,9,3,7,12]
# # for t in lst:
# # 	# print(t)
# # 	sum=sum+t
# # print('The sum of all the elements of the list is: ',sum)

# #Using else with for loop
# # lst=[4,5,9,3,7,12]
# # for t in lst:
# # 	print(t)
# # else: 
# # 	print('All the elements are printed here')

# #Indexing and Slicing on Arrays
# #Slicing
# #-Used to retrieve range of elements.
# #The format is : array_name[start:stop:stride]
# #Out of the format we can eliminate one or two from the parameters.
# # from array import*
# # a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
# # b=a[0:13]
# # b=a[0:]
# # b=a[:13]
# # b=a[0:5]
# # b=a[6:9]
# # b=a[-13:]
# # b=a[-13:-7]
# # b=a[0:13:2]
# # print(b)

# #Slicing using for loop
# # from array import*
# # a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
# # for i in a[0:16]:
# # 	print(i, end=' ')

# #Processing the arrays / Array Methods
# # from array import*
# # a=array('i',[2,3,8,6,7,9])
# # print(a)

# #Appending the element into the array
# # a.append(10)
# # print(a)
# #Inserting the element at the desired position
# # a.insert(0,0)
# # a.insert(0,11)
# # print(a)
# #Removing the element
# # a.remove(6)
# # print(a)
# #Removing the last element
# # b=a.pop()
# # print('Poped element was',b)
# # print(a)
# # #Finding the position of an element 
# # b=a.index(7)
# # print('The element 7 is found at the position: ',b)
# # #Converting array to list
# # lst=a.tolist()
# # print('Elements of list are: ', lst)
# # print('Elements of array are: ', a)

# #Take marks of students in the array, give the total of scored marks and percentage.
# # from array import*
# # a=input('Enter your marks: ').split(',')
# # marks=[int(number)for number in a]
# # total=0
# # for i in marks:
# # 	# print(i)
# # 	total=total+i
# # print('The total of all marks is: ',total)
# # l=len(marks)
# # percentage=total/l
# # print('The percentage of the student is: ',percentage)

# #Array
# #Declaring array in 3 differeent ways
# #The 1st way to declare an array
# import array
# a=array.array('i',[5,6,7,9,3,4])
# print(a)

# # #The 2nd way to declare an array
# import array as ar
# a=ar.array('i',[5,6,7,9,3,4])
# print(a)

# # #The 3rd way to declare an array
# from array import*
# a=array('i',[5,6,7,9,3,4])
# print(a)

# # from array import*
# a=array('u',['a','b','c','d','d','f'])
# print(a)

# #Indexing and Slicing of an array
# #Indexing
# from array import*
# a=array('u',['a','b','c','d','d','f'])
# print(a)
# for c in a:
# 	print(c,end=',')

# #Indexing using for loop
# from array import*
# a=array('i',[5,6,7,9,3,4])
# print(a)
# n=len(a)
# for i in range(n):
# 	print(a[i],end=',')

# #Indexing using while loop
# from array import*
# a=array('i',[5,6,7,9,3,4])
# print(a)
# n=len(a)
# i=0
# while i<n:
# 	print(a[i],end=',')
# 	i=i+1

# #Slicing in array
# #format:
# 	#array_name=[start:stop:stride]
# from array import*
# a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
# b=a[0:13]
# print(b)
# b=a[0:]
# print(b)
# b=a[:13]
# print(b)
# b=a[-13:]
# print(b)
# b=a[:6]
# print(b)
# b=a[2:7]
# print(b)
# b=a[-13:-7]
# print(b)
# b=a[0:13:2]
# print(b)
# from array import*
# a=array('u',['r','a','j','k','o','t','g','u','j','a','r','a','t'])
# for i in a[0:13]:
# 	print(i,end=',')

# #Processing the Arrays/Array Methods
# from array import*
# a=array('i',[5,6,7,9,3,4])
# print(a)
# #Appending the value to the array
# a.append(2)
# print(a)
# #Inserting the value at the specific position in the array
# a.insert(0,10)
# a.insert(1,1)
# print(a)
# #Remove the element
# a.remove(6)
# print(a)
# #Pop the element
# b=a.pop()
# print(a)
# print(b)
# #Finding position/index of an element
# b=a.index(7)
# print(b)
# #Converting an array into list
# lst=a.tolist()
# print(lst)
# print(type(lst))
# print(a)
# print(type(a))

# #Taking price of each product and giving the total of the purchase.
# from array import*
# a=input('Enter amount of product purchased space seprated: ').split(' ')
# amount=[int(n)for n in a]
# total=0
# for i in amount:
# 	# print(i)
# 	total=total+i
# print('The total payable amount is: ',total)
# l=len(amount)
# average_cost=total/l
# print('The average cost is: ',average_cost)
#Comparing arrays
# from numpy import *
# a1=array([1,2,13,4,5])
# a2=array([10,2,3,4,15])
# print('The comparison: ', a1==a2)
# print('The comparison: ', a1<=a2)
# print('The comparison: ', a1>=a2)
# print('The comparison: ', a1!=a2)


#Using where()
#format: where(comparison_condition, expression-1,expression-2)
# from numpy import *
# a1=array([1,2,13,4,5])
# a2=array([10,2,3,4,15])
# a3=where(a2==a1,a2,a1)
# print(a1)
# print(a2)
# print(a3)

#Using nonzero()
#It returns the index of all non-zero elements
# from numpy import *
# a1=array([1,2,0,4,5])
# a2=nonzero(a1)
# print(a1)
# print(a2)

#view()
# from numpy import *
# a1=array([1,2,0,4,5])
# a2=a1.view()

# print(a1)
# print(a2)
# a1[3]=40
# print(a1)
# print(a2)

#copy()
# from numpy import *
# a1=array([1,2,0,4,5])
# a2=a1.copy()
# print(a1)
# print(a2)
# a1[3]=40
# print(a1)
# print(a2)

#Slicing and indexing in numpy array
#slicing: array_name(start:stop:stepsize)
# from numpy import *
# a1=array([1,2,0,4,5])
# print(a1[0:5])
# print(a1[:])
# print(a1[::])
# print(a1[1::2])

#indexing
# from numpy import *
# a1=array([1,2,0,4,5])
# i=0
# while(i<len(a1-1)):
# 	print(a1[i])
# 	i=i+1

#Attributes of an array
#1. ndim attribute (returns 1 if the array is single dimension, returns 2 if the array is multi dimension)
# from numpy import *
# a1=array([1,2,0,4,5])
# print(a1.ndim)
# from numpy import *
# a1=array([[1,2,0,4,5],[2,4,9,7,8],[2,4,9,7,8]])
# print(a1.ndim)

#2.shape attribute (returns no. of elements in case of single dimension, 
# and in multi dim it returns dimensions of the array)
# from numpy import *
# a1=array([1,2,0,4,5])
# print(a1.shape)
# a2=array([[1,2,0,4,5],[2,4,9,7,8],[2,4,9,7,8]])
# print(a2.shape)

#3.size attribute (returns number of elements)
# from numpy import *
# a1=array([1,2,0,4,5])
# print(a1.size)
# a2=array([[1,2,0,4,5],[2,4,9,7,8],[2,4,9,7,8]])
# print(a2.size)

#4.dtype attribute (returns the datatype of an array)
# from numpy import *
# a1=array([1,2,0,4,5])
# print(a1.dtype)

#reshape() method
#format: array_name.reshape(n,r,c)
# from numpy import *
# a1=array([1,2,0,4,5,7,6,4,9])
# a2=a1.reshape(3,3)
# print(a1)
# print(a2)

# from numpy import *
# a1=array([1,2,0,4,5,7,6,4,9,10,11,12])
# a2=a1.reshape(2,3,2)
# print(a1)
# print(a2)

#flatten() method
# from numpy import *
# a1=array([[1,2,0,4,5,7],[6,4,9,10,11,12]])
# print(a1)
# a2=a1.flatten()
# print(a2)

#Multidimensionl arrays
from numpy import*
a=array([[1,2,3,4],[5,6,7,8]])
print(a)
#Slicing
print(a[0])
print(a[1])
print(a[:,0])
print(a[0:1,0:1])
print(a[0,:]) 
print(a[:,0]) 
a=array([[1,2,3],[4,5,6],[7,8,9]])
print(a[2:3,2:3])

#Using where() function
# Format:where(condition,expression-1,expression-2)
from numpy import*
a1=array([1,12,3,4,15])
b1=array([10,2,3,41,5])
c1=where(a1!=b1,a1,b1)
print(c1)
print(type(c1))

#Return index of non-zero elements using nonzer()
from numpy import*
a1=array([1,12,3,4,15])
a2=nonzero(a1)
print(a2)
b1=array([1,12,3,0,15])
b2=nonzero(b1)
print(b2)

#The view()
from numpy import*
a1=array([1,12,3,4,15])
a2=a1.view()
# print(a1)
# print(a2)
a2[3]=40
print(a1)
print(a2)
a1[2]=30
print(a1)
print(a2)

#The copy()
from numpy import*
a1=array([1,12,3,4,15])
a2=a1.copy()
print(a1)
print(a2)
a2[3]=40
print(a1)
print(a2)
a1[2]=30
print(a1)
print(a2)

#Slicing and Indexing in numpyArrays.
#Slicing: array_name[start:stop:stepsize]
from numpy import*
a1=array([1,12,3,4,15])
print(a1)
print(a1[0:5:])
print(a1[::])
print(a1[:])
print(a1[2:4])
print(a1[::2])
#Indexing
from numpy import*
a1=array([1,12,3,4,15])
i=0
while(i<len(a1-1)):
	print(a1[i],end=',')
	i=i+1

#Attributes of an Array.
#i). ndim attribute (it returns 1 if the array is single dimension, 
# and returns 2 if the array is multi dimensional)
from numpy import *
a1=array([1,2,3,4,5])
print(a1.ndim)
a2=array([[1,2,3],[4,5,6],[7,8,9]])
print(a2.ndim)

#ii). shape attribute (it returns no. of elements in the case single dimensional array,
#in case of multi-dimensional array it returns dimensions.)
from numpy import *
a1=array([1,2,3,4,5])
print(a1.shape)
a2=array([[1,2,3],[4,5,6],[7,8,9]])
print(a2.shape)

#iii). size attribute (returns no. of elements)
from numpy import *
a1=array([1,2,3,4,5])
print(a1.size)
a2=array([[1,2,3],[4,5,6],[7,8,9]])
print(a2.size)

#iv). dtype (returns the datatype of the array)
from numpy import *
a1=array([1,2,3,4,5])
print(a1.dtype)

#reshape() method
#Format: name_of_new_array=arrayname.reshape(no.of arrays,r,c))
from numpy import *
a1=array([1,2,3,4,5,6,7,8,9])
print(a1.shape)
# print(a1)
a2=a1.reshape(3,3)
print(a2.shape)
print(a2)

a1=array([1,2,3,4,5,6,7,8,9,10,11,12])
a3=a1.reshape(3,2,2)
print(a3)

#Flatten
from numpy import *
a1=array([[1,2,3],[4,5,6],[7,8,9]])
print(a1)
a2=a1.flatten()
print(a2)
