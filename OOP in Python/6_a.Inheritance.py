#inheritance : Single inheritance
class Animal():   #parent class
    def __init__(self,name):
        self.name = name
        def speak(self):
            print(f"{self.name} make sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} MEOW!!")

d1 = Dog("german shaphered")
d1.speak()
c1 = Cat("kitty")
c1.speak()


class Animal():   #parent class
    def __init__(self,name):
        self.name = name
    def speak(self):
            print(f"{self.name} make different sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} MEOW!!")
Ob1 = Animal("Different Animals")
Ob1.speak()
d1 = Dog("german shaphered")
d1.speak()
c1 = Cat("kitty")
c1.speak()