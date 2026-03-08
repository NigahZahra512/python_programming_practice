#code to make owner as publically accessible , branch is protected and balance is private
class Bank_Account():
    def __init__(self,owner,branch,balance):
        self.owner = owner
        self._branch = branch
        self.__balance = balance
    def show(self):
        print(f"The Owner of Bank Account is : {self.owner}")
        print(f"Branch of Bank  is : {self._branch}")
        print(f"Total Balance in Account is : {self.__balance}")
my_Acc = Bank_Account("nigah Zahra","MAIN","50,000")
my_Acc.show()

