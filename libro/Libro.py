class Libro:
    def __init__(self, nombre, autor, cota, genero, editorial, fecha_edicion, pais_edicion):
        self.nombre = nombre
        self.autor = autor
        self.cota = cota
        self.genero = genero
        self.editorial = editorial
        self.__fecha_edicion = fecha_edicion
        self.pais_edicion = pais_edicion
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_autor(self):
        return self.autor
    
    def obtener_cota(self):
        return self.cota
    
    def obtener_genero(self):
        return self.genero
    
    def obtener_editorial(self):
        return self.editorial
    
    def obtener_fecha_edicion(self):
        return self.__fecha_edicion
    
    def obtener_pais_edicion(self):
        return self.pais_edicion
