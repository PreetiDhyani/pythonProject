from dotenv import load_dotenv
import os

class VWOLoginPage:


    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.email == "preeti21@gmail.com" and self.password == "Pass123":
            print("Allowed, login success")

        else:
            print("Login failed")


load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

vwo_obj = VWOLoginPage(email, password)
vwo_obj.login_confirm()

# vwo_obj = VWOLoginPage("preetidhyani21@gmail.com","Pass123")
# vwo_obj.login_confirm()