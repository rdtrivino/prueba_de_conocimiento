import tkinter as tk
import random

def disable_row_column(row, column):
    if len(selected_positions) < 5:
        for i in range(10):
            buttons[i][column].config(state=tk.DISABLED, bg="blue", text="X")
            buttons[row][i].config(state=tk.DISABLED, bg="blue", text="X")
        selected_positions.append((row, column))
        if len(selected_positions) == 5:
            select_random_button.config(state=tk.DISABLED)

def select_random():
    if len(selected_positions) < 5:
        while True:
            row = random.randint(0, 9)
            column = random.randint(0, 4)
            if (row, column) not in selected_positions:
                disable_row_column(row, column)
                break

window = tk.Tk()
window.title("Aprendiz SENA ")

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.geometry("+%d+%d" % (x, y))

for i in range(5):
    window.columnconfigure(i, weight=1)

title_label = tk.Label(window, text="Aprendiz Rubén Darío Triviño Díaz - Programa ADSO", font=("Arial", 16))
title_label.grid(row=0, column=0, columnspan=5)

buttons = []
selected_positions = []
for i in range(10):
    row_buttons = []
    for j in range(5):
        button = tk.Button(window, text="", padx=10, pady=5, command=lambda row=i, column=j: disable_row_column(row, column), bg="white")
        button.grid(row=i+1, column=j, sticky="nsew")
        row_buttons.append(button)
    buttons.append(row_buttons)

select_random_button = tk.Button(window, text="Seleccionar Aleatoriamente", command=select_random)
select_random_button.grid(row=11, column=0, columnspan=5)

window.mainloop()
