#multiplr inheritance
class father:
    def skill_father(self):
        print("Driving")


class mother:
    def skill_mother(self):
        print("Cooking")


class children(father, mother):
    def hobby(self):
        print("Gaming")


child = children()

child.skill_father()
child.skill_mother()
child.hobby()


#Multiple Inheritance
class Father:
    def __init__(self, eyecolor):
        self.eyecolor = eyecolor
    def show_eye(self):
        print(f"Eye color is {self.eyecolor}")
        
class Mother:
    def __init__(self, haircolor):
        self.haircolor = haircolor
    def show_hair(self):
        print(f"Hair color is {self.haircolor}")
        
class Children(Father, Mother):
    def __init__(self, eyecolor, haircolor):
        Father.__init__(self, eyecolor)
        Mother.__init__(self, haircolor)
    def show(self):
        print(f"Child has eye color {self.eyecolor} from father")
        print(f"Child has hair color {self.haircolor} from mother")


Ob1 = Children("bluish", "reddish")
Ob1.show()



#Multiple inheritance occurs when a class is derived from a class that is already derived from another class
class Grandparent():
    def lageacy(self):
        print("family tradition:")
class parent(Grandparent):
    def guidance(self):
        print("Guiding Children:") 
class child(parent):
    def play(parent):
        print("family tradition:")
obj = child()
obj.lageacy()
obj.guidance()
obj.play()