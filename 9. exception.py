try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is {result:.2f}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
    
except ValueError:
    print("Error: Invalid input! Please enter numeric values.")
    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    
finally:
    print("Execution completed. Thank you for using the program!")