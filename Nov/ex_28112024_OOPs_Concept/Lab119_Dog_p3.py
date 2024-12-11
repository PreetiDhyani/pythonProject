class Dog:
#Attributes
     name = None
     breed = None
     height = None


     def __init__(self, name, breed):
         print("PC")
         self.name = name
         self.breed = breed
# Behaviour
     def bark(self):
         print("barking")
     def sleep(self):
         print("who is sleeping ->" + self.name)


# Object ref
chow_ref = Dog("chow", "popo")
mow_ref  = Dog("coco", "husky")

print(chow_ref.name)
print(chow_ref.breed)
chow_ref.sleep()
print(id(chow_ref))


print(mow_ref.name)
print(mow_ref.breed)
mow_ref.sleep()


# Dog() - Object
# chow - object ref

