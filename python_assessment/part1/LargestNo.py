numbers=[12,5,8,20,15]

largest=numbers[0]

for num in numbers:
    if num > largest:
        largest=num

print("First Largest Number: ",largest)