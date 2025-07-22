# a={12,1,5,78,55}
# print(a)

# b=set('Rohan')
# print(type(b))
# print(b)

# a={45,1,2,3,77}
# a.remove(77)
# print(a)

#dictonary
# a={"name":"Rohan","city":"Rajkot","age":21}
# print(a["city"])
# del a["city"]
# print(a.keys())
# print(a.values())

num = 1100

if 1 <= num <= 999:
    print(num * 5 / 100)
    print(f"{num} - you are a little bit away")

elif 1000 <= num <= 1900:
    print(num * 5 / 100)
    print(f"{num} - you will get 10% discount")

elif 1901 <= num <= 2200:
    print(num * 5 / 100)
    print(f"{num} - you will get 15% discount")

else:
    print("Hurry! You availed the maximum discount")
   
