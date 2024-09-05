class Car:
    def __init__(self, make, model, year):
        print("I am a car")
        self.make = make
        self.model = model
        self.year = year
        
    def start(self):
        print(f"{self.make} {self.model} started")
        
    
mercedes =  Car("Mercedes", "G63", "2017" )
print(mercedes.year)
print(mercedes.start())

bmw = Car("BMW", "M5", "2021")
print(bmw.model)
print(bmw.start())

# school management system
# Users
# Student
# Staff
# classroom
# program