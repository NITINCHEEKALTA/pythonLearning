class Student:
    def __init__(self,name,house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
            raise ValueError("Missing house")
        self.name = name
        self.house = house
        self.patronus = patronus
    

def get_student():
            name = input("Enter name :")
            house = input("Enter house :")
            patronus = input("Patronus: ") 
            return Student(name, house, patronus)
    
def main():
    student = get_student()
    print(student)
    print("Expecto Patronum!")
    print(student.charm())

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
           match self.patronus:
                  case "Stag":
                         return "Horse"
                  case "Otter":
                         return "seal"
                  case "Jack Russell Terrier":
                         return "Dog"
                  case _:
                         return ""




if __name__ == "__main__":
    main()