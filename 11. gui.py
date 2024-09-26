import tkinter as tk
from tkinter import messagebox

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = var_operation.get()

        if operation == "Add":
            result = add(num1, num2)
        elif operation == "Subtract":
            result = subtract(num1, num2)
        elif operation == "Multiply":
            result = multiply(num1, num2)
        elif operation == "Divide":
            result = divide(num1, num2)
        
        messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Input fields
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

# Operation selection
var_operation = tk.StringVar(value="Add")
label_operation = tk.Label(root, text="Select operation:")
label_operation.pack()

operations = ["Add", "Subtract", "Multiply", "Divide"]
for operation in operations:
    rb = tk.Radiobutton(root, text=operation, variable=var_operation, value=operation)
    rb.pack(anchor=tk.W)

# Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

# Start the GUI event loop
root.mainloop()
