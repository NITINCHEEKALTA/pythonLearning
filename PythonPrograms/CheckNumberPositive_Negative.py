def main():
    number = input("What is the number ? ")
    checkNumber(number)


def checkNumber(num):
    num = int(float(num))
    if num < 0:
        print("Negative number")
    elif num > 0:
        print("positive number")
    else:
        print("Number is zero")        


main()
