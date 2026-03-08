#publically Accessing Data
class bank_Account():     
    def __init__(self,owner):
        self.owner = owner
Acc_name = bank_Account("Nigah Zahra")
print(Acc_name.owner)

 #protected Accessing Data
class Bank_Account():
    def __init__(self):
        self._Branchcode = 12345   #protected
Acc_1 = Bank_Account()
print(Acc_1._Branchcode)


#both publically and protected Accessing Data
class bank_Acc():
    def __init__(self,owner):
        self.owner = owner  #publically access
        self._Branchcode = 12345 #protected
Acc_1 = bank_Acc("Nigah Zahra")
print(Acc_1.owner)
print(Acc_1._Branchcode)

#private and use another method fun to access it
class Bank_Account():
    def __init__(self):
        self.__balance = 5000   #private and use another method fun to access it
    def display(self):
        return self.__balance 
        
my_Acc = Bank_Account()
print(my_Acc.display())