"""operaciones.py - Lógica de negocio sobre las ventas.

Recibe un DataFrame ya cargado (inyección de dependencias): así esta clase
no depende de cómo se obtienen los datos y es fácil de probar o ampliar.
"""

import pandas as pd


class OperacionesVentas:
    """Operaciones de consulta sobre la tabla de ventas."""

    # Columna sobre la que se calculan el máximo y el mínimo por defecto.
    COLUMNA_POR_DEFECTO = "precio_unitario"

    def __init__(self, df: pd.DataFrame, columna_valor: str = COLUMNA_POR_DEFECTO) -> None:
        self._df = df
        self._columna_valor = columna_valor

    def mostrar_tabla(self, cantidad: int = 5) -> pd.DataFrame:
        """Devuelve los primeros `cantidad` registros (5 por defecto)."""
        return self._df.head(cantidad)

    def mostrar_max_min(self) -> None:
        """Imprime el registro con el valor máximo y el que tiene el mínimo.

        No devuelve nada: solo muestra por pantalla (según el diseño original).
        """
        self._validar_columna()

        # nlargest/nsmallest devuelven la fila completa, no solo el número.
        registro_max = self._df.nlargest(1, self._columna_valor)
        registro_min = self._df.nsmallest(1, self._columna_valor)

        print(f"\n--- Máximo de '{self._columna_valor}' ---")
        print(registro_max.to_string(index=False))
        print(f"\n--- Mínimo de '{self._columna_valor}' ---")
        print(registro_min.to_string(index=False))

    def _validar_columna(self) -> None:
        """Comprueba que la columna existe y es numérica antes de operar."""
        if self._columna_valor not in self._df.columns:
            raise KeyError(f"La columna '{self._columna_valor}' no existe en el CSV.")
        if not pd.api.types.is_numeric_dtype(self._df[self._columna_valor]):
            raise TypeError(f"La columna '{self._columna_valor}' no es numérica.")
