def main():

    number = int(input("Enter the number :"))

    print("the sum of cubes of number is: ", cube_sum_num(number) )


def cube_sum_num(num):
    if num <= 0:
        return 0
    else:
        total = sum([i**3 for i in range(1, num+1)])
        return total
    

if __name__ == "__main__":
    main()