"""Write a program to swap two variables"""
import random
import calendar
# input two variables
a = int(input("enter first number: "))
b= int(input("enter second number: "))

print(f"first number is : {a}")
print(f"second number is : {b}")

temp = a
a = b
b= temp

print(f"the value of first number after swapping is {a}")
print(f"the value of second number after swapping is {b}")
print("======================================" * 3)

"""Write a program to print a random number"""
print(random.randint(1,10000))
print("======================================" * 3)

"""Convert kilometers to miles"""
kilometer = float(input("the kilometer value is : "))

if kilometer == 0:
    print("Error: Cannot convert zero kilometers to miles")
else:
    miles = kilometer/1.6
    print(f"The miles are: {miles}")

"""Display calendar"""
month = int(input("Enter month: "))
year = int(input("Enter year: "))
cal = calendar.month(year,month)
print(cal)

