# Grandparent class
class Grandparent:
    def __init__(self, family_name):
        self.family_name = family_name

    def show_family(self):
        print("Family Name:", self.family_name)


# Parent class inherits from Grandparent
class Parent(Grandparent):
    def __init__(self, family_name, eyecolor):
        super().__init__(family_name)
        self.eyecolor = eyecolor

    def show_eyecolor(self):
        print("Eye Color from Parent:", self.eyecolor)


# Child class inherits from Parent
class Child(Parent):
    def __init__(self, family_name, eyecolor, name):
        super().__init__(family_name, eyecolor)
        self.name = name

    def show_child(self):
        print("Child Name:", self.name)
        print("Family Name:", self.family_name)
        print("Eye Color:", self.eyecolor)


# Create a child object
child1 = Child("Khan", "Brown", "Ali")

# Call methods
child1.show_family()     # Grandparent method
child1.show_eyecolor()   # Parent method
child1.show_child()      # Child method