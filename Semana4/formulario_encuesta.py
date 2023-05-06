import tkinter as tk

def imprimir_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    rut = entry_rut.get()
    telefono = entry_telefono.get()
    sexo = var_sexo.get()
    esta_de_acuerdo = var_acuerdo.get()
    
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("RUT:", rut)
    print("Teléfono:", telefono)
    print("Sexo:", sexo)
    print("¿Está de acuerdo con la construcción de la escuela en su comunidad?:", esta_de_acuerdo)

ventana = tk.Tk()
ventana.title("Encuesta sobre la construcción de una escuela")
ventana.geometry("500x300")

ventana.configure(bg="#F5F5F5")

label_nombre = tk.Label(ventana, text="Nombre:", bg="#F5F5F5")
label_nombre.grid(row=0, column=0)
entry_nombre = tk.Entry(ventana, bg="#FFFFFF")
entry_nombre.grid(row=0, column=1)

label_apellido = tk.Label(ventana, text="Apellido:", bg="#F5F5F5")
label_apellido.grid(row=1, column=0)
entry_apellido = tk.Entry(ventana, bg="#FFFFFF")
entry_apellido.grid(row=1, column=1)

label_rut = tk.Label(ventana, text="RUT:", bg="#F5F5F5")
label_rut.grid(row=2, column=0)
entry_rut = tk.Entry(ventana, bg="#FFFFFF")
entry_rut.grid(row=2, column=1)

label_telefono = tk.Label(ventana, text="Teléfono:", bg="#F5F5F5")
label_telefono.grid(row=3, column=0)
entry_telefono = tk.Entry(ventana, bg="#FFFFFF")
entry_telefono.grid(row=3, column=1)

label_sexo = tk.Label(ventana, text="Sexo:", bg="#F5F5F5")
label_sexo.grid(row=4, column=0)
var_sexo = tk.StringVar()
opcion_masculino = tk.Radiobutton(ventana, text="Masculino", variable=var_sexo, value="Masculino", bg="#F5F5F5")
opcion_masculino.grid(row=4, column=1)
opcion_femenino = tk.Radiobutton(ventana, text="Femenino", variable=var_sexo, value="Femenino", bg="#F5F5F5")
opcion_femenino.grid(row=4, column=2)

label_acuerdo = tk.Label(ventana, text="¿Está de acuerdo con la\n construcción de la escuela\n en su comunidad?")
label_acuerdo.configure(bg="#F5F5F5")
label_acuerdo.grid(row=5, column=0)
var_acuerdo = tk.StringVar()
opcion_si = tk.Radiobutton(ventana, text="Sí", variable=var_acuerdo, value="Sí", bg="#F5F5F5")
opcion_si.grid(row=5, column=1)
opcion_no = tk.Radiobutton(ventana, text="No", variable=var_acuerdo, value="No", bg="#F5F5F5")
opcion_no.grid(row=5, column=2)

boton_enviar = tk.Button(ventana, text="Enviar", command=imprimir_datos)
boton_enviar.grid(row=6, column=1, pady=10)

ventana.mainloop()
