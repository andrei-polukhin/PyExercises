import tkinter as tk

# Initializing the main window
root = tk.Tk()

# The label will allocate all the vertical space and is glued to the left
# other elements will appear on the right side
tk.Label(root, text="Label left", bg="red").pack(side="left", fill="both", expand=True)
# Appears on the right side, glued to the top
tk.Label(root, text="Label 1", bg="blue").pack(side="top", fill="both", expand=True)
# Glued to the bottom of the second label
tk.Label(root, text="Label 2", bg="green").pack(side="top", fill="both", expand=True)
# Appears down the previous label, glued to the left of the first label
tk.Label(root, text="Label left", bg="yellow").pack(side="left", fill="both", expand=True)
# Located beneath the penultimate label, glued to the right of the previous label
tk.Label(root, text="Label left", bg="white").pack(side="left", fill="both", expand=True)

# Running the main window
root.mainloop()
