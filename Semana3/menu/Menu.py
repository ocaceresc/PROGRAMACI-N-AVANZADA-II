class Menu:
    def __init__(self, opciones):
        self.opciones = opciones

    def mostrar_menu(self):
        print("Seleccione una opción:")
        for i, opcion in enumerate(self.opciones):
            print(f"{i+1}. {opcion}")
        print(f"{len(self.opciones)+1}. Salir")
        opcion_elegida = int(input("Opción seleccionada: "))
        if opcion_elegida == len(self.opciones)+1:
            return None
        return opcion_elegida
