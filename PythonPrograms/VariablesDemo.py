"""first course
fee"""
#intiating the variables
course_fee = 800
course_name = "Python class"
is_Starting_Soon = True
course_rating = 4.99
My_income = None
print("===========================")
"""print the values of variables"""
print(course_fee)
print(course_name)
print(is_Starting_Soon)
print(course_rating)
print(My_income)

print("===========================")
"""Print the type of variables"""
print(type(course_name))
print(type(course_fee))
print(type(is_Starting_Soon))
print(type(course_rating))
print(type(My_income))
print("===========================")
"""Type errors"""
# Run time error. Here we're trying to concatenate a String to int
# print(course_name + 1)

"""Type Casting 
manual type casting 
"""
# Add new variables

course_fee = "800"
course_fee = (int(course_fee) + int(course_fee) * .1)
print(course_fee)
print("==========================="*3)

"""Sting concatenation
    and formatting 
"""
first_name = "Nitin"
last_name = "Cheekatla"
# print("My first name is "+first_name+" and my last name is "+last_name)
print(f"My first name is {first_name} and my last name is {last_name}")

"""How take input 
   from user
"""
print("==========================="*3)
salary = input("what is your salary:")
Hike = input("what is the hike percentage: ")

new_salary = int(salary) + int(salary) * int(Hike)/100
print(f" the new salary after hike is {new_salary}")