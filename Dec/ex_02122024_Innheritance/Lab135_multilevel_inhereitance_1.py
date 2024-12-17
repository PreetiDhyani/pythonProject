class Grandfather:
    titanium = "1kg"

    def home0(self):
        print("1BHK")

class Parent(Grandfather):
    gold = "2kg"

    def home(self):
        print("2BHK")

class Child(Parent):
    diamond = "Diamond"

    def home2(self):
        print("3BHK")

Parent_ref = Parent()
print(Parent_ref.titanium)
Parent_ref.home0()

Child_ref = Child()
print(Child_ref.gold)
Child_ref.home0()