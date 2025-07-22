#datatype in python 
#1].none
#2].numeric
#3].sequence
    #i]str datatype
    #ii]byte datatype
    #it can accept positive number from 0 to 225
    #we cannnot modify any element from the bytes

# a=[2,45,22,45,12,23]#this is list
# print(type(a))
# print(a)
# b=bytes(a)#convetrd a list named 'a' to bytes 'b' 
# print(type(b))
# print(b)
# print(b[0])
# print(b[4])
# b[3]=6 #TypeError: 'bytes' object does not support item assignment

#iii] bytearray datatype
# a=[2,45,66,77,55,66] #this is list
# print(a)
# b=bytearray(a)
# print(type(b))
# print(b)
# print(b[0])
# print(b[3]) #o/p:2
# b[3]=6
# print(b[3]) #o/p:6

#iv]list dataype

# a=[1,10,-15,-45,'Rohan',66,22.69,4]
# print(type(a))
# print(a)
# print(a[0])
# print(a[0:3])
# print(a[1:3])
# print(a[2:3])
# print(a[2:4])
# print(a[2:6])
# a[4]='Rohan Chudasama'
# print(a)
# print(a*2)

# #v] tuple datatype
# a=[1,10,-15,-45,'Rohan',66,22.69,4]
# print(type(a))
# print(a)
# print(a[0])
# print(a[0:3])
# print(a[1:3])
# print(a[1:3])
# print(a*2)
# a[3]='Rohan Chudasama' #TypeError: 'tuple' object does not support item assignment

#vi] range datatype
#it represent a sequence of numbers.
#number in the sequence are not modifiable
# generally used for representing a 'for loop'

# a=range(5)
# for i in a:
#     print(1)

# lst=list(range(8))
# print(type(lst))
# print(lst)



