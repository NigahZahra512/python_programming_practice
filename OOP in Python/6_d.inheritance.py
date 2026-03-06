class Father:
    def __init__(self, eyecolor):
        self.eyecolor = eyecolor

class Children(Father):
    def __init__(self, eyecolor, haircolor):
        Father.__init__(self, eyecolor)  # parent attribute inherit
        self.haircolor = haircolor       # child attribute

child1 = Children("Brown", "Black")
print(child1.eyecolor)  # from parent
print(child1.haircolor) # from child


class Father:
    def show_skill(self):
        print("Driving")

class Children(Father):
    def __init__(self, name):
        self.name = name   # child attribute

child1 = Children("Ali")
child1.show_skill()  # parent method
print(child1.name)   # child attribute