class Father:

    def home(self):
        return "This is my home1"

    def father_money(self):
        return 5


class Mother:

    def home(self):
        return "This is my home2"

    def mother_money(self):
        return 2


class Son(Mother, Father):
    print("Son")

    def print_info(self):
        print("Son")


Son_ref = Son()
print(Son_ref.mother_money())
print(Son_ref.father_money())
print(Son_ref.home())
