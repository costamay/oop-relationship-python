class Student:
    all = []
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._teacher = None
        Student.all.append(self)
        
    # getter and setter methods
        
    @property
    def teacher(self):
        return self._teacher
    
    @teacher.setter
    def teacher(self, teacher):
        if not isinstance(teacher, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = teacher
        
        
class Teacher:
    def __init__(self, name):
        self.name = name
        
    def students(self):
        return [student.__dict__ for student in Student.all if student.teacher == self]
    
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self
        
s1 = Student("John", 20) 
s2 = Student("Jane", 22)
s3 = Student("Jack", 21)
s4 = Student("Jill", 19)
# s1.teacher = "Kennedy" #wrong
# s1.teacher = Teacher("Mr. Smith") #right 
        
teacher1 = Teacher("Mr. Smith")
teacher2 = Teacher("Mr. Johnson")

# assigning students to teachers

s1.teacher = teacher1
s2.teacher = teacher2

s3.teacher = teacher1
s4.teacher = teacher2

# all student for teacher1 Mr. Smith

smith_students = teacher1.students()

print(f"Mr. Smith students...................")
print(smith_students)

# all student for teacher2 Mr. Johnson
johnson_students = teacher2.students()

print(f"Mr. Johnson students...................")
print(johnson_students)     