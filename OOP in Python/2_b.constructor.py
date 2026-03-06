class Student:
    def __init__(self, name ,marks):     #parameterized Constructor
     self.name = name
     self.marks = marks
    print("WELCOME TO PYTHON OOP")
     
s1 = Student("Nigah Zahra", 85)  
print(s1.name, s1.marks)
s2 = Student("Maryem", 90)  
print(s2.name, s2.marks)


"""self parameter is reference to the current 
instance(object) of the class and is used to access 
variables that belong to the class"""