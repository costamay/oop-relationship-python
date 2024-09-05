class Person:
    all_persons = []
    count_persons = 0
    
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.add_person(self)
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        # if not value.isalpha():
        #     raise ValueError("First name must contain only letters")
        # self._first_name = value
        if isinstance(value, str):
            self._first_name = value
        else:
            raise ValueError("First name must be a string")

    
        
        
    def greeting(self):
        return f"Hello, my name is {self.first_name} {self.last_name}. I am {self.age} years old."
    
    @classmethod
    def add_person(cls, person):
        cls.all_persons.append(person)
        
        
    @classmethod
    def print_first_names(cls):
        return [person.first_name for person in cls.all_persons]
        # person_list = []
        # for person in cls.all_persons:
        #     person_list.append(person.first_name)
        # return person_list
        
    
    
        
        
        

kennedy =   Person("Kennedy", "Owusu", 20)

print(kennedy.age)

ivy = Person("Ivy", "Lona", 0)

print(ivy.age)

# print(Person.all_persons)

# print(Person.print_first_names())

