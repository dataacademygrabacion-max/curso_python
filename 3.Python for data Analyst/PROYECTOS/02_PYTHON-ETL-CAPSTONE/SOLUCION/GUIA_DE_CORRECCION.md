# Capstone — guia de correccion

## Como corregir, en 15 minutos por alumno

1. Clonar el repo en un entorno limpio: `conda activate pyda3`.
2. Seguir **solo** lo que dice su README. Si no llegas a correrlo con eso, el criterio
   "Entrega" pierde la mitad de los puntos: el proyecto no es reproducible.
3. `Restart & Run All`. Si truena, anota en que celda y sigue corrigiendo el resto.
4. Leer **primero** la seccion de conclusiones finales, antes del codigo. Si esa seccion no
   se sostiene sola, el proyecto no cumple su proposito aunque el codigo sea impecable.
5. Recien despues revisar el codigo contra los requisitos tecnicos del enunciado.

## Puntaje (ver `_ADMIN/RUBRICA.md` para el detalle)

| Criterio | Pts |
|---|---|
| Extract | 3 |
| Transform | 4 |
| Join | 3 |
| Analisis | 3 |
| Visualizacion | 3 |
| Entrega (repo, README, commits) | 4 |

## Cifras de control

Con los datasets del curso sin modificar:

- 12 archivos en `ventas_mensuales/`, **491 filas** consolidadas.
- Tras `drop_duplicates()`: **482**.
- Excluyendo la devolucion `V9001`: **481 ventas efectivas**.
- `clientes.csv`: 21 filas — `C099` no tiene ninguna venta.
- `productos.csv`: 8 filas — todos aparecen en ventas.
- `V9002` referencia al cliente `C777`, que no existe en el maestro.
- Merge con `clientes`: `inner` -> 481, `left` -> 482.

**Si su tabla maestra no tiene 482 filas, pregunta por que.** Puede tener una respuesta
buena (decidio excluir la devolucion y lo documento) o mala (uso `inner` sin mirar).
La diferencia entre las dos es todo el proyecto.

## Que separa un 20 de un 14

Un capstone de 14 hace todo lo que pide el enunciado. Uno de 20 ademas:

- Encuentra algo que **no** estaba en las 3 preguntas y lo justifica con datos.
- Declara sus limitaciones sin que nadie se las pida.
- Tiene funciones que se podrian copiar tal cual a otro proyecto.
- El README se entiende sin haber visto el curso.
- Las conclusiones cambiarian una decision real de la empresa.

## Senales de alarma

| Senal | Que revisar |
|---|---|
| Total facturado muy distinto a S/ 1.3 M | Probablemente no deduplico, o el decimal quedo mal |
| Tabla maestra con mas de 482 filas | Merge que multiplico filas — falto `validate=` |
| Analisis mensual con picos raros | `to_datetime` sin `dayfirst=True` |
| Cero celdas markdown entre etapas | No hay analisis, hay codigo |
| Todos los commits el mismo dia a la misma hora | Trabajo de ultima noche; no descuenta por si solo, pero explica el resto |
