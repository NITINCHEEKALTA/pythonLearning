def main():
   
   sumOfArray()

def sumOfArray():

    list = [1,2,3,4,5]
    sum = 0

    for element in list :
        sum += element 
    
    print(sum)

if __name__ == "__main__":
    main()