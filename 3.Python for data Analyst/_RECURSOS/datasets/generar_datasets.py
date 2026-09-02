# -*- coding: utf-8 -*-
"""Genera los datasets compartidos del curso. Deterministico (seed fija)."""
import os, random, datetime

ROOT = r"G:\Mi unidad\HOME\DATA ACADEMY\CURSO\EDICION_3\3.Python for data Analyst"
DS = os.path.join(ROOT, "_RECURSOS", "datasets")
random.seed(20260824)

CIUDADES = ["Lima", "Arequipa", "Trujillo", "Cusco", "Piura", "Chiclayo"]
CATEGORIAS = {
    "Laptop": 3200.0, "Monitor": 780.0, "Teclado": 120.0, "Mouse": 65.0,
    "Audifonos": 210.0, "Impresora": 950.0, "Webcam": 180.0, "Silla": 640.0,
}
CANALES = ["Web", "Tienda", "Telefono"]
SEGMENTOS = ["Retail", "Corporativo", "PyME"]


def esc(v):
    s = str(v)
    return '"' + s + '"' if ";" in s else s


def write_csv(path, header, rows, sep=";"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(sep.join(header) + "\n")
        for r in rows:
            f.write(sep.join(esc(x) for x in r) + "\n")
    print("OK", os.path.relpath(path, ROOT), f"({len(rows)} filas)")


# ---------------------------------------------------------------- clientes --
NOMBRES = ["Ana Torres", "Luis Ramos", "Carla Diaz", "Jorge Sosa", "Maria Leon",
           "Pedro Vega", "Sofia Ruiz", "Diego Paz", "Elena Cruz", "Raul Mena",
           "Nadia Rojas", "Ivan Soto", "Paula Nieto", "Hugo Lara", "Rosa Pinto",
           "Marco Silva", "Julia Campos", "Oscar Bravo", "Nora Quispe", "Cesar Ayala"]
clientes = []
for i, nom in enumerate(NOMBRES, start=1):
    cid = f"C{i:03d}"
    clientes.append([cid, nom, random.choice(CIUDADES), random.choice(SEGMENTOS),
                     f"20{random.randint(20, 24)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"])
# un cliente extra que NO tiene ventas -> sirve para explicar left vs inner join
clientes.append(["C099", "Cliente Sin Compras", "Lima", "PyME", "2024-11-02"])
write_csv(os.path.join(DS, "clientes.csv"),
          ["id_cliente", "nombre", "ciudad", "segmento", "fecha_alta"], clientes)

# --------------------------------------------------------------- productos --
productos = [[f"P{i:02d}", nom, round(precio, 2), "Tecnologia" if nom != "Silla" else "Mobiliario"]
             for i, (nom, precio) in enumerate(CATEGORIAS.items(), start=1)]
write_csv(os.path.join(DS, "productos.csv"),
          ["id_producto", "producto", "precio_lista", "categoria"], productos)

# ------------------------------------------------- ventas.csv (sucio a proposito)
# sep=';', decimal=',', fechas en dos formatos, nulos, duplicados, espacios,
# una fila con id_cliente inexistente y una cantidad negativa (devolucion).
prod_ids = [p[0] for p in productos]
cli_ids = [c[0] for c in clientes if c[0] != "C099"]
ventas = []
vid = 1
base = datetime.date(2025, 1, 1)
for _ in range(480):
    d = base + datetime.timedelta(days=random.randint(0, 364))
    pid = random.choice(prod_ids)
    precio = dict(zip(prod_ids, [p[2] for p in productos]))[pid]
    cant = random.randint(1, 6)
    desc = random.choice([0, 0, 0, 5, 10, 15])
    fecha = d.strftime("%d/%m/%Y") if random.random() < 0.25 else d.isoformat()
    cliente = random.choice(cli_ids)
    ciudad = random.choice(CIUDADES)
    # ruido: espacios y mayusculas inconsistentes en el canal
    canal = random.choice(CANALES)
    canal = random.choice([canal, canal.upper(), f" {canal} ", canal.lower()])
    importe = round(precio * cant * (1 - desc / 100), 2)
    ventas.append([f"V{vid:04d}", fecha, cliente, pid, cant,
                   str(precio).replace(".", ","), desc,
                   str(importe).replace(".", ","), ciudad, canal])
    vid += 1

# nulos: 18 filas sin ciudad, 12 sin importe
for r in random.sample(ventas, 18):
    r[8] = ""
for r in random.sample(ventas, 12):
    r[7] = ""
# duplicados exactos: 9 filas repetidas
ventas += [list(r) for r in random.sample(ventas, 9)]
# 1 devolucion (cantidad negativa) y 1 cliente fantasma
ventas.append(["V9001", "2025-07-14", "C004", "P01", -1, "3200,0", 0, "-3200,0", "Lima", "Web"])
ventas.append(["V9002", "2025-09-03", "C777", "P03", 2, "120,0", 0, "240,0", "Cusco", "Tienda"])
random.shuffle(ventas)
write_csv(os.path.join(DS, "ventas.csv"),
          ["id_venta", "fecha", "id_cliente", "id_producto", "cantidad",
           "precio_unitario", "descuento_pct", "importe", "ciudad", "canal"], ventas)

# ------------------------- ventas_mensuales/ : mismos datos partidos por mes --
carpeta = os.path.join(DS, "ventas_mensuales")
por_mes = {}
for r in ventas:
    f = r[1]
    mes = f[3:5] + "-" + f[6:10] if "/" in f else f[5:7] + "-" + f[0:4]
    mm, yyyy = mes.split("-")
    por_mes.setdefault(f"{yyyy}-{mm}", []).append(r)
for mes, rows in sorted(por_mes.items()):
    write_csv(os.path.join(carpeta, f"ventas_{mes}.csv"),
              ["id_venta", "fecha", "id_cliente", "id_producto", "cantidad",
               "precio_unitario", "descuento_pct", "importe", "ciudad", "canal"],
              rows)

# ------------------------------------------------------------------ README --
with open(os.path.join(DS, "README.md"), "w", encoding="utf-8") as f:
    f.write("""# Datasets del curso

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
| Separador `;` y decimal `,` | todas | `read_csv(sep=';', decimal=',')` |
| Fechas en dos formatos (`YYYY-MM-DD` y `DD/MM/YYYY`) | ~25% | `pd.to_datetime(..., format='mixed', dayfirst=True)` |
| `ciudad` vacia | 18 | `isna`, `fillna`, `dropna` |
| `importe` vacio | 12 | recalcular en vez de rellenar |
| Filas duplicadas exactas | 9 | `duplicated`, `drop_duplicates` |
| `canal` con espacios y mayusculas inconsistentes | ~75% | `.str.strip().str.title()` |
| 1 venta con `cantidad` negativa (`V9001`) | 1 | decidir si es error o devolucion, y documentarlo |
| 1 venta con `id_cliente` inexistente (`C777`) | 1 | validar el merge: inner pierde la fila, left la conserva con nulos |
| 1 cliente sin ninguna venta (`C099`) | 1 | la otra cara del join |

**Los conteos de arriba son la respuesta.** No compartir este README con el alumno antes
de cerrar el MODULO-04.

## Regenerar

Los datos son deterministicos (`random.seed(20260824)`). El script que los genera vive en
`_RECURSOS/datasets/generar_datasets.py`.
""")
print("OK _RECURSOS/datasets/README.md")

# copia del generador junto a los datos, para poder regenerarlos
import shutil
shutil.copy(__file__, os.path.join(DS, "generar_datasets.py"))
print("OK _RECURSOS/datasets/generar_datasets.py")
