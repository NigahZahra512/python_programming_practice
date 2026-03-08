class Nadra_System():
    def __init__(self,name,district,biometric):
        self.name = name
        self._district = district
        self.__biometric_data = biometric
    def verify_fingerprint(self,scan_input):
        if scan_input == self.__biometric_data :
            print("Match! Identity Verified ")
            return True
        else:
            print("Do not Match!Security Alert")
            return False

citizen =Nadra_System("Nigah Zahra" ,"MUzaffarabad" ,"encode Thumbprint-512")
print(citizen.name)
print(citizen._district)
citizen.verify_fingerprint("encode Thumbprint-512") 





class Nadra_System():
    def __init__(self,name,district,biometric):
        self.name = name
        self._district = district
        self.__biometric_data = biometric


    def show_identity(self):
        print(f" ID card holder : {self.name}")

    def show_location(self):
        print(f" District of {self.name} is : {self._district}")
        
    def verify_fingerprint(self,scan_input):
        if scan_input == self.__biometric_data :
            print("Match! Identity Verified ! ")
            return True
        else:
            print("Do not Match!Security Alert")
            return False

citizen =Nadra_System("Nigah Zahra" ,"MUzaffarabad" ,"encode Thumbprint-512")
citizen.show_identity()
citizen.show_location()
citizen.verify_fingerprint("encode Thumbprint-512") 


#practice 
class Student:
    def __init__(self, marks):
        self.__marks = marks   # private variable

    def set_marks(self, m):
        if m >= 0 and m <= 100:
            self.__marks = m
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks


s = Student(80)

print("Marks:", s.get_marks())

s.set_marks(90)

print("Updated Marks:", s.get_marks())