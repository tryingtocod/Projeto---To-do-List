import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# Variáveis globais
task_goal = 0
tasks_done = []
tasks = []

# ================= Funções ====================

def celebrate():
    messagebox.showinfo("Parabéns! 🎉", "Você atingiu sua meta de tarefas!\n🎉🎉🎉")

def update_progress():
    completed = len(tasks_done)
    if task_goal > 0:
        progress = int((completed / task_goal) * 100)
        progress_bar["value"] = progress
        progress_label.config(text=f"{completed}/{task_goal} tarefas concluídas")

        if completed >= task_goal and not update_progress.goal_achieved:
            celebrate()
            update_progress.goal_achieved = True  

update_progress.goal_achieved = False

def add_task():
    task = entry_task.get()
    if task:
        tasks.append(task)
        draw_tasks()
        entry_task.delete(0, tk.END)
        update_progress()
    else:
        messagebox.showwarning("Aviso", "Por favor, insira uma tarefa.")

def delete_task():
    if tasks:
        task = tasks.pop()
        if task in tasks_done:
            tasks_done.remove(task)
        draw_tasks()
        update_progress()

def toggle_done(index):
    task = tasks[index]
    if task in tasks_done:
        tasks_done.remove(task)
    else:
        tasks_done.append(task)
    draw_tasks()
    update_progress()

def draw_tasks():
    for widget in task_frame.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        frame = tk.Frame(task_frame, bg="#fffaf0", bd=2, relief="groove")
        frame.pack(fill="x", padx=10, pady=5)

        var = tk.BooleanVar(value=(task in tasks_done))
        check = tk.Checkbutton(frame, variable=var, command=lambda idx=i: toggle_done(idx),
                               bg="#fffaf0", activebackground="#fffaf0")
        check.pack(side="left", padx=5)

        task_text = tk.Label(frame, text=task, font=("Arial", 12, "bold"), bg="#fffaf0")
        task_text.pack(side="left", padx=5)

        if task in tasks_done:
            task_text.config(fg="gray", font=("Arial", 12, "bold", "overstrike"))
        else:
            task_text.config(fg="black", font=("Arial", 12, "bold"))

# ================== UI ====================

root = tk.Tk()
root.title("To-do List estilizada (Tkinter)")
root.geometry("500x600")
root.configure(bg="#f5f5f5")

# Perguntar meta inicial
task_goal = simpledialog.askinteger("Meta do dia", "Quantas tarefas você quer concluir hoje?", minvalue=1)

# Entrada
entry_frame = tk.Frame(root, bg="#f5f5f5")
entry_frame.pack(pady=10)

entry_task = tk.Entry(entry_frame, width=30, font=("Arial", 12))
entry_task.pack(side="left", padx=5)

button_add = tk.Button(entry_frame, text="Adicionar", command=add_task,
                       bg="#7D5BA6", fg="white", font=("Arial", 12, "bold"),
                       relief="flat", padx=10, pady=5)
button_add.pack(side="left")

# Barra de progresso
progress_label = tk.Label(root, text="0/0 tarefas concluídas", bg="#f5f5f5", font=("Arial", 11))
progress_label.pack(pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5)

# Lista de tarefas
task_frame = tk.Frame(root, bg="#f5f5f5")
task_frame.pack(fill="both", expand=True, pady=10)

# Botão deletar
button_delete = tk.Button(root, text="Deletar última tarefa", command=delete_task,
                          bg="#E57373", fg="white", font=("Arial", 11, "bold"),
                          relief="flat", padx=10, pady=5)
button_delete.pack(pady=10)

root.mainloop()