def main():
   time = "7:30"
   meal(time)

def conv(time):

  time = time.split(':',1)

  return time

def meal(mealTime):
   time= conv(mealTime)
   hour = time[0]
   min = time[len(time)-1]
   
   if (hour >= '7' or hour <= '8') and (min == '00' or min <= '59'):
      print("break fast")
   elif (hour >= '12' or hour <= '13') and ( min == '00' or min <= '59'):
      print("lunch")

main()
        

