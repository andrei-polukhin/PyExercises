import tkinter as tk
from tkinter import ttk


def greet():
    # Printing the contents of user_name.get()
    # or 'World' if entry field is empty (see below)
    print(f"Hello, {user_name.get() or 'World'}")
    # Just a small improvement to delete the contents
    # of the entry when the button is pressed
    name_entry.delete(0, "end")


# Defining the main window
root = tk.Tk()
# Defining the title for the main window
root.title("Greeter")

# Defining the "Name: " label
name_label = ttk.Label(root, text="Name: ")
# Aligning the label to the left, and adding padding
# so that it has 10 extra px on the right side
name_label.pack(side="left", padx=(0, 10))

# Defining the variable which stores entry contents
user_name = tk.StringVar()
# Defining entry with the width of 20px, its contents are in
# tk variable defined above
name_entry = ttk.Entry(root, width=20, textvariable=user_name)
# Aligning to the left so all components stay side-by-side
name_entry.pack(side="left")
# Enabling blue frame on focus
name_entry.focus()

# Enabling the greet button, which pressed calls greet()
greet_button = ttk.Button(root, text="Greet", command=greet)
# Greet button is also aligned to left and fills the width of
# the main window
greet_button.pack(side="left", fill="x")

# Running the programme per se
root.mainloop()
