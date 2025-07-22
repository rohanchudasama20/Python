# #creating file
# f=open('abc.txt','w')
# str=input('enter the text:')
# f.write(str)
# f.close()

# #reading the file
# f=open('abc.txt','r')
# a=f.read()
# print(a)
# f.close()

# #opening the file
# with open('abc.txt', 'r') as file:
#     content = file.read()
#     print(content)


#appending the file
# f=open('abc.txt','a+')
# str=input('enter the text:')
# f.write(str)
# f.close()

# import os,sys
# file_name=input('enter the name of file you want to open:')
# if os.path.isfile(file_name):
#     f=open('abc.txt','r')
# else:
#     print(file_name+'file is not avalabile')
#     sys.exit()
# str=f.read()
# print(str)
# f.close()

# import os
# import sys

# file_name = input('Enter the file name to open: ')

# if os.path.isfile(file_name):
#     f = open(file_name, 'r')
# else:
#     print(file_name + ' file is not available.')
#     sys.exit()

# line_count = word_count = char_count = 0

# for line in f:
#     words = line.split()
#     line_count += 1
#     word_count += len(words)
#     char_count += len(line)

# # Print results
# print('Number of lines in the file:', line_count)
# print('Number of words in the file:', word_count)
# print('Number of characters in the file:', char_count)

# f.close()


# f1 = open('image.png', 'rb')   
# f2 = open('image_1.png', 'wb')    

# abc = f1.read()               
# f2.write(abc)                 

# f1.close()
# f2.close()


# from zipfile import*
# f=ZipFile('demo1.zip','w',ZIP_STORED)
# f.write('image.png')
# f.write('sample.txt')
# f.close()


# from zipfile import*
# z=ZipFile('demo1.zip','r')
# z.extractall('D:/phython')


  

# store the binary file to store in the bin name of restrorent
# record_len = 15  # fixed size of each record

# with open('restaurant.bin', 'wb') as f:
#     no = int(input('How many items you want: '))

#     for i in range(no):
#         restaurant = input('Enter the name of food: ')
#         restaurant = restaurant.ljust(record_len, '*')  
#         f.write(restaurant.encode())  
