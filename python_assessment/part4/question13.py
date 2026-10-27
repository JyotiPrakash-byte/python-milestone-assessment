class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display_details(self):
        print("Name:",self.name)
        print("Roll No:",self.roll_no)
        print("Marks:",self.marks)

    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student1=Student("Biswa",101,75)
student2=Student("Jyoti",102,45)
student3=Student("Baidya",103,30)

for student in [student1,student2,student3]:
    student.display_details()
    print("Result:",student.check_result())
    
        