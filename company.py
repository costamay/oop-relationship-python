
'''
This code demonstrates a one-to-many relationship between a Company and its Employees.

The Company class has a list of Employee objects, and each Employee object has a reference to the Company it belongs to.

In this example, we create a Company instance and two Employee instances. We then add the Employee instances to the employees list of the Company instance.

By doing this, we establish the relationship between the Company and its Employees, allowing us to access the Employee information from the Company object and vice versa.

This is a common pattern in object-oriented programming, where one object (in this case, the Company) contains a reference to or collection of other objects (in this case, the Employees).
'''
class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
        

    

class Employee:
    def __init__(self,name, position):
        self.name = name
        self.position = position
        
# running our code

# creating company instance

company1 = Company("TechCorp")

# employee instances
emp1 = Employee("John", "Manager")
emp2 = Employee("Jane", "Developer")

# adding employees to the company

company1.add_employee(emp1)
company1.add_employee(emp2)

for employee in company1.employees:
    print(f"Employee Name: {employee.name}, Position: {employee.position}")

