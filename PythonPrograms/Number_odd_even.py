def main():
    number = input("what is the number ? ")
    oddOrEven(number)


def oddOrEven(num):
    num = int(float(num))
    if num % 2 == 0:
        print("Even number")
    else :
        print("Odd number")
   

main()