import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        list_task.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = list_task.curselection()[0]
        list_task.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")


root = tk.Tk()
root.title("To-do List App")


frame_input = tk.Frame(root)
frame_input.pack(pady=10)
entry_task = tk.Entry(frame_input, width=40)
entry_task.pack(side=tk.LEFT, padx=10)
button_add = tk.Button(frame_input, text="Add task", command=add_task)
button_add.pack(side=tk.LEFT)


list_task = tk.Listbox(root, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
list_task.pack(pady=10)

button_delete = tk.Button(root, text="Delete task", command=delete_task)
button_delete.pack(pady=5)

root.mainloop()