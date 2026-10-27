import csv

with open("employees.csv","w") as file:
    writer=csv.writer(file)
    writer.writerow(["id","name","salary"])
    writer.writerow([1,"Biswa",40000])
    writer.writerow([2,"Jyoti",70000])
    writer.writerow([3,"Baidya",50000])

print("employees.csv created successfully")