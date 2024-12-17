class Father:
    key = "2BK"

    def car(self):
        print("Father has a car -> Alto")
        print(self.key)


class Son(Father):
    key2 = "3BHK"

    def suv(self):
        print("MG hector, black")
        print(self.key2)


Father_ref = Father()
Father_ref.car()

Son_ref = Son()
Son_ref.car()


