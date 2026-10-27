with open("notes.txt","w") as file:
    file.write("Line 1: good in java\n")
    file.write("Line 2: good in python\n")
    file.write("Line 3: good in playwright\n")
    file.write("Line 4: good in sql\n")
    file.write("Line 5: good in selenium\n")

print("completed file connect: ")
with open("notes.txt","r") as file:
    content = file.read()
    print(content)

with open("notes.txt","r") as file:
    lines=file.readlines()
    print("Third Line:")
    print(lines[2])

with open("notes.txt","a") as file:
    file.write("Line 6: good in javascript\n")

print("New line append successfully")
