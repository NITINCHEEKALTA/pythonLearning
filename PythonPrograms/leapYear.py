import calendar
def main():
    year = input("what is the year ? ")
    if leapYear(year) == True:
        print("it is a leap year")
    else:
        print("Not leap year")


def leapYear(year):
    year = int(year)
    return calendar.isleap(year)


main()