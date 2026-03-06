class Student:
    College_name = "ABC College"   #class variable
    def __init__(self, name ,marks):     #parameterized Constructor
     self.name = name
     self.marks = marks
    print("WELCOME TO PYTHON OOP")
     
s1 = Student("Nigah Zahra", 85)  
print(s1.name, s1.marks)
s2 = Student("Maryem", 90)  
print(s2.name, s2.marks)
print(Student.College_name)   #accessing class variable using class name
