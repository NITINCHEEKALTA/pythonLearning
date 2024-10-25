import sys
def main():

    print("Welcome to BMI calculator")

    weight = float(input("Enter your weight :"))
    height = float(input("Enter your height in meters : "))

    if weight <= 0.0 or height <= 0.0:
        print("Please enter values greater than zero thank you")
        sys.exit()
    else:
        Bmi(weight, height)    

def Bmi(weight,height):

    bmi = round((weight / height **2),2)

    if bmi <= 18.5:
        print("your bmi is {bmi} and You are under weight")

    elif 18.5 < bmi <= 24.9:
        print(f" your bmi is {bmi} and Your weight is normal")

    elif 25 < bmi < 29.9:
        print(f"your bmi is {bmi} and You are overweight")
    
    else:
        print(f"your bmi is {bmi} and You are obese")

if __name__ == "__main__":
    main()