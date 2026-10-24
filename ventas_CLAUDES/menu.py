"""menu.py - Interfaz de usuario por consola.

Solo pinta el menú y recoge/valida lo que escribe el usuario.
No conoce las operaciones: quien lo usa decide qué hace cada opción.
"""

from typing import Dict


class Menu:
    """Menú de consola genérico basado en un diccionario {número: texto}."""

    def __init__(self, titulo: str, opciones: Dict[int, str]) -> None:
        self._titulo = titulo
        self._opciones = opciones

    def mostrar(self) -> None:
        """Pinta el título y todas las opciones."""
        print(f"\n=== {self._titulo} ===")
        for numero, texto in self._opciones.items():
            print(f"{numero} - {texto}")

    def pedir_opcion(self) -> int:
        """Pide una opción hasta que sea un número válido del menú."""
        while True:
            entrada = input("Selecciona una opción: ").strip()
            try:
                opcion = int(entrada)
            except ValueError:
                print("Error: debes introducir un número.")
                continue
            if opcion not in self._opciones:
                print(f"Error: la opción {opcion} no es válida.")
                continue
            return opcion

    @staticmethod
    def pedir_entero_positivo(mensaje: str, por_defecto: int) -> int:
        """Pide un entero > 0. Si el usuario pulsa Enter, usa `por_defecto`."""
        while True:
            entrada = input(f"{mensaje} [{por_defecto}]: ").strip()
            if not entrada:
                return por_defecto
            try:
                valor = int(entrada)
            except ValueError:
                print("Error: debes introducir un número entero.")
                continue
            if valor <= 0:
                print("Error: el número debe ser mayor que 0.")
                continue
            return valor
