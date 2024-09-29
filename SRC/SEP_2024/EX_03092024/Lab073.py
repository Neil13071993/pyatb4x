# Web Automation - Selenium
# Page - You are going automate

class vmologinpage:

    def __init__(self, email_arg, password_arg):
        self.email = "email_arg"
        self.password = "password_arg"

    def login_confirmation(self):
        if self.email == "ng@gmail.com" and self.password == "pass@123":
            print(" Allowed to login")
        else:
            print("Not Allowed")


email = input("Enter the email \n")
password = input("Enter the password \n")

vmo_Obj = vmologinpage(email, password)
vmo_Obj.login_confirmation()
