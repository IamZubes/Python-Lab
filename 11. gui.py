import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.config(bg="lightblue")

label = tk.Label(root, text="GUI Example")
label.pack()

def hello():
    label.config(text="Hello Zubin")

button = tk.Button(root, text="Click me!", command=hello)
button.pack()

root.mainloop()