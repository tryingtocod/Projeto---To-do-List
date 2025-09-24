import tkinter as tk
from tkinter import messagebox, simpledialog

# Variáveis globais
task_goal = 0
tasks_done = []
tasks = []

def celebrate():
    messagebox.showinfo("Parabéns! 🎉", "Você atingiu sua meta de tarefas!\n🎉🎉🎉")

def update_progress():
    completed = len(tasks_done)
    if task_goal > 0 and completed >= task_goal and not update_progress.goal_achieved:
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
        tasks.pop()
        draw_tasks()

def toggle_done(index):
    task = tasks[index]
    if task in tasks_done:
        tasks_done.remove(task)
    else:
        tasks_done.append(task)
    draw_tasks()
    update_progress()

def draw_tasks():
    task_canvas.delete("all")
    for i, task in enumerate(tasks):
        x, y = 20, 30 + i * 50
        color = "green" if task in tasks_done else "lightgreen"
        # Desenha bolinha
        task_canvas.create_oval(x, y, x+20, y+20, fill=color, outline="")
        task_canvas.create_text(x+50, y+10, text=task, anchor="w", font=("Arial", 12, "bold"), fill="black")
        # Vincula clique na bolinha
        task_canvas.tag_bind(task_canvas.create_oval(x, y, x+20, y+20), "<Button-1>", lambda e, idx=i: toggle_done(idx))

# ======== Função utilitária: desenhar retângulo arredondado ==========
def round_rectangle(canvas, x1, y1, x2, y2, r=25, **kwargs):
    points = [
        x1+r, y1,
        x1+r, y1,
        x2-r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y1+r,
        x2, y2-r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x2-r, y2,
        x1+r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y2-r,
        x1, y1+r,
        x1, y1+r,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# ================== UI ====================
root = tk.Tk()
root.title("To-do List estilizada (Tkinter puro)")

# Perguntar meta inicial
task_goal = simpledialog.askinteger("Can you be productive today?", minvalue=1)

# Canvas de entrada com bordas arredondadas
input_canvas = tk.Canvas(root, width=420, height=60, bg="white", highlightthickness=0)
input_canvas.pack(pady=10)
round_rectangle(input_canvas, 5, 5, 410, 55, r=20, fill="#e5d4fa", outline="")

# Entry por cima do canvas
entry_task = tk.Entry(root, width=30, font=("Arial", 12), relief="flat", bg="#e5d4fa")
entry_window = input_canvas.create_window(130, 30, window=entry_task)

# Botão Add estilizado
button_add = tk.Button(root, text="Add Task", command=add_task,
                       bg="#d7b3f7", fg="black", font=("Arial", 12, "bold"),
                       relief="flat")
button_window = input_canvas.create_window(330, 30, window=button_add)

# Canvas para exibir tarefas
task_canvas = tk.Canvas(root, width=420, height=300, bg="#ffe6cc", highlightthickness=0)
task_canvas.pack(pady=20)

# Botão deletar
delete_canvas = tk.Canvas(root, width=200, height=50, bg="white", highlightthickness=0)
delete_canvas.pack(pady=5)
round_rectangle(delete_canvas, 5, 5, 190, 45, r=15, fill="#ff9999", outline="")
button_delete = tk.Button(root, text="Deletar última tarefa", command=delete_task,
                          bg="#ff9999", fg="black", font=("Arial", 11, "bold"),
                          relief="flat")
delete_canvas.create_window(100, 25, window=button_delete)

root.mainloop()
