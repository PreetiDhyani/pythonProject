class Person1:


    def __init__(self):
        print ("I'll be called")
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")

    def name_1(self):
            print("name is->"+self.name)

Person_REF = Person1()
Person_REF.name_1()
