import tkinter as tk
from tkinter import ttk


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)


root = tk.Tk()
root.title("Text-Editor-Redefined")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(5,0))

menubar = tk.Menu()
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(menu=file_menu, label="File")

file_menu.add_command(label="New", command=create_file)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.mainloop()
