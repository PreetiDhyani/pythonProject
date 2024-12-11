class Person:

    def __init__(self,name):
        self.name = name
    def walk(self):
        return self.name

amit = Person("amit")
pramod = Person("Parmod")

print(amit.walk())
print(pramod.walk())