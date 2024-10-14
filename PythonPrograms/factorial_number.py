def main():
    number = int(input("Enter the number : "))
    factorial(number)


def factorial(num):
    factorial = 1;
    if num == 0:
        print("The factorial of 0 is 1")
    elif num < 0:
        print("There is no factorial for negative numbers")
    else:
        for i in range(1,num+1):
            factorial = factorial * i;
        print(f"The factorial of {num} is {factorial}")

main()