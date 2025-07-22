# bar chart
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.read_excel('newspaper.xlsx')
# print(df)
# y = df['readers']
# x = df['newspaper']

# bar_colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow']

# plt.bar(x, y, label='news_paper_wise_reader', color=bar_colors[:len(x)])
# plt.ylabel = 'no of readers'
# plt.xlabel = 'name of news paper'
# plt.title = 'news paper readers in rajkot'
# plt.legend()
# plt.show()




#pie chart
# import pandas as pd
# import matplotlib.pyplot as plt
# readers_in_percentage=[22,33,12,45,39]
# name_of_newspaper=['Gujarat Samachar',' Sandesh ',' Divya Bhaskar','Gujarat Mitra','Kutchmitra']
# col=['green','yellow','purple','blue','red']
# plt.pie(readers_in_percentage,labels=name_of_newspaper,colors=col,startangle=90)
# plt.title('readers')
# plt.legend()
# plt.show()

#line graph
# import matplotlib.pyplot as plt
# year=['2020','2021','2022','2023','2024',]
# birth=[75,44,99,78,69]
# plt.plot(year,birth)
# plt.title('population growth')
# plt.xlabel('years')
# plt.ylabel('birth in year')
# plt.legend()
# plt.show()

#scatter chart
# import matplotlib.pyplot as plt
# x=[2,9,4,8,3,4,7,]
# y=[8,2,9,4,3,7,5]
# plt.scatter(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('scatter diagram')
# plt.legend()
# plt.show()

#area plot
# import matplotlib.pyplot as plt
# import numpy as np
# x=range(1,8)
# y=[2,7,9,3,1,4,6]
# plt.fill_between(x,y)
# plt.title('area plot')
# plt.legend()
# plt.show()
