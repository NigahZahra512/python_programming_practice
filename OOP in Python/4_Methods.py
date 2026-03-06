#methods are functions taht belong to objects
class Student:
    College_name = "ABC College"   
    def __init__(self, name ,marks):    
     self.name = name
     self.marks = marks
    print("WELCOME TO PYTHON OOP")

    def hello(self):
        print("Hello, I am a student of", self.College_name)
        
    def get_marks(self):
       return self.marks

s1 = Student("Nigah Zahra", 85)  
s1.hello()   #calling method using object

print(s1.get_marks())   #calling method to get marks