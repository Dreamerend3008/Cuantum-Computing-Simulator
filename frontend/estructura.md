```text
frontend/
├── public/
│   ├── logo.png             # Tu koala minimalista
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── ui/
│   │   │   ├── Navbar.astro
│   │   │   ├── Footer.astro
│   │   │   └── Button.astro
│   │   ├── simulator/        # Componentes específicos del simulador
│   │   │   ├── CircuitBoard.astro
│   │   │   ├── Toolbox.astro    # Puertas cuánticas (H, X, CNOT...)
│   │   │   └── ResultsPanel.astro
│   │   └── theory/           # Componentes de apoyo para la teoría
│   │       └── ConceptCard.astro
│   ├── content/              # Para manejar los textos de teoría sin ensuciar el código
│   │   └── theory/
│   │       ├── introduccion.md
│   │       └── compuertas-basicas.md
│   ├── layouts/
│   │   └── Layout.astro      # El que ya tienes con los colores y el bloqueo de scroll
│   ├── pages/
│   │   ├── index.astro       # El Hero que acabamos de hacer
│   │   ├── simulador.astro   # Página del simulador interactivo
│   │   └── teoria/
│   │       ├── index.astro   # Listado de temas de teoría
│   │       └── [slug].astro  # Página dinámica para cada lección de teoría
│   ├── styles/
│   │   └── global.css        # Variables de color y fuentes
│   └── utils/
│       └── quantum-logic.js  # Aquí irá la matemática de los qubits (puertas, matrices)
├── astro.config.mjs
└── package.json
```