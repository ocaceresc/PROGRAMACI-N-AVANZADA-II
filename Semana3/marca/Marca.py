class Marca:
    def __init__(self, nombre, porcentaje_aumento):
        self.nombre = nombre
        self.porcentaje_aumento = porcentaje_aumento

    def __str__(self):
        return f"{self.nombre} ({self.porcentaje_aumento}%)"
