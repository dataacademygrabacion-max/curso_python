# MODULO 06 — Archivos, rutas y bases de datos

**Objetivo:** Procesar carpetas enteras de archivos y leer/escribir contra una base de datos.

**Prerequisito:** MODULO-05 completo.

**Entregable:** `Reto_06_Archivos_y_BBDD.ipynb` resuelto.

---

## Temario

1. `pathlib.Path`: rutas que funcionan en Windows y Linux
2. Recorrer carpetas con `glob` / `rglob`
3. Procesamiento en lote: leer N archivos y consolidarlos en un DataFrame
4. Abrir, leer y escribir archivos de texto con `with open`
5. SQLite con `sqlite3`: crear tabla, insertar, consultar
6. SQLAlchemy: `create_engine`, `pd.read_sql`, `df.to_sql`
7. Credenciales fuera del codigo (variables de entorno)

---

## Ruta de la sesion

| Fase | Carpeta | Que pasa |
|------|---------|----------|
| 1 | `1.DESCUBRE/` | El profesor explica con `Clase_06.ipynb` y las slides. El alumno mira. |
| 2 | `2.EXPLORA/` | Practica guiada. El alumno abre el `_Base` y replica; el profesor va por el `_Caso`. |
| 3 | `3.APLICA/` | Reto individual fuera de clase. La solucion esta en `SOLUCION/` y se libera al cerrar el modulo. |

## Checklist antes de dictar

- [ ] `1.DESCUBRE/Clase_06.ipynb` corre entero sin error
- [ ] Cada notebook de `2.EXPLORA` tiene su pareja `_Base` / `_Caso`
- [ ] Los `_Base` estan sin outputs guardados
- [ ] Las rutas a datos son relativas (`./data/...`), no absolutas
- [ ] `3.APLICA/` tiene el reto y `SOLUCION/` la respuesta
- [ ] La grabacion de la edicion anterior esta en `_GRABACIONES/MODULO-06/`
