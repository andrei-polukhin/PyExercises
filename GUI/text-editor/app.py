import tkinter as tk
from tkinter import ttk


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)


root = tk.Tk()
root.title("Text-Editor-Redefined")

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(5,0))

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()
create_file()

root.mainloop()
