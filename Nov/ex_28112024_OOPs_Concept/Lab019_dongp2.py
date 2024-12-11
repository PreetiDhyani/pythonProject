class Dog:
#Attributes
     name = "Chow"
     breed = None
     height = None


# Behaviour
     def bark(self):
         print("barking")
     def sleep(self):
         print("sleep")


# Object ref
chow_ref = Dog()
mow_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)

# Dog() - Object
# chow - object ref