class Student:
    def __init__ (self,name, school_id, gpa):
      self.name = name
      self.school_id = school_id
      self.gpa = gpa 

    def __str__(self):
        return f'Student name: {self.name}, ID {self.school_id}, GPA{self.gpa}'

alex = Student( 'Alex','jsjalkj', 3.2)
print(alex.name)
print(alex.school_id)
print(alex)

sam = Student('Sam','xkjksw', 3.6)
print (sam)