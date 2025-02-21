import tkinter as tk

# Function to handle button clicks
def on_button_click(value):
    current = entry_var.get()
    if value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif value == "C":
        entry_var.set("")
    else:
        entry_var.set(current + value)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Create an entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

# Button layout
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

# Create buttons
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda val=text: on_button_click(val))
        btn.grid(row=i+1, column=j, sticky="nsew")

# Make buttons expandable
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i+1, weight=1)

# Run the application
root.mainloop()
