students={
    "Jyoti":75,
    "Biswa":38,
    "Baidyanath":45
}

for name, marks in students.items():
    if marks > 40:
        print(name,"- pass")
    else:
        print(name,"- fail")