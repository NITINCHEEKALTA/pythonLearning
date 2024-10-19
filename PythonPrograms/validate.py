import re

def main():

    getEmail()




def getEmail():

    email = input("what's your email ? ").strip()

    if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email):
        print("Valid")

    else:
        print("Invalid") 


main()


# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email)
# . (dot): This matches any single character except a newline (\n).
# + (plus): This matches one or more occurrences of the preceding pattern
# ^ matches the start of the string 
# $ matches the end of the string 
# or just before the newline at the end of 
# the string 
# [] allow the set of characters
# [^] complementing the set meaning cannot match any of these characters
# \d decimal digit
# \D not a decimal digit
#\s whitespace characters
# \s not a white space characters
# \w word character as well as number and the underscore
# \W not a word character
# (...)