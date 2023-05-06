import mysql.connector
import datetime
import tkinter as tk
from tkinter import ttk

# Conexión a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)


# Crear la base de datos si no existe
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")
mycursor.execute("USE biblioteca")

# Crear la tabla de libros si no existe
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS libros (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255),
        codigo VARCHAR(255),
        ano_publicacion INT,
        autor VARCHAR(255),
        editorial VARCHAR(255)
    )
""")


# Funciones para realizar operaciones en la base de datos
def crear_bd():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca")
    resultado_label.configure(text="Base de datos creada \U0001F44D")

def insertar_libros():
    libros = [
        ('Cien años de soledad', '978-0307474728', 1967, 'Gabriel García Márquez', 'Editorial Sudamericana'),
        ('La ciudad y los perros', '978-8466338187', 1962, 'Mario Vargas Llosa', 'Seix Barral'),
        ('Pedro Páramo', '978-9681609391', 1955, 'Juan Rulfo', 'Fondo de Cultura Económica'),
        ('El Aleph', '978-0307950968', 1949, 'Jorge Luis Borges', 'Emecé Editores'),
        ('Rayuela', '978-8466306476', 1963, 'Julio Cortázar', 'Alianza Editorial'),
        ('La tregua', '978-8423337346', 1960, 'Mario Benedetti', 'Destino'),
        ('Doña Bárbara', '978-8491051019', 1929, 'Rómulo Gallegos', 'Alfaguara'),
        ('El llano en llamas', '978-9708100217', 1953, 'Juan Rulfo', 'Fondo de Cultura Económica'),
        ('La casa de los espíritus', '978-9507315152', 1982, 'Isabel Allende', 'Editorial Sudamericana'),
        ('Los pasos perdidos', '978-8432211676', 1953, 'Alejo Carpentier', 'Seix Barral')
    ]

    for libro in libros:
      mycursor.execute("INSERT INTO libros (titulo, codigo, ano_publicacion, autor, editorial) VALUES (%s, %s, %s, %s, %s)", libro)

    mydb.commit()
    resultado_label.configure(text="Libros insertados \U0001F4D7")

def eliminar_libros_antiguos():
    year = datetime.datetime.now().year
    sql = "DELETE FROM libros WHERE ano_publicacion < %s"
    val = (2000,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount > 0:
        resultado_label.configure(text=str(mycursor.rowcount) + " libros eliminados \U0001F5D1")
    else:
        resultado_label.configure(text="No se encontraron libros antiguos \U0001F615")

def crear_tabla():
    mycursor.execute("CREATE TABLE IF NOT EXISTS libros (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255), codigo VARCHAR(255), ano_publicacion INT(4), autor VARCHAR(255), editorial VARCHAR(255))")
    resultado_label.configure(text="Tabla creada \U0001F44D")

def listar_libros_actuales():
    sql = "SELECT * FROM libros "
    mycursor.execute(sql)
    libros = mycursor.fetchall()

    # Crear la tabla y sus cabeceras
    tabla = ttk.Treeview(root, columns=("titulo", "codigo", "ano_publicacion", "autor", "editorial"))
    tabla.heading("#0", text="ID")
    tabla.heading("titulo", text="Título")
    tabla.heading("codigo", text="Código")
    tabla.heading("ano_publicacion", text="Año de Publicación")
    tabla.heading("autor", text="Autor")
    tabla.heading("editorial", text="Editorial")

    # Insertar los datos en la tabla
    for libro in libros:
        tabla.insert("", tk.END, text=libro[0], values=(libro[1], libro[2], libro[3], libro[4], libro[5]))

    tabla.pack()

root = tk.Tk()

root.geometry("1200x600")
root.title("Biblioteca")

crear_bd_button = tk.Button(root, text="Crear BD", command=crear_bd)
crear_bd_button.pack()

crear_tabla_button = tk.Button(root, text="Crear tabla", command=crear_tabla)
crear_tabla_button.pack()

insertar_libros_button = tk.Button(root, text="Insertar libros", command=insertar_libros)
insertar_libros_button.pack()

eliminar_libros_antiguos_button = tk.Button(root, text="Eliminar libros antiguos", command=eliminar_libros_antiguos)
eliminar_libros_antiguos_button.pack()

listar_libros_actuales_button = tk.Button(root, text="Listar libros actuales", command=listar_libros_actuales)
listar_libros_actuales_button.pack()

resultado_label = tk.Label(root, text="")
resultado_label.pack()

footer_label = tk.Label(root, text="Oscar Caceres - IACC 2023")
footer_label.pack(side="bottom")

root.mainloop()
