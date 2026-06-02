# Guía: Cómo Editar Lecciones en la Sección de Teoría

Esta guía te muestra cómo editar y mejorar las lecciones de la sección de aprendizaje en Kuantum.

---

## 📍 Dónde encontrar las lecciones

Todas las lecciones están en esta carpeta:
```
frontend/src/content/theory/
```

Cada lección es un archivo `.md` (Markdown). Por ejemplo:
- `introduccion.md`
- `compuertas-basicas.md`
- `circuito-bell.md`
- `leer-resultados.md`

---

## 📝 Estructura de una lección

Cada archivo Markdown tiene dos partes:

### 1️⃣ Cabecera (metadatos) — Líneas 1-5
```
---
title: Nombre de la lección
description: Breve descripción que aparece en el listado
order: 1
---
```

**Qué significa cada campo:**
- `title`: El nombre de la lección (aparece al principio de la página)
- `description`: Resumen corto (aparece en el listado de teoría)
- `order`: Número que ordena las lecciones (1, 2, 3...). **No cambies esto sin avisar**

### 2️⃣ Contenido — A partir de la línea 7
El resto del archivo es el contenido de la lección en **Markdown** (texto con formato).

---

## ✏️ Cómo editar el contenido

### Editar texto existente
1. Abre el archivo `.md` en tu editor
2. Busca el texto que quieres cambiar
3. Edítalo directamente
4. Guarda el archivo

### Añadir un nuevo párrafo
Simplemente escribe el texto nuevo. Markdown interpreta cada línea en blanco como un nuevo párrafo.

```markdown
Este es el primer párrafo.

Este es el segundo párrafo.
```

### Dar formato al texto

| Efecto | Sintaxis | Resultado |
|--------|----------|-----------|
| **Negrita** | `**texto**` | **texto** |
| *Cursiva* | `*texto*` | *texto* |
| `Código` | `` `código` `` | `código` |
| Tachado | `~~texto~~` | ~~texto~~ |

---

## 🔗 Añadir enlaces internos

Los enlaces a otras lecciones se escriben así:

```markdown
[Texto que sale en la página](/teoria/compuertas-basicas/)
```

**Importante:** El slug (nombre) debe coincidir con el nombre del archivo sin `.md`.

**Ejemplo:**
- Archivo: `compuertas-basicas.md`
- Enlace: `[Ver compuertas básicas](/teoria/compuertas-basicas/)`

**Enlaces externos:**
```markdown
[Visita Google](https://google.com)
```

---

## 🖼️ Cómo insertar imágenes

### Paso 1: Guardar la imagen
1. Coloca tu imagen (`.jpg`, `.png`, `.svg`, etc.) en esta carpeta:
   ```
   frontend/public/images/theory/
   ```
2. Dale un nombre descriptivo, por ejemplo: `hadamard-gate.png`

### Paso 2: Insertar en la lección
En el contenido Markdown, usa:

```markdown
![Descripción de la imagen](/images/theory/hadamard-gate.png)
```

**Explicación:**
- `![...]` es la sintaxis de imagen en Markdown
- El texto en `[...]` es la descripción (aparece si falla la imagen y ayuda con accesibilidad)
- `(...)` es la ruta a la imagen

### Ejemplo completo:
```markdown
## La puerta Hadamard

Aquí vemos cómo funciona:

![Diagrama de la puerta Hadamard](/images/theory/hadamard-gate.png)

Como ves en el diagrama, la puerta H...
```

---

## 🔘 Cómo añadir botones y llamadas a la acción

### Enlace como botón (llamada destacada)
Usa un enlace normal, pero Markdown lo renderizará como un botón si la página lo permite:

```markdown
[Abrir simulador](/simulador/)
```

Este enlace aparecerá como un botón en ciertos contextos (por ejemplo, en una nota destacada).

### Texto destacado con nota (caja de atención)
Aunque Markdown básico no tiene "cajas", puedes simularlas con **citas** (blockquotes):

```markdown
> **Importante:** Este es un aviso que destaca.
> Puedes escribir varios párrafos aquí.
```

También puedes usar formatos simples:

```markdown
**📌 Recuerda:** La numeración de qubits comienza en 0.
```

---

## 📊 Cómo añadir tablas

Usa la sintaxis de tablas en Markdown:

```markdown
| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |
```

**Resultado:**

| Columna 1 | Columna 2 | Columna 3 |
|-----------|-----------|-----------|
| Dato 1    | Dato 2    | Dato 3    |
| Dato 4    | Dato 5    | Dato 6    |

---

## 📋 Cómo añadir listas

### Lista desordenada (puntos):
```markdown
- Primer punto
- Segundo punto
  - Subpunto
- Tercer punto
```

### Lista ordenada (números):
```markdown
1. Primer paso
2. Segundo paso
3. Tercer paso
```


