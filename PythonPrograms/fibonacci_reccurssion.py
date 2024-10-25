def main():

    number = int(input("Enter number "))
    if number <= 0:
        print("Enter positive number")
    else:
        for i in range(number):
            print(fibonacci(i))


def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

if __name__ == "__main__":
    main()