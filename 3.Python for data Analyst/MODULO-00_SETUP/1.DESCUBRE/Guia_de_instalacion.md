# Guia de instalacion — Python for Data Analyst

Haz esto **antes** de la primera clase. Si algo falla, escribe al canal del curso
con la captura del error; no lo dejes para el dia de la sesion.

Tiempo estimado: 30 minutos, casi todos de descarga.

---

## 1. Instalar Anaconda

Instalador incluido en `_RECURSOS/Instaladores/`, o desde https://www.anaconda.com/download

Durante la instalacion:

- Instalar **"Just Me"** (no requiere permisos de administrador).
- Ruta **sin espacios ni tildes**. `C:\Users\tunombre\anaconda3` sirve.
- Dejar marcado "Register Anaconda as my default Python".
- La casilla "Add to PATH" viene desmarcada y **asi se queda**. Vas a usar el
  **Anaconda Prompt**, que ya trae todo configurado.

## 2. Abrir el Anaconda Prompt

Menu Inicio -> escribe `Anaconda Prompt`. Es una consola negra. Verifica:

```bash
conda --version
```

Si responde con un numero de version, vas bien.

> **Windows:** usa Anaconda Prompt, no CMD ni PowerShell. Es la causa numero uno de
> `conda: command not found`.

## 3. Crear el entorno del curso

Un entorno es una instalacion de Python aislada. Sirve para que este curso no rompa
otro proyecto tuyo, y al reves.

Desde la carpeta del curso:

```bash
conda env create -f _RECURSOS/environment.yml
conda activate pyda3
```

Cuando el entorno esta activo, el prompt empieza con `(pyda3)`. **Si no lo ves, no esta activo.**

### Si no usas conda

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r _RECURSOS/requirements.txt
```

## 4. Registrar el kernel en Jupyter

Este es el paso que todo el mundo se salta y luego pasa media clase con `ModuleNotFoundError`:

```bash
python -m ipykernel install --user --name pyda3 --display-name "Python (pyda3)"
```

Sin esto, Jupyter abre tus notebooks con el Python de siempre —el que **no** tiene pandas—
y no te dice por que.

## 5. Abrir JupyterLab

```bash
cd "ruta/a/la/carpeta/del/curso"
jupyter lab
```

Se abre en el navegador. Arriba a la derecha de cada notebook aparece el kernel:
debe decir **Python (pyda3)**. Si dice otra cosa: `Kernel -> Change Kernel`.

## 6. Verificar

Abre `MODULO-00_SETUP/3.APLICA/Reto_00_Verifica_tu_entorno.ipynb` y corre
`Kernel -> Restart & Run All`. Si llega al final sin errores rojos, terminaste.

---

## Comandos de conda que vas a necesitar

| Necesito | Comando |
|---|---|
| Ver mis entornos | `conda env list` |
| Activar el del curso | `conda activate pyda3` |
| Salir del entorno | `conda deactivate` |
| Instalar un paquete mas | `conda install -c conda-forge nombre` |
| Ver que tengo instalado | `conda list` |
| Empezar de cero | `conda env remove -n pyda3` y volver al paso 3 |

## Problemas frecuentes

| Error | Causa | Solucion |
|---|---|---|
| `conda: command not found` | Estas en CMD o PowerShell | Usa el Anaconda Prompt |
| `ModuleNotFoundError: pandas` en Jupyter | El kernel no es `pyda3` | Paso 4, y `Kernel -> Change Kernel` |
| `CondaHTTPError` | Red o proxy corporativo | Prueba desde otra red; si es proxy, `conda config --set ssl_verify false` (temporal) |
| `EnvironmentNotWritableError` | Anaconda instalado "All Users" | Reinstalar como "Just Me" |
| Jupyter abre pero no ve la carpeta del curso | Lo lanzaste desde otro sitio | `cd` a la carpeta del curso **antes** de `jupyter lab` |
| Ruta con tildes o espacios da errores raros | Windows + rutas no ASCII | Mueve el curso a una ruta simple |

## Editor: VS Code (opcional pero recomendado)

https://code.visualstudio.com/ + la extension **Python** de Microsoft.
Abre `.ipynb` directamente y es mas comodo que el navegador para escribir codigo.
Selecciona el interprete con `Ctrl+Shift+P` -> "Python: Select Interpreter" -> `pyda3`.
