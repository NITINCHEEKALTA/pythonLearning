import math

#stringOperations

bigdata_fee = 800
azure_fee = 600
bigdata_enrollments = 20
azure_enrollments = 40

# Arithmetic operations
"""+ - * - / % //"""
"""Precedence of operation is from left to right
And Multiplication; Division takes precedence over addition or subtraction
"""
print("====================" * 3 + "Arithmetic Operations" + "====================" * 3)
total_revenue = bigdata_fee * bigdata_enrollments + azure_fee * azure_enrollments

print(f"total revenue is {total_revenue}")

"""Avg order price"""

Avg_order_price = total_revenue / (bigdata_enrollments + azure_enrollments)

print(f"avg order rice is {Avg_order_price}")

"""To the power of """

print(2 ** 3)

# right side binding so the calculations happen on right side first and them
# move to left
print(2 ** 2 ** 3)

"""Short end writing"""
bigdata_fee += 50

print(f"{bigdata_fee}")

total_sales = 20000.60

print(math.ceil((total_sales)))
print(math.floor((total_sales)))

print("====================" * 3 + "Conditional Operations" + "====================" * 3)
"""Conditional Statements"""
"""Single if condition"""
marks = int(input("Enter marks :"))
if marks >= 35:
    if marks > 80:
        print("A grade")
    else:
        print("You passed but did not get A grade")
else:
    print("fail")
"""============================================================"""
"""elif conditional statement"""
if marks > 80:
    print("A grade")
elif marks >= 35:
    print("You passed but did not secure A grade")
else:
    print("Fail")
"""=================================="""
print("====================" * 3 + "Conditional Operations-2" + "====================" * 3)
age = int(input("Enter Age: "))
crime_record = input("Do you have a crime record: ")
No = "No"
Yes = "Yes"

if age >= 18:
    if crime_record == No:
        print("You are eligible for Voting")
    if crime_record == Yes:
        print("You are not eligible for voting")
else:
    print("Your age is not 18")

name = "Nitin"
print("Nitin" in name)

print("====================" * 3 + "String Operations" + "====================" * 3)

# String can be enclosed in "" ; '': """ """ quotes.
# \ means escape a character in string
# \n means new line
# \t means Tab
fname = input("first name:")
lname = input("last name:")
print(fname + " " + lname)
print(len(fname + " " + lname))

# Two main operations in String Indexing and Slicing
# Indexing helps to get a particular character; Index starts from 0 to get last character
# use [-1]
# Slicing helps to get a part of String.
#  String is immutable. We cannot make changes/modifications to the String
Order_status = "Complete Order"

print(Order_status[3])
print("Last character " + Order_status[-1])
print(Order_status[0:8])
print(Order_status[9:14])

# print everything after the space

index = Order_status.find(" ")

print(index)

# reverse a string
print(Order_status[::-1])

# Find returns the index of first occurrence in string (if not found returns -1)
