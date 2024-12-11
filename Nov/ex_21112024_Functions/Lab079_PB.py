public_toilet = "PB"

def home ():
    private_toilet = "PT"
    print(public_toilet)
    print(private_toilet)

def strange():
    print(public_toilet)
   # print(private_toilet) # local variable can't use as global

print(public_toilet)
home()

