import pymysql
from tkinter import messagebox
import database_setup

class Farmaco:
    def __init__(self, id, nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion):
        self.id = id
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.mg = mg
        self.fecha_elaboracion = fecha_elaboracion
        self.fecha_vencimiento = fecha_vencimiento
        self.presentacion = presentacion

    @staticmethod
    def connect_to_db():
        try:
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='',
                                         database='farmacia')
            return connection
        except Exception as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def crear(nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion):
        # Establecer conexión con la base de datos
        connection = database_setup.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("USE farmacia")

        # Insertar el nuevo fármaco en la base de datos
        cursor.execute("INSERT INTO Farmaco (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion) VALUES (%s, %s, %s, %s, %s, %s)",
                    (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion))
        connection.commit()

        messagebox.showinfo("Creación exitosa", "El fármaco ha sido creado correctamente.")

        # Cerrar cursor y conexión
        cursor.close()
        connection.close()

    @staticmethod
    def read_all():
        connection = Farmaco.connect_to_db()
        if connection:
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Farmaco")
            data = cursor.fetchall()

            farmacos = []

            for row in data:
                farmaco = Farmaco(*row)
                farmacos.append(farmaco)

            connection.close()
            return farmacos
        else:
            print("No se pudo conectar a la base de datos.")
            return []

    @staticmethod
    def editar(farmaco_id, nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion):
        # Establecer conexión con la base de datos
        connection = database_setup.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("USE farmacia")

        # Actualizar el fármaco en la base de datos
        cursor.execute("UPDATE Farmaco SET nombre = %s, laboratorio = %s, mg = %s, fecha_elaboracion = %s, fecha_vencimiento = %s, presentacion = %s WHERE id = %s", (nombre, laboratorio, mg, fecha_elaboracion, fecha_vencimiento, presentacion, farmaco_id))
        connection.commit()

        messagebox.showinfo("Actualización exitosa", "El fármaco ha sido actualizado correctamente.")

        # Cerrar cursor y conexión
        cursor.close()
        connection.close()


    @staticmethod
    def delete(farmaco_id):
        # Establecer conexión con la base de datos
        connection = database_setup.connect_to_db()
        cursor = connection.cursor()
        cursor.execute("USE farmacia")

        # Mostrar ventana de confirmación
        confirmation = messagebox.askyesno("Confirmar eliminación", "¿Estás seguro que deseas eliminar este fármaco?")
        if confirmation:
            # Eliminar el fármaco de la base de datos
            cursor.execute("DELETE FROM Farmaco WHERE id = %s", (farmaco_id,))
            connection.commit()

            messagebox.showinfo("Eliminación exitosa", "El fármaco ha sido eliminado correctamente.")

        # Cerrar cursor y conexión
        cursor.close()
        connection.close()