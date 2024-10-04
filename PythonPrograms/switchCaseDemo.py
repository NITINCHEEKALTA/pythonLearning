def switchDemo():
    name = input("What is the name ? ")
    isName(name)



def isName(name):

    match name:
        case "Harry Potter":
            print("Griffindor")
        
        case "Hermony":
            print("Slytherin")

        case "Ron":
            print("Hufflepuff")    

        case _:
            print("Not valid")    


switchDemo()