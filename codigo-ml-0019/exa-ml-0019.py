# Jesus Arriaga 
# Machine Learning pandas,
#  NC 0019
import sys
import os
import io
import importlib.util
from pathlib import Path
import pandas as pd

# Detectar la carpeta raíz del proyecto (C:\Users\Alumno\Documents\exa-va-0019)
BASE_DIR = Path(__file__).resolve().parent.parent
DIR_DATOS = BASE_DIR / "datos-de-entrada-ml-0019"

# Verificar que la carpeta de datos exista
if not DIR_DATOS.exists():
    print(f"[ERROR CRÍTICO] La carpeta '{DIR_DATOS}' no existe.")
    sys.exit(1)

# Buscar automáticamente cualquier archivo .py dentro de la carpeta de datos
archivos_py = list(DIR_DATOS.glob("*.py"))

if not archivos_py:
    print(f"[ERROR CRÍTICO] No se encontró ningún archivo .py en: {DIR_DATOS}")
    sys.exit(1)

# Usar el primer archivo .py encontrado (ej. dicc-0019.py o dicc_0019.py)
ruta_dicc = archivos_py[0]
print(f"[INFO] Cargando datos desde: {ruta_dicc.name}")

# Cargar el módulo dinámicamente sin importar el uso de guiones
spec = importlib.util.spec_from_file_location("modulo_datos", ruta_dicc)
dicc_0019 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dicc_0019)

print("Jesus Arriaga Machine Learning pandas, NC 0019")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Jesus Arriaga Machine Learning pandas, NC 0019"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")


def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")


# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0019.datos_libros)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Paginas)
registrar("3. Estadísticas Generales de la Columna 'Paginas'", df['Paginas'].describe())

# 4. Ordenar Ascendente por Paginas
df_asc_paginas = df.sort_values(by="Paginas", ascending=True)
registrar("4. Ordenar Ascendente por Paginas", df_asc_paginas)

# 5. Ordenar Descendente por Paginas
df_desc_paginas = df.sort_values(by="Paginas", ascending=False)
registrar("5. Ordenar Descendente por Paginas", df_desc_paginas)

# Guardar el archivo resultados-ml-0019.md en la carpeta resultados-0019
CARPETA_RESULTADOS = BASE_DIR / 'resultados-0019'
CARPETA_RESULTADOS.mkdir(parents=True, exist_ok=True)
ruta_archivo_md = CARPETA_RESULTADOS / "resultados-ml-0019.md"

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Jesus Arriaga Machine Learning pandas, NC 0019")