# 1 - No return type no arguments

def Say_hello():
    print("Hello")

Say_hello()

#2 No return type with argument

def Say_hello_1(Name):
    print("Hello", Name)

Say_hello_1("Preeti")

# 3 No return type with default argument

def Say_hello_2(Name="preeti" ):
    print("Hello", Name)

Say_hello_2("Dhyani")

def Say_hello_multiple_argument(name1="preeti", name2 ="Dhyani"):
    print("Hello", name1, name2)

Say_hello_multiple_argument()
Say_hello_multiple_argument(name1="preei", name2 ="Dhyan")

#4. Argument + return type

def sum_of_two(a,b):
    return a + b

result = sum_of_two(4,56)
print(result)