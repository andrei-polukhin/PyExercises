import tkinter as tk
from tkinter import ttk

# Initializing the main window
root = tk.Tk()

# Defining the main frame which is aligned to left
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

# Putting 2 labels into the frame, the labels are aligned to top
tk.Label(main, text="Label top", bg="green").pack(side="top", fill="both", expand=True)
tk.Label(main, text="Label top", bg="blue").pack(side="top", fill="both", expand=True)

# This label is in the main window, so touches the right side of the frame
tk.Label(root, text="Label left", bg="red").pack(
    side="left", fill="both", expand=True
)

# Running the main window
root.mainloop()
