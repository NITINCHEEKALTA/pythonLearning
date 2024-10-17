def main():
    readcsv()

def readcsv():

    with open("names.csv") as file:
        for line in file:
            row = line.rstrip().split(",")
            print(f"{row[0]} is in{row[1]}")


main()