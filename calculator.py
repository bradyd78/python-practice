import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display input/output
entry = tk.Entry(root, width=16, font=('Arial', 24), bd=10, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

root.mainloop()
