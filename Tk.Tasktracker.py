import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "No task selected!")

def mark_task_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        completed_listbox.insert(tk.END, task)
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("Task tracker")
root.configure(background="grey98")

# Entering a new task
text1 = tk.Label(root, text="Enter your task:", bg="grey98", fg="LightSlateGray")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="azure3", fg="grey22")
task_entry.pack(pady=10)

# Task management buttons
add_task_button = tk.Button(root, text="Add task", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete task", command=delete_task)
delete_button.pack(pady=5)

completed_button = tk.Button(root, text="Task is completed", command=mark_task_completed)
completed_button.pack(pady=5)

# List of all tasks
text2 = tk.Label(root, text="Task list:", bg="grey98", fg="LightSlateGray")
text2.pack(pady=5)

task_listbox = tk.Listbox(height=10, width=50, bg="LightSlateGray")
task_listbox.pack(pady=10)

# List of completed tasks
text3 = tk.Label(root, text="Completed tasks:", bg="grey98", fg="LightSlateGray")
text3.pack(pady=5)

completed_listbox = tk.Listbox(height=10, width=50, bg="MediumSeaGreen", selectmode=tk.SINGLE)
completed_listbox.pack(pady=10)

root.mainloop()