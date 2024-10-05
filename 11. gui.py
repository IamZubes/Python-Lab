import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.config(bg="lightblue")

label = tk.Label(root, text="GUI Example", width=20, height=2)
label.pack()

def hello():
    label.config(text="Hello Zubin")

button = tk.Button(root, text="Click me!", command=hello, width=20, height=2)
button.pack(pady=20)

root.mainloop()