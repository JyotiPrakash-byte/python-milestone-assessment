class Employee:

    def __init__(self,employee_id,name,role,salary):
        self.employee_id=employee_id
        self.name=name
        self.role=role
        self.salary=salary

    def display_details(self):
        print(f"{self.employee_id} - {self.name} - {self.role} - {self.salary}")

def add_employee(employee):
    with open("employees.txt","a") as file:
        file.write(f"{employee.employee_id},{employee.name},{employee.role},{employee.salary}\n")

def read_employees():
    employees=[]   

    try:
        with open("employees.txt","r") as file:
            for line in file:
                data=line.strip().split(",")

                emp=Employee(
                    int(data[0]),
                    data[1],
                    data[2],
                    int(data[3])
                )

                employees.append(emp)
    except FileNotFoundError:
        print("employees.txt file not found")

    return employees

def find_highest_salary(employees):
    return max(employees,key=lambda emp:emp.salary)

def find_employees_by_role(employees):
    role_count={}

    for emp in employees:
        role_count[emp.role] = role_count.get(emp.role,0) + 1

    return role_count

employee1=Employee(101,"Rahul","Python Developer",50000)
employee2=Employee(102,"Anjali","Tester",45000)
employee3=Employee(103,"John","Developer",60000)
employee4=Employee(104,"Priya","Tester",48000)

with open("employees.txt","w") as file:
    pass

add_employee(employee1)
add_employee(employee2)
add_employee(employee3)
add_employee(employee4)

employees=read_employees()

print("\n====== Employee Details=========")
for emp in employees:
    emp.display_details()

print("\n=========== Employee With salary > 50000 ============")
for emp in employees:
    if emp.salary > 50000:
        print(f"{emp.name} - {emp.salary}")

highest_paid= find_highest_salary(employees)

print("\n=======Highest paid employee =========")
print(f"{highest_paid.name} - {highest_paid.salary}")

print("\n=======Employee count by role =========")
roles=find_employees_by_role(employees)

for role,count in roles.items():
    print(f"{role}: {count}")




