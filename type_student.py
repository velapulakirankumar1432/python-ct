class Student:
    def __init__(self, name, age, roll_no, marks):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)
    def result(self):
        if self.marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")
    def update_marks(self, new_marks):
        self.marks = new_marks
        print("Marks updated successfully")
