# Datasets del curso

Todos los modulos de Pandas en adelante usan **el mismo caso**: una tienda de tecnologia.
Asi el alumno no pierde tiempo entendiendo un dominio nuevo en cada clase.

| Archivo | Separador | Decimal | Se usa en |
|---|---|---|---|
| `ventas.csv` | `;` | `,` | MODULO-04 (cargar y limpiar), 05, 08 |
| `clientes.csv` | `;` | `.` | MODULO-05 (merge) |
| `productos.csv` | `;` | `.` | MODULO-05 (merge) |
| `ventas_mensuales/` | `;` | `,` | MODULO-06 (procesar una carpeta en lote) |

## Suciedad intencional de `ventas.csv`

Esta sucio a proposito. Cada defecto existe para ensenar algo:

| Defecto | Filas | Se ensena en |
|---|---|---|
| Separador `;` y decimal `,` | 491 | `read_csv(sep=';', decimal=',')` |
| Fechas en dos formatos (`YYYY-MM-DD` y `DD/MM/YYYY`) | 124 de 491 | `pd.to_datetime(..., format='mixed', dayfirst=True)` |
| `ciudad` vacia | 19 | `isna`, `fillna`, `dropna` |
| `importe` vacio | 12 | recalcular en vez de rellenar |
| Filas duplicadas exactas | 9 (491 -> 482) | `duplicated`, `drop_duplicates` |
| `canal` con espacios y mayusculas inconsistentes | 12 variantes para 3 canales | `.str.strip().str.title()` |
| 1 venta con `cantidad` negativa (`V9001`) | 1 | decidir si es error o devolucion, y documentarlo |
| 1 venta con `id_cliente` inexistente (`C777`) | 1 | validar el merge: inner pierde la fila, left la conserva con nulos |
| 1 cliente sin ninguna venta (`C099`) | 1 | la otra cara del join |

**Los conteos de arriba son la respuesta.** No compartir este README con el alumno antes
de cerrar el MODULO-04.

## Cifras de control

- `ventas.csv`: **491 filas**, 10 columnas. Tras `drop_duplicates()`: **482**.
- `clientes.csv`: 21 filas (20 con ventas + `C099` sin ninguna).
- `productos.csv`: 8 filas.
- Importe total sin duplicados, ignorando nulos: **S/ 1,304,567.75**.

## Regenerar

Los datos son deterministicos (`random.seed(20260824)`). El script que los genera vive en
`_RECURSOS/datasets/generar_datasets.py`.
