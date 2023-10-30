import datetime
name=print(input("Hi! Please enter your name : "))
age=int(input("Enter your age : "))
year_now=datetime.datetime.now()
print(year_now.year)
print("You will turn 100 years old in "+str(int(100-age)+int(year_now.year)))
