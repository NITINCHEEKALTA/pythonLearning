def conditionals_demo():
    """compare()"""""
    x = int(input("What is x ? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")    

def compare():
    x = int(input("what's x ?"))
    y = int(input("what's y ?"))

    if x < y:
        print("x is less than y")

    elif x > y:
        print("x is greater than y")
    
    else:
        print("x is equal to y")

def is_even(n):
    if n% 2 == 0:
        return True
    else:
        return False
    


conditionals_demo()