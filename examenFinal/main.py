from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
import database_setup
import datetime
from farmaco import Farmaco

def abrir_ventana_edicion(farmaco,root, table_frame):
    ventana_edicion = Toplevel()
    ventana_edicion.title("Editar Fármaco")

    # Campos de entrada para cada atributo del fármaco
    Label(ventana_edicion, text="ID:").grid(row=0, column=0)
    id_label = Label(ventana_edicion, text=farmaco.id)
    id_label.grid(row=0, column=1)

    Label(ventana_edicion, text="Nombre:").grid(row=1, column=0)
    nombre_entry = Entry(ventana_edicion)
    nombre_entry.grid(row=1, column=1)
    nombre_entry.insert(0, farmaco.nombre)

    Label(ventana_edicion, text="Laboratorio:").grid(row=2, column=0)
    laboratorio_entry = Entry(ventana_edicion)
    laboratorio_entry.grid(row=2, column=1)
    laboratorio_entry.insert(0, farmaco.laboratorio)

    Label(ventana_edicion, text="mg:").grid(row=3, column=0)
    mg_entry = Entry(ventana_edicion)
    mg_entry.grid(row=3, column=1)
    mg_entry.insert(0, farmaco.mg)

    Label(ventana_edicion, text="Fecha de Elaboración:").grid(row=4, column=0)
    fecha_elaboracion_entry = DateEntry(ventana_edicion, date_pattern='dd/mm/yyyy')
    fecha_elaboracion_entry.grid(row=4, column=1)
    fecha_elaboracion_entry.set_date(farmaco.fecha_elaboracion)

    Label(ventana_edicion, text="Fecha de Vencimiento:").grid(row=5, column=0)
    fecha_vencimiento_entry = DateEntry(ventana_edicion, date_pattern='dd/mm/yyyy')
    fecha_vencimiento_entry.grid(row=5, column=1)
    fecha_vencimiento_entry.set_date(farmaco.fecha_vencimiento)

    Label(ventana_edicion, text="Presentación:").grid(row=6, column=0)
    presentacion_combobox = ttk.Combobox(ventana_edicion, values=["Capsula", "Jarabe"])
    presentacion_combobox.grid(row=6, column=1)
    presentacion_combobox.set(farmaco.presentacion)

    # Función para guardar los cambios
    def guardar_edicion():
        # Obtener los nuevos valores del formulario
        nuevo_nombre = nombre_entry.get()
        nuevo_laboratorio = laboratorio_entry.get()
        nuevo_mg = mg_entry.get()
        nueva_fecha_elaboracion = fecha_elaboracion_entry.get()
        nueva_fecha_elaboracion = datetime.datetime.strptime(nueva_fecha_elaboracion, '%d/%m/%Y').strftime('%Y-%m-%d')
        nueva_fecha_vencimiento = fecha_vencimiento_entry.get()
        nueva_fecha_vencimiento = datetime.datetime.strptime(nueva_fecha_vencimiento, '%d/%m/%Y').strftime('%Y-%m-%d')
        nueva_presentacion = presentacion_combobox.get()

        # Llamar a la función editar en farmaco.py
        Farmaco.editar(farmaco.id, nuevo_nombre, nuevo_laboratorio, nuevo_mg, nueva_fecha_elaboracion, nueva_fecha_vencimiento, nueva_presentacion)

        # Cerrar la ventana de edición
        ventana_edicion.destroy()

        # Refrescar la tabla
        root.withdraw()
        table_frame.destroy()
        cargar_datos()

    # Botón "Guardar"
    guardar_button = Button(ventana_edicion, text="Guardar", command=guardar_edicion)
    guardar_button.grid(row=7, column=0, columnspan=2)

    cancelar_button = Button(ventana_edicion, text="Cancelar", command=ventana_edicion.destroy)
    cancelar_button.grid(row=8, column=0, columnspan=2)

def abrir_ventana_creacion(root, table_frame):
    ventana_creacion = Toplevel()
    ventana_creacion.title("Crear Fármaco")

    # Campos de entrada para cada atributo del fármaco
    Label(ventana_creacion, text="Nombre:").grid(row=0, column=0)
    nombre_entry = Entry(ventana_creacion)
    nombre_entry.grid(row=0, column=1)

    Label(ventana_creacion, text="Laboratorio:").grid(row=1, column=0)
    laboratorio_entry = Entry(ventana_creacion)
    laboratorio_entry.grid(row=1, column=1)

    Label(ventana_creacion, text="mg:").grid(row=2, column=0)
    mg_entry = Entry(ventana_creacion)
    mg_entry.grid(row=2, column=1)

    Label(ventana_creacion, text="Fecha de Elaboración:").grid(row=3, column=0)
    fecha_elaboracion_entry = DateEntry(ventana_creacion, date_pattern='dd/mm/yyyy')
    fecha_elaboracion_entry.grid(row=3, column=1)

    Label(ventana_creacion, text="Fecha de Vencimiento:").grid(row=4, column=0)
    fecha_vencimiento_entry = DateEntry(ventana_creacion, date_pattern='dd/mm/yyyy')
    fecha_vencimiento_entry.grid(row=4, column=1)

    Label(ventana_creacion, text="Presentación:").grid(row=5, column=0)
    presentacion_combobox = ttk.Combobox(ventana_creacion, values=["Capsula", "Jarabe"])
    presentacion_combobox.grid(row=5, column=1)

    # Función para guardar el nuevo fármaco
    def guardar_creacion():
        # Obtener los valores del formulario
        nuevo_nombre = nombre_entry.get()
        nuevo_laboratorio = laboratorio_entry.get()
        nuevo_mg = mg_entry.get()
        nueva_fecha_elaboracion = fecha_elaboracion_entry.get()
        nueva_fecha_elaboracion = datetime.datetime.strptime(nueva_fecha_elaboracion, '%d/%m/%Y').strftime('%Y-%m-%d')
        nueva_fecha_vencimiento = fecha_vencimiento_entry.get()
        nueva_fecha_vencimiento = datetime.datetime.strptime(nueva_fecha_vencimiento, '%d/%m/%Y').strftime('%Y-%m-%d')
        nueva_presentacion = presentacion_combobox.get()

        # Llamar a la función crear en farmaco.py
        Farmaco.crear(nuevo_nombre, nuevo_laboratorio, nuevo_mg, nueva_fecha_elaboracion, nueva_fecha_vencimiento, nueva_presentacion)

        # Cerrar la ventana de creación
        ventana_creacion.destroy()

        # Refrescar la tabla
        root.withdraw()
        table_frame.destroy()
        cargar_datos()

    # Botón "Guardar"
    guardar_button = Button(ventana_creacion, text="Guardar", command=guardar_creacion)
    guardar_button.grid(row=6, column=0, columnspan=2)

    cancelar_button = Button(ventana_creacion, text="Cancelar", command=ventana_creacion.destroy)
    cancelar_button.grid(row=7, column=0, columnspan=2)


def cargar_datos():
    # Obtener los datos de los fármacos
    farmacos = Farmaco.read_all()

    # Crear ventana de tkinter
    root = Tk()
    root.title("Farmacia")

    # Crear la tabla
    table_frame = Frame(root)
    table_frame.pack()

    Label(table_frame, text="ID").grid(row=0, column=0)
    Label(table_frame, text="Nombre").grid(row=0, column=1)
    Label(table_frame, text="Laboratorio").grid(row=0, column=2)
    Label(table_frame, text="mg").grid(row=0, column=3)
    Label(table_frame, text="Fecha de Elaboración").grid(row=0, column=4)
    Label(table_frame, text="Fecha de Vencimiento").grid(row=0, column=5)
    Label(table_frame, text="Presentación").grid(row=0, column=6)

    # Mostrar los datos en la tabla
    for i, farmaco in enumerate(farmacos):
        Label(table_frame, text=farmaco.id).grid(row=i+1, column=0)
        Label(table_frame, text=farmaco.nombre).grid(row=i+1, column=1)
        Label(table_frame, text=farmaco.laboratorio).grid(row=i+1, column=2)
        Label(table_frame, text=farmaco.mg).grid(row=i+1, column=3)
        Label(table_frame, text=farmaco.fecha_elaboracion).grid(row=i+1, column=4)
        Label(table_frame, text=farmaco.fecha_vencimiento).grid(row=i+1, column=5)
        Label(table_frame, text=farmaco.presentacion).grid(row=i+1, column=6)
        Label(table_frame, text="Acciones").grid(row=0, column=7)
        edit_button = Button(table_frame, text="Editar", command=lambda index=i: abrir_ventana_edicion(farmacos[index], root, table_frame))
        edit_button.grid(row=i+1, column=7)

        delete_button = Button(table_frame, text="Eliminar", command=lambda index=i: delete_farmaco(farmacos[index].id, root, table_frame))
        delete_button.grid(row=i+1, column=8)

    # Botones de CRUD
    create_button = Button(root, text="Crear", command=lambda: abrir_ventana_creacion(root, table_frame))
    create_button.pack()


    root.mainloop()

def delete_farmaco(farmaco_id, root, table_frame):
    Farmaco.delete(farmaco_id)
    root.withdraw()
    table_frame.destroy()
    cargar_datos()
    

def main():
    # Verificar la base de datos
    database_setup.check_connection()

    cargar_datos()

if __name__ == "__main__":
    main()
