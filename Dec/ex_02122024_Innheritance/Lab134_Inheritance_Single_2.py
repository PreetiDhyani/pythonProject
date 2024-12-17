class Parent:
    gold = "2kg"

    def home(self):
        print("2BHK")

class Child(Parent):
    diamond = "Diamond"

    def home2(self):
        print("3BHK")

child_object = Child()
print(child_object.gold)
child_object.home()

father_object_ref = Parent()
father_object_ref.home()
