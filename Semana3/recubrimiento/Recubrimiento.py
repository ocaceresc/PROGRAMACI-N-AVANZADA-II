class Recubrimiento:
    def __init__(self, nombre, porcentaje_descuento):
        self.nombre = nombre
        self.porcentaje_descuento = porcentaje_descuento

    def __str__(self):
        return f"{self.nombre} ({self.porcentaje_descuento}%)"
