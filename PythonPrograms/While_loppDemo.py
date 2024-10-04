#i =1 
#while i <= 3:
 #   print("meow")
  #  i += 1
def main():
   Number = getNumber()
   meow(Number)


def getNumber():
     while True:
        n = int(input("what's n ? "))
        if n > 0:
           break 
     return n



def meow(n):
     for _ in range(n):
        print("meow")


main()