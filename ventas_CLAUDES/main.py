"""main.py - Punto de entrada: une datos, operaciones y menú.

Solo orquesta; la lógica vive en cada módulo.
Ejecutar con:  python main.py
"""

from datos import GestorDatos
from menu import Menu
from operaciones import OperacionesVentas

RUTA_POR_DEFECTO = "DS/ventas.csv"

# Números de opción del menú (evita "números mágicos" repartidos por el código).
OPC_TABLA = 1
OPC_MAX_MIN = 2
OPC_SALIR = 3

OPCIONES_MENU = {
    OPC_TABLA: "Mostrar tabla de ventas",
    OPC_MAX_MIN: "Mostrar máximo y mínimo",
    OPC_SALIR: "Salir",
}


def ejecutar_menu(operaciones: OperacionesVentas) -> None:
    """Bucle principal: muestra el menú hasta que el usuario decide salir."""
    menu = Menu("Menú Ventas", OPCIONES_MENU)

    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == OPC_TABLA:
            cantidad = Menu.pedir_entero_positivo("¿Cuántos registros quieres ver?", 5)
            print(operaciones.mostrar_tabla(cantidad).to_string(index=False))
        elif opcion == OPC_MAX_MIN:
            # La propia función imprime el resultado.
            try:
                operaciones.mostrar_max_min()
            except (KeyError, TypeError) as error:
                print(f"Error: {error}")
        else:  # OPC_SALIR
            print("Gracias, un saludo.")
            break


def main() -> None:
    print("Bienvenido al programa de ventas.")
    print("Podrás ver la tabla de ventas y sus valores máximo y mínimo.\n")

    ruta = input(f"Ruta del CSV [{RUTA_POR_DEFECTO}]: ").strip() or RUTA_POR_DEFECTO

    gestor = GestorDatos()
    try:
        df = gestor.cargar_csv(ruta)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return

    print("Datos cargados correctamente.")
    ejecutar_menu(OperacionesVentas(df))


if __name__ == "__main__":
    main()
