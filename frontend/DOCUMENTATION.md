# Documentación del Frontend: Kuantum Simulator

Bienvenido a la documentación técnica del frontend de Kuantum. Este documento sirve como fuente única de verdad para desarrolladores y diseñadores sobre la arquitectura, convenciones y decisiones de diseño de la interfaz de usuario.

---

## 📂 Estructura del Proyecto

El proyecto sigue una estructura modular basada en las convenciones de Astro.

```text
frontend/
├── public/                 # Assets estáticos (imágenes, favicon, fuentes locales)
│   ├── logo.png
│   └── favicon.svg
├── src/                    # Código fuente principal
│   ├── components/         # Componentes de Astro divididos por contexto
│   │   ├── ui/             # Componentes de interfaz general (Navbar, Footer, Botones)
│   │   ├── simulator/      # Componentes del simulador (CircuitBoard, Toolbox)
│   │   └── theory/         # Componentes para lecciones (ConceptCard)
│   ├── content/            # Colecciones de contenido (Markdown para lecciones de teoría)
│   ├── layouts/            # Plantillas base (Layout.astro)
│   ├── pages/              # Enrutamiento basado en archivos (index.astro, teoria/, simulador/)
│   └── utils/              # Funciones auxiliares y lógica del simulador cuántico
├── astro.config.mjs        # Configuración del framework Astro
└── package.json            # Dependencias y scripts
```

**Convenciones de archivos:**
*   Los componentes y layouts usan PascalCase (ej: `ConceptCard.astro`, `Layout.astro`).
*   Las páginas y directorios usan kebab-case (ej: `index.astro`, `simulador.astro`).

---

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Propósito |
| :--- | :--- | :--- |
| **Astro** | `^6.3.1` | Framework principal. Elegido por su rendimiento, arquitectura de islas, y soporte nativo para colecciones de Markdown. |
| **Node.js** | `>=22.12.0` | Entorno de ejecución requerido. |
| **CSS Nativo** | N/A | Estilos scopeados y globales mediante variables CSS. Evita sobrecarga de frameworks adicionales y ofrece flexibilidad. |

---

## 🏗️ Patrones y Arquitectura

*   **Arquitectura de Islas (Astro):** El HTML es renderizado en el servidor por defecto para máxima velocidad. Solo se envía JavaScript al cliente cuando es estrictamente necesario (ej: toggle del tema, simulador interactivo).
*   **Gestión de Contenido (Content Collections):** Toda la teoría se gestiona mediante archivos Markdown (`.md`) en la carpeta `src/content/`. Esto separa la presentación (Astro) de la información.
*   **Estado y Flujo de Datos:** En componentes estáticos o de UI, los datos fluyen de arriba hacia abajo a través de `Astro.props`.
*   **Enrutamiento:** Basado en el sistema de archivos de Astro dentro de `src/pages/`. Soporta rutas dinámicas como `src/pages/teoria/[slug].astro`.

---

## 🎨 Guía de Estilo

El proyecto utiliza un sistema de variables de diseño estandarizado enfocado exclusivamente en un **Modo Claro**. Las variables CSS globales se definen en `Layout.astro`.

### Paleta de Colores

| Variable CSS | Valor HEX | Uso Principal |
| :--- | :--- | :--- |
| `--bg-color` | `#F0F1F1` | Fondo principal de la aplicación. |
| `--text-main` | `#2C3E50` | Color del texto general y títulos. |
| `--koala-grey` | `#808e8f` | Textos secundarios, descripciones, bordes sutiles. |
| `--primary-blue` | `#2596be` | Fondos de navegación, tarjetas, y énfasis de la marca. |
| `--accent-pink` | `#e938b0` | Botones principales (Call to Action), links de énfasis, efectos hover en títulos. |
| `--accent-orange`| `#f99b0f` | Acentos secundarios y elementos interactivos. |
| `--accent-yellow`| `#fdf715` | Elementos de advertencia o destacados especiales. |
| `--accent-green` | `#73fd3d` | Elementos de éxito y validaciones. |
| `--accent-purple`| `#8E44AD` | Elementos teóricos y detalles adicionales. |

### Tipografía

*   **Títulos (`h1` - `h6`, Títulos principales):** `Quicksand`, sans-serif. Pesos: 500, 700, 900.
*   **Cuerpo (Textos generales, botones):** `Inter`, sans-serif. Pesos: 400, 500, 600.

### Elementos Visuales

*   **Sombras:** Usadas sutilmente para elevar componentes al hacer hover. Ej: `box-shadow: 0 4px 14px rgba(233, 56, 176, 0.3);`.
*   **Bordes y Radios:** Bordes redondeados estandarizados (ej: `border-radius: 8px` en botones y `12px` en tarjetas).
*   **Transiciones:** Animaciones suaves para colores y transformaciones (ej: `transition: all 0.3s ease`).

---

## 🧩 Componentes Reutilizables

### `ConceptCard.astro` (src/components/theory/ConceptCard.astro)
Tarjeta para mostrar lecciones de teoría.
**Props:**
*   `title` (string): Título de la tarjeta.
*   `description` (string): Breve descripción de la lección.
*   `href` (string, opcional): URL a la que dirige la lección.
*   `comingSoon` (boolean, opcional, por defecto `false`): Si es `true`, deshabilita el enlace y muestra el badge "Próximamente".

### `Layout.astro` (src/components/layouts/Layout.astro)
Plantilla principal que envuelve cada página, define metaetiquetas, fuentes y estructura del DOM (Navbar + Main + Footer).
**Props:**
*   `title` (string): Título de la página (para el tag `<title>`).
*   `showNavAndFooter` (boolean, opcional, por defecto `true`): Oculta la navegación y el pie de página (útil para landing pages completas como el Hero).

---

## 📝 Convenciones de Código

1.  **Componentes (.astro):** Dividir la lógica de servidor en el bloque superior (`---`), el HTML en el medio, y los estilos en la parte inferior (`<style>`).
2.  **CSS Scopeado:** Los estilos definidos dentro de un componente `<style>` solo afectan a ese componente, previniendo choques de estilos.
3.  **CSS Global:** Utilizar `<style is:global>` únicamente en el `Layout.astro` principal para variables CSS y reseteos generales (como el `overflow: hidden` global si es requerido o el cambio de temas).
4.  **Importaciones:** Agrupar importaciones de Astro/Layouts al inicio, seguido de componentes, y finalmente utilidades o datos.

---

## 🎨 Temas y Configuración

El proyecto ha sido estandarizado para operar en una **identidad visual unificada (Modo Claro)**, eliminando la complejidad del cambio de temas dinámicos. Esto asegura consistencia en el espaciado, tipografía y paleta de colores en todas las vistas.
Todas las variables de configuración de la UI (colores y tipografía) están centralizadas en el bloque `<style is:global>` de `Layout.astro`. No se deben usar colores "sueltos" en código, sino siempre referenciar a estas variables (e.g. `var(--accent-pink)`).

---

## 📦 Dependencias Críticas

| Dependencia | Propósito en el Proyecto |
| :--- | :--- |
| `astro` | Orquestador de la aplicación, empaquetador, enrutador y motor de renderizado. Maneja la construcción de los SSG (Static Site Generation) o SSR según se configure. |

---

## 🚀 Guía de Cómo Empezar

Para correr el proyecto localmente y empezar a desarrollar:

1.  **Navegar al directorio:**
    ```bash
    cd frontend
    ```
2.  **Instalar dependencias:**
    ```bash
    npm install
    ```
3.  **Iniciar el servidor de desarrollo:**
    ```bash
    npm run dev
    ```
    *(El proyecto correrá en `http://localhost:4321` por defecto)*

4.  **Construir para producción:**
    ```bash
    npm run build
    ```
    Generará una carpeta `dist/` con la versión estática y minificada del sitio.

5.  **Previsualizar producción:**
    ```bash
    npm run preview
    ```

**¿Dónde encontrar ejemplos?**
*   **Hero / Landing:** `src/pages/index.astro`.
*   **Layout Base:** `src/layouts/Layout.astro`.
*   **Componente Complejo:** `src/components/ui/Navbar.astro` (contiene lógica JS de cliente).
