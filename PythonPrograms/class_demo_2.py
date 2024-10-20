class Student():
    
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

     #getter
    @property 
    def get_house(self):
      return self._house

    #setter
    @house.setter 
    def house(self, house):
          if house not in ["Gryffindor", "Hufflepuff", "RavenClaw", "Slytherin"]:
            raise ValueError("Invalid house")
          self._house = house   


def main():
    student = get_student()
    print(student)

def get_student():
            name = input("Enter name :")
            house = input("Enter house :")
            return Student(name, house)
    
def __str__(self):
        return f"{self.name} from {self.house}"


if __name__ == "__main__":
    main()

