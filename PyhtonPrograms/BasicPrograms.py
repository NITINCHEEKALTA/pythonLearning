"""Write a pyhton program to do arithmetical operations addition and division"""
"Addition"

num1 = float(input("Enter first number for addition: "))
num2 = float(input("Enter Second number for addition: "))
num3 = float(num1 + num2)
print(f"the sum of {num1} and {num2} = {num3}")

"Division"
num4 = float(input("Enter first number for division: "))
num5 = float(input("Enter Second number for division: "))

if num5 == 0:
    print("Error : division by zero is not allowed")
else:
    num6 = float(num4 / num5)
    print(f"the result of division of {num4} by {num5} is {num6}")

"""Write a program to find the area of triangle"""
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base of the triangle: "))
area = float(0.5 * height * base)
print(f"area of triangle is {area}")