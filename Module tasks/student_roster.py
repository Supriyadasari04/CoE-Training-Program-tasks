class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.student_class = None  

    def add_class(self, student_class):
        self.student_class = student_class  

    def display(self):
        print("Original attributes and their values of the Student class:")
        print(f"Student ID: {self.id}")
        print(f"Student Name: {self.name}")
        if self.student_class:
            print(f"Student Class: {self.student_class}")

id = input("Enter Student Id: ")
name = input("Enter Student Name: ")
student = Student(id,name)
student_class = input("Enter Student Class (optional, press Enter to skip): ")
if student_class:
    student.add_class(student_class)
student.display()
