# import pandas as pd
# # rc=pd.read_csv('store.csv')#working with csv file to show the data
# # print(rc)

# rc=pd.read_excel('store.xlsx')#working with other extension
# # print(rc[rc.manufa_city=='Seattle'])#it will sow the particular city
# # print(rc[rc.price>110])# it will show the value is above or the price it will shoe the all data
# print(rc[['name']][rc.price>150])

# stud={'roll':[101,102],'name':['rohan','drashti'],'city':['rajkot','veraval']}#convert in to dataframe
# rc=pd.DataFrame(stud)
# print(rc)


# stud=[(101,'rohan','rajkot'),
#        (102,'drashti','veraval')]
# rc=pd.DataFrame(stud,columns=['roll','name','city'])
# print(rc[['name','city']])#print particular fields
# print(rc['roll'].min())#it will print the max & min value in the dataframe 

#bar graph

# import pandas as pd
# import matplotlib.pyplot as plt
# rc=pd.read_excel('newspaper.xlsx')
# print(rc)
# y=rc['readers']
# x=rc['news paper']
# plt.bar(x,y,label='news_paper_wise_readrs',color='yellow')
# plt.ylabel='no of readers'
# plt.xlabel='name of news paper'
# plt.title='news paper readrs in rajkot'
# plt.legend()
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
# data = pd.read_excel('newspaper.xlsx')#bar chart
# plt.bar(data['newspaper'], data['readers'], color='yellow')
# plt.xlabel('Newspaper')
# plt.ylabel('Readers')
# plt.title('Readers of Gujarati Newspapers')
# # plt.xticks(rotation=45)
# plt.show()


# readers_in_percentage= [20, 15, 25, 10, 8, 7, 9, 6]#pie chart
# name_of_news_paper=['Gujarat Samachar','Sandesh',' Divya Bhaskar',' Gujarat Mitra','Kutchmitra','Jai Hind','Akila Daily',' Nobat']
# col=['red','blue','green','orange','purple','yellow','cyan','magenta']
# plt.pie(readers_in_percentage,labels=name_of_news_paper,colors=col,startangle=90)
# plt.title('readrs')
# plt.legend()
# plt.show()


# year=['2020','2021','2022','2023','2024'] #line graph
# birth=[75,87,56,45,98]
# plt.plot(year,birth)
# plt.title('population growth')
# plt.xlabel('years')
# plt.ylabel('birth bin the year')
# plt.show()


# x=[2,9,7,6,3,4,8,10]  #scatter graph
# y=[8,2,4,9,6,3,2,5]
# plt.scatter(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('scatter diagram')
# plt.show()


x=range(1,8)
y=[2,7,6,9,4,5,1]
plt.fill_between(x,y)
plt.title('area plot')
plt.show()
