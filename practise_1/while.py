# #make a program to accept number from user untill user prees zero. make the sum of all numbers.
# sum=0
# num=int(input('enter the number:'))
# while num!=0:
#     sum=sum+num
#     num=int(input('enter the num:'))
#     print('the sum of all the entered number is:',num)

# #to display the table of the number 
# num=2
# counter=1
# print('the table of :',num)
# while counter<=10:
#     answer=num*counter
#     print(num,'x',counter,'=',answer)
#     counter=counter+1

# #display even numbers beetween 1 to 10
# num=2
# while num>=1 and num<=10:
#     print(num)
#     num=num+2

# display odd numbers between 1 to 10
# num=1
# while num>=1 and num<=10:
#     print(num)
#     num=num+2

#take choice from the user whether to print even numbers or odd numbers
# num=int(input('enter the 1 to get odd numbers or 2  to get even numbers between 1-10: '))
# if num==1:
#     print('program will print all odd numbers')
#     while num>=1 and num<=10:
#         print(num)
#         num=num+2

# else:
#     print('program will print all even numbers')
#     while num>=1 and num<=10:
#         print(num)
#         num=num+2    

#display number and its square (1-10)
num=1
while(num<=10):
    print(num,'\t',num**2)
    num=num+1

a=[3,4,8,6,8,13]
b=0
while(b<len(a)):
    if a[b]%1==0:
        print(a[b])
        b=b+1

val='Rohan'
b=0
while(b<len(val)):
    print(val[b])
    b=b+1


# from numpy import* 
# a=array([[1,2,3,4],[5,6,7,8]])
# # print(a)
# #Slicing
# print(a[0])
# print(a[1])
# print(a[:,0])
# print(a[0:1,0:1])
# print(a[0,:]) 
# print(a[:,0]) 
# a=array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[2:3,2:3])


#Using where() function
# Format:where(condition,expression-1,expression-2)
# from numpy import*
# # a1=array([1,12,3,4,15])
# # b1=array([10,2,3,41,5])
# # c1=where(a1!=b1,a1,b1)
# # print(c1)
# # print(type(c1))