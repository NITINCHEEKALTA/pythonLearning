import sys 

def main():

    number = int(input("what is the number ? : "))
    disariumNumber(number)


def disariumNumber(number):

    num = str(number)
    length = len(num)
    sum = 0

    if number <= 0:
        print("Invalid Number")
        sys.exit()
    
    for i in range(length):
        integerNumber = int(num[i])
        sum += integerNumber ** (i+1)            

    if sum == number:

        print(f"The number {number} is Disarium number") 

    else:
        print("The number is not Disarium number")           
    
if __name__ == "__main__":

    main()