from libreria.libreria import Libreria
from libro.libro import Libro
import time

# Crear una instancia de la librería
libreria = Libreria()

print("Agregando Libros...")
for i in range(4):
    time.sleep(1)  # Esperar 1 segundo
    print("#", end="", flush=True)  # Imprimir una barra de progreso

print("\nLibros cargados exitosamente!\n")

# Crear instancias de la clase Libro y añadirlos a la lista de la librería
libro1 = Libro("La Casa de los Espíritus", "Isabel Allende", "863 A435c", "Novela", "Editorial Sudamericana", "1982", "Chile")
libreria.anadir_libro(libro1)

libro2 = Libro("Los detectives salvajes", "Roberto Bolaño", "863.64 B694d", "Novela", "Editorial Anagrama", "1998", "Chile")
libreria.anadir_libro(libro2)

libro3 = Libro("Poemas y antipoemas", "Nicanor Parra", "861.62 P269p", "Poesía", "Editorial Universitaria", "1954", "Chile")
libreria.anadir_libro(libro3)

libro4 = Libro("La ciudad ausente", "Ricardo Piglia", "863 P634c", "Novela", "Editorial Anagrama", "1992", "Chile")
libreria.anadir_libro(libro4)

libro5 = Libro("La muerte y la doncella", "Ariel Dorfman", "863 D692m", "Drama", "Editorial Andrés Bello", "1990", "Chile")
libreria.anadir_libro(libro5)

print("Creando Listado de Libros...")
for i in range(4):
    time.sleep(1)  # Esperar 1 segundo
    print("#", end="", flush=True)  # Imprimir una barra de progreso

print("\nLibros cargados exitosamente!\n")

# Imprimir el listado de libros
libreria.imprimir_lista_libros()
