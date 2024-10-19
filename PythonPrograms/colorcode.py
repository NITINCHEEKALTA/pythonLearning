import re

def main():



def colorCodeMatch():

    code = input("Hexadecimal color code: ")

    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern, code)

    if match:
        print(f"valid. matched with {match.group()}")
    else:
        print("Invalid.")    