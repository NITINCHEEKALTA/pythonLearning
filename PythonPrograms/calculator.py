import sys
def main():


    
    print(cal())

def cal():
        try:
            task = input("what is the task you want to perform? : ")
            if task not in ["sum", "subtraction", "multiplication", "division"]:
                sys.exit     
            else:
                num = int(input("What is the number ? "))
                num2 = int(input("what is the second number ? "))
        except (TypeError, ValueError):
            print("Invalid arguments")    
        
        match task:

            case "sum":
                return num + num2
            
            case "subtraction":
                return num - num2
            
            case "multiplication":
                return num * num2
            
            case "division":
                return num / num2
            
            case _:
                return "Invalid task"

if __name__ == "__main__":
    main()
