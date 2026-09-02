# Reto 07 — referencia de correccion

## Como corregir, en 5 minutos por alumno

1. Abrir la URL **en incognito**. Si pide login, no es publico: −5 directo.
2. `git clone <url> && cd <repo> && git log --oneline --graph --all`
   - Cuenta commits, mira mensajes, verifica que exista una rama mergeada.
3. `git log --all --full-history -- "*.env" "*.csv" "*.xlsx"`
   - Si sale algo, hubo fuga. Avisarle **en privado** y decirle que rote la credencial.
4. Leer el README como si no conocieras el curso. Se entiende en 40 segundos?
5. Abrir el notebook en GitHub: renderiza? Tiene rutas absolutas?

## Puntaje (sobre 20)

| Criterio | Pts |
|---|---|
| Repo publico y accesible | 2 |
| README con las 6 secciones | 5 |
| `.gitignore` correcto y sin credenciales en el historial | 4 |
| 5+ commits con mensajes utiles | 4 |
| Rama creada y mergeada, visible en el grafo | 3 |
| Notebook limpio, sin outputs pesados ni rutas absolutas | 2 |

Extras: +1 LICENSE, +1 requirements.txt, +2 perfil de GitHub completo con el repo fijado.
Maximo 20.

---

## README de referencia

Este es el nivel que se espera. Sirve de ejemplo para mostrar en clase.

````markdown
# Analisis de ventas 2025 — tienda de tecnologia

Consolida un ano de ventas y responde donde poner el presupuesto del proximo trimestre.

## El problema

El area comercial reparte el presupuesto de marketing por igual entre ciudades y canales.
Este analisis prueba que ese reparto parejo no corresponde con como se factura de verdad.

## Los datos

- `ventas.csv`: 491 registros de ventas de 2025, 10 columnas.
- Fuente: export del sistema comercial. Llega con separador `;`, decimal `,`,
  fechas en dos formatos y duplicados.
- Tras limpiar: 481 ventas efectivas (482 movimientos menos 1 devolucion).

Los datos no se versionan (ver `.gitignore`). Para reproducir, pedirlos al area comercial
y dejarlos en `data/`.

## Como correrlo

```bash
git clone https://github.com/usuario/analisis-ventas-2025.git
cd analisis-ventas-2025
pip install -r requirements.txt
jupyter lab analisis_ventas.ipynb
```

## Resultados

![Dashboard](dashboard_ventas.png)

1. **El top 3 de productos concentra el 62% de la facturacion.** Un quiebre de stock ahi
   cuesta mas que cualquier campana.
2. **El mix de canales cambia por ciudad**: en Lima domina Web, en Cusco Tienda.
   El presupuesto nacional unico deja plata sobre la mesa.
3. **El ticket promedio enganaba**: la distribucion tiene cola larga y una sola laptop
   mueve la media del mes. Se propone reportar la mediana.

## Stack

Python 3.11 · pandas 2.2 · matplotlib 3.8 · seaborn 0.13
````

---

## Fallas tipicas y como orientar

| Sintoma | Que decirle |
|---|---|
| `git push` pide usuario y contrasena y rechaza | GitHub ya no acepta contrasena. Personal Access Token o GitHub CLI (`gh auth login`). |
| `error: failed to push some refs` | Creo el repo en GitHub **con** README. `git pull --rebase origin main` y volver a pushear. Por eso se pide crearlo vacio. |
| `fatal: not a git repository` | Esta parado en otra carpeta. `pwd` y `cd`. |
| El notebook no renderiza en GitHub | JSON corrupto o demasiado pesado. Limpiar outputs y volver a guardar. |
| Subio la carpeta `.venv` entera | `.gitignore` puesto despues del primer `add`. `git rm -r --cached .venv` y recommitear. |
