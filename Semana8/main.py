import tkinter as tk
from tkinter import messagebox
import csv

def calcular_impuesto():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    rut = rut_entry.get()
    sexo = sexo_var.get()
    ingreso = ingreso_entry.get()

    if nombre == "" or apellido == "" or rut == "" or sexo == "" or ingreso == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
        return

    try:
        ingreso = float(ingreso)
    except ValueError:
        messagebox.showerror("Error", "El valor ingresado en el campo 'Ingreso' no es válido.")
        return

    impuesto = ingreso * 0.2
    impuesto_entry.configure(text=f"{impuesto:.1f}")

def exportar_datos():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    rut = rut_entry.get()
    sexo = sexo_var.get()
    ingreso = ingreso_entry.get()
    impuesto = impuesto_entry.cget("text")

    if nombre == "" or apellido == "" or rut == "" or sexo == "" or ingreso == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
        return
    
    if impuesto == "":
        messagebox.showerror("Error", "Debe calcular el impuesto antes de exportar los datos.")
        return

    try:
        ingreso = float(ingreso)
    except ValueError:
        messagebox.showerror("Error", "El valor ingresado en el campo 'Ingreso' no es válido.")
        return

    # Guardar los datos en un archivo CSV
    datos = [('-----------------------------'),('Campo', 'Valor'),('nombre', nombre),('apellido', apellido),('rut', rut),('sexo', sexo),('ingreso', ingreso), ('impuesto', impuesto)]
    with open("datos_impuestos.csv", "a", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)

    messagebox.showinfo("Éxito", "Los datos han sido enviados al Departamento de Impuestos.")
    
    limpiar_formulario()
    
def limpiar_formulario():
    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    rut_entry.delete(0, tk.END)
    ingreso_entry.delete(0, tk.END)
    impuesto_entry.configure(text="")

    # Restablecer la selección predeterminada del botón de sexo
    sexo_var.set("Masculino")


window = tk.Tk()
window.title("Calculadora de Impuestos")

nombre_label = tk.Label(window, text="Nombre:")
nombre_label.pack()
nombre_entry = tk.Entry(window)
nombre_entry.pack()

apellido_label = tk.Label(window, text="Apellido:")
apellido_label.pack()
apellido_entry = tk.Entry(window)
apellido_entry.pack()

rut_label = tk.Label(window, text="RUT:")
rut_label.pack()
rut_entry = tk.Entry(window)
rut_entry.pack()

sexo_label = tk.Label(window, text="Sexo:")
sexo_label.pack()
sexo_var = tk.StringVar()
sexo_var.set("Masculino")
sexo_radiobutton1 = tk.Radiobutton(window, text="Masculino", variable=sexo_var, value="Masculino")
sexo_radiobutton1.pack()
sexo_radiobutton2 = tk.Radiobutton(window, text="Femenino", variable=sexo_var, value="Femenino")
sexo_radiobutton2.pack()
sexo_radiobutton3 = tk.Radiobutton(window, text="Otro", variable=sexo_var, value="Otro")
sexo_radiobutton3.pack()

ingreso_label = tk.Label(window, text="Ingreso:")
ingreso_label.pack()
ingreso_entry = tk.Entry(window)
ingreso_entry.pack()

calcular_button = tk.Button(window, text="Calcular Impuesto", command=calcular_impuesto)
calcular_button.pack()

exportar_button = tk.Button(window, text="Exportar Datos", command=exportar_datos)
exportar_button.pack()

impuesto_label = tk.Label(window, text="Impuesto:")
impuesto_label.pack()
impuesto_entry = tk.Label(window, text="", fg="red")
impuesto_entry.pack()

limpiar_button = tk.Button(window, text="Limpiar", command=limpiar_formulario)
limpiar_button.pack()

footer_label = tk.Label(window, text="Desarrollado por Oscar Caceres C.")
footer_label.pack(side=tk.BOTTOM)

window.mainloop()
