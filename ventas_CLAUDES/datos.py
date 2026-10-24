"""datos.py - Capa de acceso a datos.

Responsabilidad única: cargar el fichero CSV y custodiar el DataFrame.
No sabe nada de menús ni de cálculos (principio S de SOLID).
"""

from pathlib import Path
from typing import Optional

import pandas as pd


class GestorDatos:
    """Gestiona la carga y el acceso a los datos del fichero CSV."""

    def __init__(self) -> None:
        # Guardamos el DataFrame en un atributo "privado".
        # Mientras no se cargue ningún fichero vale None.
        self._df: Optional[pd.DataFrame] = None

    def cargar_csv(self, ruta: str) -> pd.DataFrame:
        """Lee el CSV indicado y lo guarda en memoria.

        Raises:
            FileNotFoundError: si la ruta no apunta a un fichero existente.
        """
        path = Path(ruta)
        if not path.is_file():
            raise FileNotFoundError(f"No se encuentra el archivo: {path}")

        # utf-8-sig elimina el BOM que Excel añade al guardar CSV;
        # sin él la primera columna se llamaría '\ufeffid_venta'.
        self._df = pd.read_csv(path, encoding="utf-8-sig")
        return self._df

    def obtener_datos(self) -> pd.DataFrame:
        """Devuelve el DataFrame cargado.

        Raises:
            ValueError: si todavía no se ha cargado ningún fichero.
        """
        if self._df is None:
            raise ValueError("Aún no se han cargado datos. Usa cargar_csv() primero.")
        return self._df

    def hay_datos(self) -> bool:
        """Indica si hay un DataFrame cargado y con filas."""
        return self._df is not None and not self._df.empty
