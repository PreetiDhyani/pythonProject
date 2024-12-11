class Car:
    model = None
    name = None
    password = 123
    password_secure = 123

    def __init__(self):
        self.password = "Parmod" # public instance variable
        self.__password_secure = "Pass 123" # by adding __ we can make our variable private


    def change_password(self):
        print(self.password)


# object_ref = Car()
# print(object_ref.password) #Public variable_we can change password
# object_ref.password = "Geeta" #Public variable_we can change password
# print(object_ref.password) #Public variable_we can change password

object_ref = Car()
print(object_ref.password_secure) #Private variable_we can't change password
object_ref.password_secure = "Geeta Sharma" #Public variable_we can't change password
print(object_ref.__password_secure)