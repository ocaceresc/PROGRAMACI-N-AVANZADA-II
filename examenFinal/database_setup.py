import pymysql
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import subprocess

def connect_to_db():
    try:
        # Establecer conexión con la base de datos
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='')
        
        return connection
    except Exception as e:
        print(f"Error: {e}")
        return None

def create_database():
    connection = connect_to_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS farmacia")
        cursor.execute("USE farmacia")  # Para usar la base de datos 'farmacia'
        connection.commit()
        connection.close()
        return True
    else:
        return False

def cargar_datos():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("USE farmacia")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Farmaco (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255),
            laboratorio VARCHAR(255),
            mg INT,
            fecha_elaboracion DATE,
            fecha_vencimiento DATE,
            presentacion VARCHAR(255)
        )
    ''')

    fármacos_de_ejemplo = [
        ('Paracetamol', 'Laboratorio A', 500, datetime.strptime('2023-01-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Capsula'),
        ('Ibuprofeno', 'Laboratorio B', 200, datetime.strptime('2023-02-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Capsula'),
        ('Amoxicilina', 'Laboratorio A', 500, datetime.strptime('2023-03-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Capsula'),
        ('Azitromicina', 'Laboratorio B', 500, datetime.strptime('2023-04-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Capsula'),
        ('Diclofenaco', 'Laboratorio C', 50, datetime.strptime('2023-05-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Capsula'),
        ('Loratadina', 'Laboratorio D', 10, datetime.strptime('2023-06-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Jarabe'),
        ('Ranitidina', 'Laboratorio E', 150, datetime.strptime('2023-07-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Jarabe'),
        ('Omeprazol', 'Laboratorio F', 20, datetime.strptime('2023-08-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Jarabe'),
        ('Fluconazol', 'Laboratorio G', 150, datetime.strptime('2023-09-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Jarabe'),
        ('Metformina', 'Laboratorio H', 850, datetime.strptime('2023-10-01', '%Y-%m-%d'), datetime.strptime('2025-12-31', '%Y-%m-%d'), 'Capsula'),
    ]

    try:
        cursor.executemany('''
            INSERT INTO Farmaco (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', fármacos_de_ejemplo)

        connection.commit()
        print("Los datos se cargaron correctamente.")
    except Exception as e:
        connection.rollback()
        print(f"Error al cargar los datos: {e}")
    
    cursor.close()
    connection.close()
    
    
def initialize_db_button_click(window):
    if create_database():
        cargar_datos()
        messagebox.showinfo("Información", "La base de datos ha sido inicializada.")
        window.destroy()
    else:
        messagebox.showwarning("Advertencia", "No se pudo establecer la conexión con la base de datos.")

def close_window(window):
    window.destroy()

def check_connection():
    window = Tk()
    window.title("Verificación de conexión de BD")

    status_label = Label(window, text="Estado de la conexión: ", font=("Arial", 14))
    status_label.pack()

    emoji_label = Label(window, text="", font=("Arial", 18))
    emoji_label.pack()

    connection = connect_to_db()
    if connection:
        emoji_label.config(text="\U0001F7E2")  # Emoji verde de círculo
        initialize_db_button = Button(window, text="Inicializar BD", command=lambda: initialize_db_button_click(window))
        initialize_db_button.pack()
    else:
        emoji_label.config(text="\U0001F534")  # Emoji rojo de círculo
        
    close_button = Button(window, text="Cerrar", command=lambda: close_window(window))
    close_button.pack()       

    window.mainloop()

if __name__ == "__main__":
    check_connection()