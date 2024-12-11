

class VWOLoginPage:


    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "preetidhyani21@gmail.com" and self.password == "Pass123" :
            print("Allowed, login sucess")

        else:
            print("Login failed")



email = input("Enter the email \n")
password = input("Enter the password \n")


vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()

# vwo_obj = VWOLoginPage("preetidhyani21@gmail.com","Pass123")
# vwo_obj.login_confirm()