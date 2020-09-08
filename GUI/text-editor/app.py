import os
import tkinter as tk
from tkinter import ttk, filedialog


def create_file():
    text_area = tk.Text(notebook)
    text_area.pack(fill="both", expand=True)
    notebook.add(text_area, text="Untitled")
    notebook.select(text_area)


def save_file():
    filepath = filedialog.asksaveasfilename()
    try:
        filename = os.path.basename(filepath)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")
        with open(filepath, "w") as file:
            file.write(content)
    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled")
        return
    notebook.tab("current", text=filename)


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
file_menu.add_command(label="Save", command=save_file)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()

root.mainloop()
