class Person:

    #Attributes - What you have
     id = None
     name = None
     age = None
     email = None

    # Behaviour  What you can do?

     def talk(self):     #Not returning not argument
        print("I can talk")

     def Sleep(self, name):     #Argument with no return
        print("I can sleep")

     def eat(self, name):     #Argument with return
        print("I can eat")
        return None

     def walk(self):
        return "I am walking" #No argument with return



