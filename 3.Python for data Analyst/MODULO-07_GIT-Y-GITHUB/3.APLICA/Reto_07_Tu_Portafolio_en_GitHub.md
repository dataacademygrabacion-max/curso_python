# Reto 07 — Publica tu portafolio en GitHub

**Entregable:** la URL de un repositorio **publico** en GitHub.
**Fecha limite:** la del cronograma del modulo.

Este reto no se entrega como notebook. Se entrega como link. Y ese link es el que vas a
pegar en tu CV y en LinkedIn, asi que hazlo bien una vez.

---

## Que tienes que publicar

Toma **tu solucion del reto del MODULO-05 o del MODULO-06** (la que te haya quedado mejor)
y conviertela en un repositorio presentable.

---

## Pasos

### 1. Prepara la carpeta local

```bash
mkdir analisis-ventas-2025
cd analisis-ventas-2025
git init -b main
```

Copia adentro tu notebook. **Limpia los outputs antes de nada**:
`Kernel -> Restart & Clear Output`, y guarda.

### 2. `.gitignore` primero

Antes del primer `git add`. Como minimo:

```
*.csv
*.xlsx
data/
.env
.ipynb_checkpoints/
__pycache__/
.venv/
*.db
```

> Si tus datos son chicos y **no** tienen informacion de personas reales, puedes subirlos
> a proposito: hace que tu notebook se pueda reproducir. Es una decision, tomala explicitamente
> y explicala en el README.

### 3. README.md — es lo unico que la mayoria va a leer

Debe tener, en este orden:

1. **Titulo** y una linea de que hace.
2. **El problema**: que pregunta de negocio responde.
3. **Los datos**: de donde salen, cuantas filas, que periodo cubren.
4. **Como correrlo**: los comandos exactos, desde cero.
5. **Resultados**: 2 o 3 hallazgos concretos, con numeros. Si tienes un grafico, incrustalo con `![](dashboard.png)`.
6. **Stack**: Python 3.11, pandas, matplotlib.

Escribelo pensando en alguien que llega desde LinkedIn, no te conoce y te da 40 segundos.

### 4. Al menos 5 commits con historia real

No vale hacer un `git add .` de todo y un commit "primera version".
Trocea el trabajo, un commit por paso logico:

```
Agrega el notebook de carga y exploracion inicial
Corrige el separador y el decimal en la lectura del CSV
Agrega la limpieza de duplicados y nulos
Agrega los graficos de facturacion mensual y por producto
Documenta hallazgos y como reproducir el analisis en el README
```

### 5. Una rama de verdad

Crea una rama para una mejora (un grafico extra, una funcion refactorizada), commitea ahi,
vuelve a `main` y mergeala. Que quede en el historial.

### 6. Publica

Crea el repo **vacio** en github.com (sin README, sin .gitignore — los tuyos ya existen) y:

```bash
git remote add origin https://github.com/TU-USUARIO/analisis-ventas-2025.git
git push -u origin main
```

### 7. Revisa como se ve

Abre tu repo en el navegador **en modo incognito**. Lo que ves ahi es lo que ve un reclutador.

- Se entiende que hace el proyecto sin abrir ningun archivo?
- El notebook se renderiza bien en GitHub?
- Hay algun archivo que no deberia estar ahi?

---

## Criterios de aceptacion

- [ ] El repo es **publico** y la URL abre en incognito
- [ ] Tiene `README.md` con las 6 secciones de arriba
- [ ] Tiene `.gitignore` y **ninguna** credencial ni dato personal en el historial
- [ ] Hay **5 commits o mas**, con mensajes que dicen que cambio
- [ ] Ningun mensaje es `update`, `cambios`, `.` ni similar
- [ ] El historial muestra al menos **una rama creada y mergeada** (`git log --graph` lo prueba)
- [ ] El notebook esta **sin outputs pesados** y se ve bien renderizado en GitHub
- [ ] El README tiene al menos un hallazgo con una cifra concreta

## Puntos extra

- +1 Un badge de licencia o un `LICENSE` (MIT sirve)
- +1 `requirements.txt` para que otro pueda reproducirlo
- +2 El repo fijado (*pinned*) en tu perfil de GitHub, con el perfil completo: foto, bio y link

---

## Errores que cuestan puntos

| Error | Por que importa |
|---|---|
| Subir un `.env`, un token o una cadena de conexion | Es un incidente de seguridad. Aunque lo borres despues, queda en el historial. Rota la credencial. |
| Un solo commit gigante | El historial no cuenta ninguna historia; es lo mismo que no usar git. |
| Notebook con outputs de miles de lineas | GitHub no lo renderiza y el diff es ilegible. |
| README de una linea | Es el 80% de la primera impresion. |
| Datos de clientes reales en un repo publico | Grave. Anonimiza o no los subas. |
| Rutas absolutas `C:\Users\...` en el notebook | No corre en ninguna otra maquina. |
