from lente.Lente import Lente
from marca.Marca import Marca
from recubrimiento.Recubrimiento import Recubrimiento


class InterfazLente:
    def __init__(self):
        self.lente = None
        self.marcas = [Marca("Ray-Ban", 30),
                             Marca("Oakley", 25), Marca("Prada", 20)]
        self.recubrimientos = [Recubrimiento(
            "Anti-reflejo", 5), Recubrimiento("Fotocromático", 10)]

    def elegir_marca(self):
        print("Elige una marca:")
        for i, marca in enumerate(self.marcas):
            print(f"{i+1}. {marca}")
        opcion = int(input("Opción: "))
        marca_elegida = self.marcas[opcion-1]
        return marca_elegida

    def elegir_recubrimientos(self):
        print("Elige un recubrimiento:")
        for i, recubrimiento in enumerate(self.recubrimientos):
            print(f"{i+1}. {recubrimiento}")
        opcion = int(input("Opción: "))
        return self.recubrimientos[opcion-1]

    def __mul__(self):
        costo = float(input("Ingrese el costo del lente: "))
        marca = self.elegir_marca()
        recubrimiento = self.elegir_recubrimientos()

        precio_final = costo + (costo * marca.porcentaje_aumento / 100) + \
                                (costo * recubrimiento.porcentaje_descuento / 100)

        print("{:<30} {}".format("---------------------", "---------------------"))
        print("{:<30} {}".format("Valor Lente:", f"${costo}"))
        print("{:<30} {}".format(f"Marca ({marca.nombre}):", f"${marca.porcentaje_aumento}"))
        print("{:<20} {}".format(f"Recubrimiento ({recubrimiento.nombre}):", f"${recubrimiento.porcentaje_descuento}"))
        print("{:<30} {}".format("---------------------", "---------------------"))
        print("{:<30} {}".format("Precio Final:", f"${precio_final}"))
