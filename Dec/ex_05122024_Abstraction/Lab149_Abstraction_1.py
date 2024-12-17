from tkinter.font import names


class Father():
   def __init__(self, name):
       self.name = name


   def loan(self):
       pass

class Son(Father):

    def loan(self):
        print("1L Given")

Object_Ref = Son("Preeti")
Object_Ref.loan()
