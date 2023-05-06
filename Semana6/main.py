import pandas as pd
import tkinter as tk
from tkinter import ttk
import pymysql.cursors
import config

root = tk.Tk()
root.title('Semana 6')

connection = pymysql.connect(host=config.DB_HOST,
                             user=config.DB_USER,
                             password=config.DB_PASSWORD,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def crear_bd():
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW DATABASES LIKE '{config.DB_NAME}'")
            resultado = cursor.fetchone()
            if resultado:
                mensaje.config(text="La base de datos ya existe \U0001F610")
            else:
                cursor.execute(f"CREATE DATABASE {config.DB_NAME}")
                cursor.execute(f"USE {config.DB_NAME}")
                connection.commit()
                mensaje.config(text="Base de datos creada correctamente \U0001F44D")
    except Exception as e:
        mensaje.config(text=f"Error al crear la base de datos \U0001F630: {str(e)}")

def tabla_existe():
    with connection.cursor() as cursor:
        cursor.execute(f"SHOW TABLES LIKE 'medicos'")
        resultado = cursor.fetchone()
    return bool(resultado)

def seleccionar_bd():
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW DATABASES LIKE '{config.DB_NAME}'")
            resultado = cursor.fetchone()
            if resultado:
                cursor.execute(f"USE {config.DB_NAME}")
            else:
                mensaje.config(text="La base de datos no existe, por favor crea la base de datos primero \U0001F630")
                return False
    except Exception as e:
        mensaje.config(text=f"Error al seleccionar la base de datos \U0001F630: {str(e)}")
        return False
    return True


def limpiar_tabla():
    tabla_datos.delete(*tabla_datos.get_children())
    mensaje.config(text="Tabla limpiada \U0001F5D1")

def obtener_datos():
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM medicos")
        datos = cursor.fetchall()
        df = pd.DataFrame(datos)
        hombres = df[df['sexo'] == 'M']
        mujeres = df[df['sexo'] == 'F']
        return hombres, mujeres

def crear_tabla():
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW TABLES LIKE 'medicos'")
            resultado = cursor.fetchone()
            if resultado:
                mensaje.config(text="La tabla ya existe \U0001F610")
            else:
                sql = f"""CREATE TABLE medicos (
                        id INT(11) NOT NULL AUTO_INCREMENT,
                        nombre VARCHAR(255) NOT NULL,
                        apellido VARCHAR(255) NOT NULL,
                        rut VARCHAR(255) NOT NULL,
                        sexo VARCHAR(255) NOT NULL,
                        direccion VARCHAR(255) NOT NULL,
                        edad INT(11) NOT NULL,
                        PRIMARY KEY (id)
                        )"""
                cursor.execute(sql)
                connection.commit()
                mensaje.config(text="Tabla creada correctamente \U0001F44D")
    except:
        mensaje.config(text="Error al crear la tabla \U0001F630")

def insertar_datos():
    if not seleccionar_bd():
        return
    if not tabla_existe():
        mensaje.config(text="La tabla no existe. Por favor, crea la tabla antes de insertar datos \U0001F630")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) AS total FROM medicos")
            resultado = cursor.fetchone()
            if resultado['total'] > 0:
                mensaje.config(text="Los datos ya fueron insertados \U0001F610")
            else:
                sql = "INSERT INTO medicos (nombre, apellido, rut, sexo, direccion, edad) VALUES (%s, %s, %s, %s, %s, %s)"
                val = [("Juan", "Pérez", "12.345.678-9", "M", "Calle Falsa 123", 30),
                       ("Pedro", "González", "23.456.789-0", "M", "Avenida Real 456", 45),
                       ("María", "Hernández", "34.567.890-1", "F", "Plaza Mayor 789", 22),
                       ("Ana", "García", "45.678.901-2", "F", "Boulevard Central 012", 28),
                       ("Luis", "López", "56.789.012-3", "M", "Calle del Sol 345", 50)
                      ]
                cursor.executemany(sql, val)
                connection.commit()
                mensaje.config(text="Datos insertados correctamente \U0001F44D")
    except Exception as e:
        mensaje.config(text=f"Error al insertar datos \U0001F630: {str(e)}")

def filtrar_datos(genero=None):
    if not seleccionar_bd():
        return
    hombres, mujeres = obtener_datos()

    if genero == 'M':
        datos_filtrados = hombres
        mensaje.config(text="Mostrando Hombres \U0001F468")
    elif genero == 'F':
        datos_filtrados = mujeres
        mensaje.config(text="Mostrando Mujeres \U0001F469")
    else:
        datos_filtrados = pd.concat([hombres, mujeres])
        mensaje.config(text="Mostrando Todos \U0001F64C")

    tabla_datos.delete(*tabla_datos.get_children())

    for index, row in datos_filtrados.iterrows():
        tabla_datos.insert('', index, text='', values=(row['nombre'], row['apellido'], row['rut'], row['sexo'], row['direccion'], row['edad']))

boton_hombres = tk.Button(root, text='Mostrar Hombres', command=lambda: filtrar_datos('M'))
boton_mujeres = tk.Button(root, text='Mostrar Mujeres', command=lambda: filtrar_datos('F'))
boton_todos = tk.Button(root, text='Mostrar Todos', command=lambda: filtrar_datos())
boton_crear_bd = tk.Button(root, text='Crear base de datos', command=crear_bd)
boton_crear_tabla = tk.Button(root, text='Crear tabla', command=crear_tabla)
boton_insertar_datos = tk.Button(root, text='Insertar datos', command=insertar_datos)
boton_salir = tk.Button(root, text='Salir', command=root.quit)
boton_limpiar = tk.Button(root, text='Limpiar Tabla', command=limpiar_tabla)

mensaje = tk.Label(root, text='')

boton_crear_bd.grid(row=0, column=0, padx=10, pady=10)
boton_crear_tabla.grid(row=1, column=0, padx=10, pady=10)
boton_insertar_datos.grid(row=2, column=0, padx=10, pady=10)
boton_salir.grid(row=1, column=2, padx=10, pady=10)
boton_limpiar.grid(row=2, column=2, padx=10, pady=10)
mensaje.grid(row=4, column=0, columnspan=4)
boton_hombres.grid(row=0, column=1, padx=10, pady=10)
boton_mujeres.grid(row=1, column=1, padx=10, pady=10)
boton_todos.grid(row=2, column=1, padx=10, pady=10)

tabla_datos = ttk.Treeview(root, columns=('Nombre', 'Apellido', 'RUT', 'Sexo', 'Dirección', 'Edad'))
tabla_datos.heading('#0', text='')
tabla_datos.heading('Nombre', text='Nombre')
tabla_datos.heading('Apellido', text='Apellido')
tabla_datos.heading('RUT', text='RUT')
tabla_datos.heading('Sexo', text='Sexo')
tabla_datos.heading('Dirección', text='Dirección')
tabla_datos.heading('Edad', text='Edad')
tabla_datos.column('#0', width=0, stretch='no')
tabla_datos.column('Nombre', width=100)
tabla_datos.column('Apellido', width=100)
tabla_datos.column('RUT', width=100)
tabla_datos.column('Sexo', width=50)
tabla_datos.column('Dirección', width=200)
tabla_datos.column('Edad', width=50)
tabla_datos.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
