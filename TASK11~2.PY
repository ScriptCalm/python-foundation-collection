
# Task 11.1.b

class Student:
    def __init__(self, name, age, course, ID):
        self.name = name
        self.age = age
        self.course = course
        self.ID = ID
        
    def print_details(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Course: " + self.course)
        print("Student ID: " + self.ID)
        
student1 = Student("Bob", 20, "Computer Science", "1000121")
student2 = Student("Alice", 21, "Computer Science", "1000475")
student3 = Student("Jane", 18, "Information Technology", "1000823")

student1.print_details()
student2.print_details()
student3.print_details()

print(' ') # Space
print('Input area.')

print('Please enter the details for a new student:')
# Input a new student details
student4 = Student(
    name = input('Name: '),
    age = input('Age: '),
    course = input('Course: '),
    ID = input('Student ID: ')
    )

print(' ') # Space
print('Output area:')

student4.print_details() # Calling the print function
