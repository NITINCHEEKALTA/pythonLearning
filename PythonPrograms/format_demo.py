import re
def main():

    getname()

def getname():

    name = input("what's your name? ").strip()
    matches = re.search(r"^(.+), *(.+)$",name)

    if matches := matches.group(2) + " "+ matches.group(1) :
        print(f"hello, {name}")

main()