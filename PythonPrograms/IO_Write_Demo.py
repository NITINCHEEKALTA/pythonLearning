def main():

    writeName()


def writeName():

    name = input("what is your name ? ")
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")


main()