import math
def main():

    number = float(input("Enter the number ? "))

    if number <= 0:
        print("Enter numbers greater than zero")

    else:
        logOfNum(number)




def logOfNum(num):

    result = math.log(num)

    print(f"the logarithm of {num} is : {result}")


if __name__ == "__main__":
    main()