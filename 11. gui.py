import tkinter as tk

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.config(bg="lightblue")

# Add label to display instructions
label = tk.Label(root, text="Enter your name:", width=20, height=2, bg="lightblue")
label.pack(pady=10)

# Entry widget for user input
entry = tk.Entry(root, width=20)
entry.pack(pady=10)

# Function to display personalized greeting
def say_hello():
    name = entry.get()
    if name:
        label.config(text=f"Hello {name}!")
    else:
        label.config(text="Please enter your name!")

# Button to trigger the greeting
button = tk.Button(root, text="Click me!", command=say_hello, width=20, height=2)
button.pack(pady=20)

# Start the GUI loop
root.mainloop()
