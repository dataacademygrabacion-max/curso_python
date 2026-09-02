# Proyecto capstone — ETL de ventas end-to-end

**Peso:** 40% de la nota final.
**Entrega:** repositorio publico en GitHub + el link.
**Rubrica completa:** `_ADMIN/RUBRICA.md`

Este es el proyecto que junta los 8 modulos. Tambien es, muy probablemente, el primer
proyecto real de tu portafolio. Hazlo pensando en eso.

---

## El encargo

Eres el analista de una tienda de tecnologia con 6 sucursales. La gerencia comercial
va a repartir el presupuesto de marketing del proximo trimestre y hoy lo hace
**por partes iguales entre ciudades y canales**, porque nadie ha mirado los datos.

Tu trabajo: construir el proceso que responda si ese reparto tiene sentido, y dejarlo
**repetible** — el mes que viene llegan datos nuevos y nadie quiere rehacerlo a mano.

## Las 3 preguntas de negocio

1. **Donde poner el presupuesto?** Que ciudades y canales concentran la facturacion,
   y cuanto se desvia eso del reparto parejo actual.
2. **Que productos hay que proteger?** Cuanta facturacion depende de los top productos
   y cual es el riesgo de un quiebre de stock.
3. **Que KPI deberia mirar la gerencia?** Hoy miran ticket promedio. Es el indicador correcto
   para esta distribucion de ventas? Sustenta tu respuesta con los datos.

## Las fuentes

En `data/` (o desde `_RECURSOS/datasets/`):

| Fuente | Archivo | Que trae |
|---|---|---|
| Transaccional | `ventas_mensuales/*.csv` | 12 archivos, uno por mes. Sucios. |
| Maestro de clientes | `clientes.csv` | id, nombre, ciudad, segmento |
| Catalogo | `productos.csv` | id, producto, precio de lista, categoria |
| Externa | API de tipo de cambio | para expresar el resultado tambien en USD |

Si la API no responde, tu codigo debe seguir funcionando con un valor de respaldo
y **decirlo**. Un pipeline que muere porque un servicio externo se cayo no es un pipeline.

---

## Lo que tienes que entregar

### 1. El notebook `analisis_ventas.ipynb`

Estructurado en las 5 etapas, en este orden y con estos titulos:

```
1. EXTRACT     leer las 3 fuentes sin intervencion manual
2. TRANSFORM   limpiar, tipar, deduplicar — documentando cada decision
3. LOAD        cargar el resultado a SQLite y exportar el CSV maestro
4. ANALYZE     responder las 3 preguntas con datos
5. VISUALIZE   4 graficos, cada uno con su conclusion escrita
```

Ademas, al final: **una seccion "Conclusiones y recomendaciones"** de media pagina,
escrita para alguien que no sabe programar. Es la unica parte que va a leer la gerencia.

### 2. El repo en GitHub

Con `README.md`, `.gitignore`, `requirements.txt` e historial de commits real.
Aplica exactamente lo del MODULO-07.

### 3. Reproducibilidad

Otra persona clona tu repo, sigue tu README y llega al mismo resultado.
Si tu notebook necesita que alguien renombre un archivo a mano, no esta terminado.

---

## Requisitos tecnicos

Estos se verifican uno por uno:

- [ ] La lectura de la carpeta usa `pathlib` + `glob`. **Cero nombres de archivo hardcodeados.**
- [ ] Un solo `pd.concat`, fuera del bucle.
- [ ] La limpieza esta en **funciones**, no en celdas sueltas copiadas.
- [ ] Cada `merge` lleva `how=` explicito y `validate=`.
- [ ] Antes de cada merge hay una verificacion de que no se pierden filas.
- [ ] Los nulos se tratan **por columna**, con una justificacion escrita por cada decision.
- [ ] Al menos una consulta SQL sobre la base SQLite.
- [ ] Al menos un `try/except` con un error concreto (no `except Exception`).
- [ ] Rutas relativas en todo el notebook.
- [ ] `Restart & Run All` corre limpio de principio a fin.

## Lo que hunde un capstone

| Error | Por que |
|---|---|
| Notebook de 200 celdas sin una sola de markdown | Nadie —incluido tu en dos meses— entiende que pasa |
| "Limpie los nulos" sin decir como ni por que | La limpieza **es** el analisis; lo demas es teclear |
| Graficos sin conclusion | Un grafico que no cambia una decision es decoracion |
| Conclusiones tipo "hay que vender mas" | No es un hallazgo, es una obviedad |
| Un solo commit "proyecto final" | El modulo 07 existio para algo |
| Datos de clientes en un repo publico | Es un incidente, no un descuido |

---

## Cronograma sugerido

| Semana | Entregable parcial |
|---|---|
| 1 | Extract + Transform funcionando. Repo creado con 3 commits. |
| 2 | Load + Analyze. Las 3 preguntas respondidas con numeros. |
| 3 | Visualize + README + pulido. Entrega. |

Empieza por el punto 1 del notebook base. No esperes a la ultima semana:
el 80% del tiempo real se va en Transform, y eso no se puede acelerar.
