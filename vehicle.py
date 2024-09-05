class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Starting the vehicle.")
        

class Car(Vehicle):
    
    all_cars = []
    car_count = 0
    
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model
        Car.add_car(self)
        Car.get_car_count()

    def start(self):
        super().start()
        print(f"Starting the {self.brand} {self.model} car.")
        
    @classmethod
    def add_car(cls, car):
        cls.all_cars.append(car)
        return cls.all_cars
    
    @classmethod
    def get_car_count(cls):
        # cls.car_count += 1
        return len(cls.all_cars)
        
        
        

bmw = Car("BMW", "X5")
mercedes = Car("Mercedes", "C-Class")

print(bmw.start())

print(Car.all_cars)
print(Car.car_count)