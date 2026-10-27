def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >=40:
        return "C"
    else:
        return "F"

def display_student_result(student):
    total = student["python"] + student["sql"] + student["ai"]
    average=total/3
    grade=calculate_grade(average)
    result = "Pass" if average >= 40 else "Fail"

    print("\n======== Student Result =====")
    print("Student ID:",student["id"])
    print("Student Name:",student["name"])
    print("Total:",total)
    print("Average:",round(average,2))
    print("Grade:",grade)
    print("Result:",result)

    return average

students=[
    {"id":101,"name":"Rahul","python":80,"sql":75,"ai":85},
    {"id":102,"name":"Anjali","python":60,"sql":65,"ai":70},
    {"id":103,"name":"Priya","python":90,"sql":85,"ai":88},
    {"id":104,"name":"John","python":35,"sql":40,"ai":30}
]

highest_student=None
highest_average=0

for student in students:
    avg=display_student_result(student)

    if avg > highest_average:
        highest_average=avg
        highest_student=student["name"]

students_above_75=[
    student["name"]
    for student in students if (student["python"] + student["sql"] + student["ai"]) / 3 > 75
]

print("\n======== Summary ======")
print("Highest Scoring Student:",highest_student)
print("Student Above 75 Average:",", ".join(students_above_75))