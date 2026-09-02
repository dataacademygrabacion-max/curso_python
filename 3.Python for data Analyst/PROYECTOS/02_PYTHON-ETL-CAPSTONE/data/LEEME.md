# Datos del capstone

Copia aqui, o enlaza desde `_RECURSOS/datasets/`:

```
data/
  ventas_mensuales/    los 12 CSV mensuales
  clientes.csv
  productos.csv
```

Desde la raiz del curso:

```bash
cp -r "_RECURSOS/datasets/ventas_mensuales" "PROYECTOS/02_PYTHON-ETL-CAPSTONE/data/"
cp "_RECURSOS/datasets/clientes.csv" "_RECURSOS/datasets/productos.csv" "PROYECTOS/02_PYTHON-ETL-CAPSTONE/data/"
```

En PowerShell:

```powershell
Copy-Item "_RECURSOS\datasets\ventas_mensuales" "PROYECTOS\02_PYTHON-ETL-CAPSTONE\data\" -Recurse
Copy-Item "_RECURSOS\datasets\clientes.csv","_RECURSOS\datasets\productos.csv" "PROYECTOS\02_PYTHON-ETL-CAPSTONE\data\"
```

> **No subas esta carpeta a GitHub.** Tu `.gitignore` debe incluir `data/`.
> En el README del repo explica de donde salen los datos y como obtenerlos.
