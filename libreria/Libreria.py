class Libreria:
    def __init__(self):
        self.lista_libros = []
    
    def anadir_libro(self, libro):
        self.lista_libros.append(libro)
    
    def imprimir_lista_libros(self):
        if len(self.lista_libros) == 0:
            print("La librería no tiene libros registrados.")
        else:
            for libro in self.lista_libros:
                print("Nombre: " + libro.nombre)
                print("Autor: " + libro.autor)
                print("Cota: " + libro.cota)
                print("Género: " + libro.genero)
                print("Editorial: " + libro.editorial)
                print("Fecha de edición: " + libro._Libro__fecha_edicion) # Atributo privado
                print("País de edición: " + libro.pais_edicion)
                print()
