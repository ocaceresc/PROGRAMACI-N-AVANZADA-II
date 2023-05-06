from interfaz_lente import InterfazLente

def main():
    try:
        interfaz_lente = InterfazLente()
        interfaz_lente.__mul__()
    except Exception as e:
        print(f"Se produjo un error: {e}")

if __name__ == "__main__":
    main()
