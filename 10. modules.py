import mymath as m

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"{a} + {b} = {m.add(a, b)}")
print(f"{a} - {b} = {m.subtract(a, b)}")
print(f"{a} * {b} = {m.multiply(a, b)}")
print(f"{a} / {b} = {m.divide(a, b)}")