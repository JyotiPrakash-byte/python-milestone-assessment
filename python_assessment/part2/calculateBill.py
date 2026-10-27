def calculate_bill(price, quantity):
    total=price*quantity

    if total > 2000:
        total = total - (total*0.10)

    return total

print(calculate_bill(500,5))