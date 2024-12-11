def add_my_example(func):

    def wrapper():
        print("Please print 1")
        print("please print before")
        func()
        print("please print after")
    return wrapper()


@add_my_example
def my_example():
    print("this is just an example")