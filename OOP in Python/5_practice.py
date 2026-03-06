"""create student class that take name and marks of 3 subjects as arguments 
in constructor then create a method to print average
calculate the grade based on marks"""

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        
        avg = sum / 3
        print("hi",self.name ,"your Marks avg is :",avg)

        if avg >= 90:
            print("your grade is : A+")
        elif avg >= 80:
            print("your grade is : A")
        elif avg >= 70:
            print("your grade is : B")
        elif avg >= 60:
            print("your grade is : C")
        elif avg >= 50:
            print("your grade is : D")
        else:
            print("your grade is : F")

s1 = Student("nigah" , [97,89,76])
s1.get_avg()
s1 = Student("Maryem" , [85,78,92])
s1.get_avg()

     
