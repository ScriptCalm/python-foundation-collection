
# Task 11.1.a

class Student: # Creating class Student
    def __init__(self, name, age, course, ID): # Defining constructor with attributes
        self.name = name
        self.age = age
        self.course = course
        self.ID = ID
        
    def print_details(self): # Creating print function
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Course: " + self.course)
        print("Student ID: " + self.ID)

# Creating objects        
student1 = Student("Bob", 20, "Computer Science", "1000121")
student2 = Student("Alice", 21, "Computer Science", "1000475")
student3 = Student("Jane", 18, "Information Technology", "1000823")

# Calling the print function based on the objects
student1.print_details()
student2.print_details()
student3.print_details()
