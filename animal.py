class Animal:
    all = []
    animal_count = 0
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        Animal.add_animal(self)
        Animal.track_animal_count()
        
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")
        
    def greetings(self):
        print(f"Hello, my name is {self.name} and I'm {self.color}")
        
    @classmethod
    def add_animal(cls, animal):
        cls.all.append(animal)
        
    @classmethod
    def track_animal_count(cls):
        cls.animal_count += 1
        
    @classmethod
    def print_animal_details(cls):
        # animal_list = []
        # for animal in cls.all:
        #     animal_list.append(animal.__dict__)
            
        # print(animal_list)
        return [animal.__dict__ for animal in cls.all]
            
            
    
    
        
        
    



cat = Animal("Rex", "red")

# print(cat)

dog = Animal("Scobby", "green")
# print(dog)

all_animals = Animal.all

# print(all_animals)
# print(Animal.animal_count)

x = Animal.print_animal_details()

print(x)
