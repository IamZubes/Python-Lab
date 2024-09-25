#for loop

item_prices = [19.99, 5.49, 12.99, 3.99, 8.49]
tax_rate = 0.05

total_cost = 0

for price in item_prices:
    total_cost += price

total_cost_with_tax = total_cost * (1 + tax_rate)

print(f"Total cost including tax (for loop): ${total_cost_with_tax:.2f}")

#while loop
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = int(input("Enter your ATM PIN: "))
    
    if pin == 1234:
        print("Access granted!")
        break
    else:
        attempts += 1
        print(f"Incorrect PIN. Attempts left: {max_attempts - attempts}")

if attempts == 3:
    print("Account locked due to too many incorrect attempts.")