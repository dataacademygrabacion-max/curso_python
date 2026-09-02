# Reto 00 — no tiene solucion, tiene troubleshooting

El reto es diagnostico: o corre o no corre. Lo que se corrige es el error del alumno.

## Fallas tipicas y su causa

| Sintoma | Causa | Arreglo |
|---|---|---|
| `ModuleNotFoundError: pandas` | El kernel apunta al Python base, no a `pyda3` | `Kernel -> Change Kernel -> Python (pyda3)`. Si no aparece: `conda activate pyda3 && python -m ipykernel install --user --name pyda3` |
| `FileNotFoundError: ventas.csv` | Ruta relativa mal, abrio Jupyter desde otra carpeta | Que abra JupyterLab en la raiz del curso, o que ajuste la ruta |
| El DataFrame sale con 1 sola columna | Olvido `sep=';'` | Recordar que el separador depende del archivo, no es siempre coma |
| `precio_unitario` sale como texto | Olvido `decimal=','` | Idem |
| `UnicodeDecodeError` | Windows abriendo UTF-8 como cp1252 | `encoding='utf-8'` explicito |
| El grafico no aparece | Falta `plt.show()` o backend raro | En Jupyter moderno no hace falta `%matplotlib inline`; si igual falla, agregarlo |
| `conda: command not found` | Anaconda no esta en el PATH | Usar "Anaconda Prompt" en vez de CMD/PowerShell |

## Correccion

Aprobado / no aprobado. No lleva nota numerica, pero **es requisito para entregar el reto 01**.
