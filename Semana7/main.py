import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def generar_grafico_pertinente():
    escalafon = ['Instructor', 'Asistente', 'Agregado', 'Asociado']
    casos = [945, 698, 736, 590]
    plt.bar(escalafon, casos)
    plt.xlabel('Escalafón')
    plt.ylabel('Casos')
    plt.title('Clasificación de profesores por escalafón')
    plt.xticks(rotation=45)
    plt.show()


def generar_boxplot():

    np.random.seed(0)
    serie1 = np.random.normal(loc=750, scale=50, size=700)
    serie2 = np.random.normal(loc=900, scale=20, size=700)
    serie3 = np.random.normal(loc=500, scale=40, size=700)
    fig, ax = plt.subplots()
    ax.boxplot([serie1, serie2, serie3])
    ax.set_xticklabels(['Serie 1', 'Serie 2', 'Serie 3'])
    ax.set_ylabel('Valores')
    ax.set_title('Gráfico Boxplot')
    window = tk.Toplevel(root)
    window.wm_title('Gráfico Boxplot')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def generar_diagrama_dispercion():
    x = range(200)
    y = range(200) + np.random.randint(0, 20, 200)
    plt.scatter(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Diagrama de Dispersión')
    window = tk.Toplevel(root)
    window.wm_title('Diagrama de Dispersión')
    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def limpiar_ventanas():
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.destroy()


root = tk.Tk()
root.title("Semana 7")

btn_a = tk.Button(root, text="A - Gráfico 1", command=lambda: [limpiar_ventanas(), generar_grafico_pertinente()])
btn_a.pack()

btn_b = tk.Button(root, text="B - Gráfico Boxplot", command=lambda: [limpiar_ventanas(), generar_boxplot()])
btn_b.pack()

btn_d = tk.Button(root, text="C y D - Diagrama de Dispersión", command=lambda: [limpiar_ventanas(), generar_diagrama_dispercion()])
btn_d.pack()

footer_label = tk.Label(root, text="Desarrollado por Oscar Caceres C.")
footer_label.pack(side=tk.BOTTOM)

root.mainloop()
