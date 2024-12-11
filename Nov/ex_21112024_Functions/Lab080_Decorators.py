def add_extra_security(func):

    def wrapper():
        print("1. Before the function called")
        print("Take necessary  things")
        func()# driving scooty
        print("this will print after main function")
    return wrapper()


@add_extra_security
def driving_scooty():
    print("Normal function")
    print("I am driving scooty")

@add_extra_security
def driving_car():
    print("Normal function")
    print("I am driving car")