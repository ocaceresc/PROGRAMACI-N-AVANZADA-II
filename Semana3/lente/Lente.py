class Lente:
    def __init__(self, costo, marca, precio_base):
        self.costo = costo
        self.marca = marca
        self.precio_base = precio_base

    def calcular_precio_venta(self, porcentaje_aumento, recubrimiento):
        precio_venta = self.precio_base * (1 + porcentaje_aumento/100) * (1 + recubrimiento/100)
        return round(precio_venta, 2)

    def __str__(self):
        return f"Lente: costo={self.costo}, marca={self.marca}, precio_base={self.precio_base}"
    