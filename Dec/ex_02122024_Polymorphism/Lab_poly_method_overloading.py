#Method overloading

class MathUtils:
    def add(self, a, b):
        return a+b
    def add(self, a=9, b=9, c=9):
        return a+b+c
    def add(self, a=0, b=0, c=0, d=0):
        return a+b+c+d

math = MathUtils()
# op1 = math.add(1,2)
op2 = math.add(1,2,3)
print("ope")
op3 = math.add(1,2,3,4)