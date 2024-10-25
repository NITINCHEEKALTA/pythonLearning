def main():

    number = int(input("Enter the number ?"))

    if number < 0:
        print("positive Numbers")
    else:
        print(factorial(number))

def factorial(number):

    if number == 1:
        return number

    else:
        return number * factorial(number-1)
    

if __name__ == "__main__":
    main()
    