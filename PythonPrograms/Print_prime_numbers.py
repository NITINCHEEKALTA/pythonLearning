def main():

    printPrime()

def printPrime():
    lower = 1
    upper = 10
    print("Prime numbers between", lower, "and", upper," :")
    for num in range(lower, upper):
        if num > 1:
            for i in range(2,num):
                if(num % i) == 0:
                    break

            else:
                print(num)    


main()