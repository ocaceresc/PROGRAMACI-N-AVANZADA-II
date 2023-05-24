# Proyecto Farmacia

Este proyecto es una aplicación de gestión de fármacos para una farmacia. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los fármacos almacenados en una base de datos MySQL.

## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instalados los siguientes componentes:

- Python 3.x: [Descargar e instalar Python](https://www.python.org/downloads/)
- MySQL Server: [Descargar e instalar MySQL Server](https://dev.mysql.com/downloads/mysql/)

## Instalación

Sigue estos pasos para configurar el entorno y ejecutar el proyecto:

1. Clona el repositorio o descarga los archivos del proyecto.
2. Abre una terminal o línea de comandos y navega hasta el directorio del proyecto.
3. Instala las dependencias del proyecto: `pip install -r requirements.txt`.
4. Configura la base de datos
5. Ejecuta el proyecto: `python -u main.py`.
6. Se abrira una ventana para verificar la conexión y crear la base de datos necesaria. Esto abrirá una ventana que mostrará el resultado de la conexión.

Si la conexión se establece correctamente y la base de datos se crea exitosamente, se va a cerrar la ventana de verificación de conexión.

## Uso

La aplicación abrirá una ventana principal con una tabla que muestra los fármacos almacenados en la base de datos. Desde esta ventana, puedes realizar las siguientes operaciones:

- Crear un nuevo fármaco: Haz clic en el botón "Crear" y completa el formulario en la ventana emergente. Luego, haz clic en "Guardar" para agregar el nuevo fármaco a la base de datos.
- Editar un fármaco existente: Haz clic en el botón "Editar" correspondiente a un fármaco en la tabla. Se abrirá una ventana emergente con los detalles del fármaco. Realiza los cambios deseados y haz clic en "Guardar" para actualizar el fármaco en la base de datos.
- Eliminar un fármaco: Haz clic en el botón "Eliminar" correspondiente a un fármaco en la tabla. Se mostrará una ventana de confirmación, donde podrás confirmar o cancelar la eliminación del fármaco.
