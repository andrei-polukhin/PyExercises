import tkinter as tk
# ttk stands for theme tk
# this is a theme for components of the app
from tkinter import ttk


def greet():
    # This will print some text
    # into a PYTHON CONSOLE
    print("Hello, world!")


# Initializing the main window
root = tk.Tk()
# Titling the window
root.title("Hello, world!")

# Initializing the greet button
# into root - the main window
# with the text "Greet" onto it
# which calls function greet when asked (no parenthesis)
greet_button = ttk.Button(root, text="Greet", command=greet)
# Aligning to the left, filling Ox, expands on the width
# of the screen
greet_button.pack(side="left", fill="x", expand=True)

# root.destroy function preemptively stops the application
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)

# tk.Tk().mainloop() occupies the thread of the application
root.mainloop()
