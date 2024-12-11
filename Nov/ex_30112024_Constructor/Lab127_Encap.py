class Car:

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model

    def start_engine(self):
        print("Starting a car with the name " + self.name)
        print("Starting a car with the make " + self.make)
        print("Starting a car with the model " + self.model)

lambo = Car("Lambo", "V6", "2023")
lambo.start_engine()

print("-------------------")


Citron = Car("French", "Turbo", "2024")
Citron.start_engine()