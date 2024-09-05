from dataclasses import dataclass

@dataclass
class Student:
        name:str
        school_id: str
        gpa: float 

        def __str__(self):
         return f'Student name: {self.name}, ID:{self.school_id},GPA: {self.gpa}'

#create a student objects 
def main ():
    alex = Student ('Alex','abced', 3.2)
    print(alex)

    manuel= Student ('Manuel','xkww', 3.5)
    print(manuel)

    lucy = Student('Lucy','njaje',3.5)

main()


    #if you don't have a str defined, it will still print legible information.
    

