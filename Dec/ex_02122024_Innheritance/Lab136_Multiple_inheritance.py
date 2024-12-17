class Father:
    def father_money(self):
        return 5

class Mother:
    def mother_money(self):
        return 2

class Son(Mother, Father):
    print("Son")

    def print_info(self):
        print("Son")

Son_ref = Son()
print(Son_ref.mother_money())
print(Son_ref.father_money())