import tkinter as tk
from tkinter import filedialog
import csv

LARGURA = 800
ALTURA = 600

def carregar_csv():
    filename = filedialog.askopenfilename(
        title="Escolher ficheiro CSV",
        filetypes=[("Ficheiros CSV", "*.csv"), ("Todos", "*.*")]
    )
    if not filename:
        return

    pontos = []
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                try:
                    x = int(row[0])
                    y = int(row[1])
                    pontos.append((x, y))
                except ValueError:
                    pass  # ignora linhas inválidas

    if not pontos:
        return

    # limites
    xs = [p[0] for p in pontos]
    ys = [p[1] for p in pontos]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    # evitar divisão por zero
    dx = (x_max - x_min) if x_max != x_min else 1
    dy = (y_max - y_min) if y_max != y_min else 1

    escala_x = LARGURA / dx
    escala_y = ALTURA / dy

    canvas.delete("all")

    # grelha em Y (horizontal, de 20px em 20px)
    for py in range(0, ALTURA, 20):
        valor_y = y_max - int(py / escala_y)
        canvas.create_line(0, py, LARGURA, py, fill="lightgray")
        canvas.create_text(5, py, text=str(valor_y), anchor="w", fill="black")

    # grelha em X (vertical, de 20px em 20px)
    for px in range(0, LARGURA, 20):
        valor_x = x_min + int(px / escala_x)
        canvas.create_line(px, 0, px, ALTURA, fill="lightgray")
        canvas.create_text(px, ALTURA-10, text=str(valor_x), anchor="n", fill="black")

    # desenhar pontos
    for (x, y) in pontos:
        xp = (x - x_min) * escala_x
        yp = ALTURA - (y - y_min) * escala_y
        canvas.create_oval(xp, yp, xp+2, yp+2, fill="black", outline="black")


# janela principal
root = tk.Tk()
root.title("Plot CSV")
root.geometry(f"{LARGURA}x{ALTURA}")

canvas = tk.Canvas(root, width=LARGURA, height=ALTURA-40, bg="yellow")
canvas.pack(side="top", fill="both", expand=True)

frame_botoes = tk.Frame(root, bg="yellow", height=40)
frame_botoes.pack(side="bottom", fill="x")

btn = tk.Button(frame_botoes, text="Carregar ficheiro .csv", command=carregar_csv)
btn.pack(pady=5)

root.mainloop()

