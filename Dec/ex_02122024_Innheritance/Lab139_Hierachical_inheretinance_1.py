class father():
     def BHK1(self):
         print("BHK1")

class sushant(father):
    def BHK4(self):
        print("BHK4")

class preeti(father):
    def BHK5(self):
        print("BHK5")

class shritik(father):
    def BHK6(self):
        print("BHK6")

sushant_ref = sushant()
sushant_ref.BHK4()
sushant_ref.BHK1()

shritik_ref = shritik()
shritik_ref.BHK6()
shritik_ref.BHK1()