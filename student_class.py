class Student:
    
    all_students = []
    count_number_of_students = 0
    
    def __init__(self,first_name, last_name):
        self.student_count()
        self.first_name = first_name
        self.last_name = last_name
        Student.add_student_details(self)
        
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def student_count(cls):
        cls.count_number_of_students += 1
        return cls.count_number_of_students
    
    @classmethod
    def add_student_details(cls, student):
        cls.all_students.append(student)
        
    @classmethod
    def get_student_names(cls):
        for student in cls.all_students:
            print(student.last_name)
        
        


    

victor = Student("Victor", "Owusu")
print(victor.fullname())

joy =  Student("Joy","Nyarango")
print(joy.fullname())

frank = Student("Frank", "Ndegwa")

print(Student.count_number_of_students)
print(Student.all_students)
Student.get_student_names()

