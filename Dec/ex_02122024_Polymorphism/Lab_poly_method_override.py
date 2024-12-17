class Father:
    def home(self):
        print("1BHK")

class Pramod(Father):
    def home(self):
        print("3BHK")

p = Pramod()
p.home() # it will call 3BHK, local has highest prefernce

f = Father()
f.home()