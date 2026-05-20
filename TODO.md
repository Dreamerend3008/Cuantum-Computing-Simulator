# TODO — Conectar frontend (Astro) con backend (FastAPI)

- [ ] **Levantar ambos servidores y confirmar rutas.**  
  Backend: `python3 backend/main.py` (puerto 8000). Frontend: `npm run dev` en `frontend/` (puerto 4321).  
  Rutas disponibles del backend (prefijo `/api`):
  - `POST /api/circuits/` 
  - `POST /api/simulations/`
  - `POST /api/simulations/run`

- [ ] **Habilitar CORS en el backend para el origen del frontend.**  
  En `backend/main.py`, agregar `CORSMiddleware` con `allow_origins = ["http://localhost:4321"]` (y el dominio real si despliegas).  
  Sin esto, el navegador bloqueará las llamadas.

- [ ] **Definir la URL base del API en el frontend.**  
  Crear `frontend/.env` (o `.env.local`) con:  
  `PUBLIC_API_BASE_URL=http://localhost:8000/api`  
  En Astro, solo las variables que empiezan con `PUBLIC_` llegan al cliente.

- [ ] **Crear un cliente API reutilizable en el frontend.**  
  Archivo sugerido: `frontend/src/utils/api.ts` (o `.js`).  
  Funciones mínimas:
  - `runSimulation(payload)` → `POST ${API_BASE}/simulations/run`
  - `saveCircuit(payload)` → `POST ${API_BASE}/circuits/` (si vas a guardar circuitos)

- [ ] **Construir el `CircuitInput` en la página del simulador.**  
  En `frontend/src/pages/simulador.astro`, agregar UI para:
  - `num_qubits` (>= 1)
  - `initial_state` (string de longitud `num_qubits` con solo `0`/`1`)
  - `instructions` (lista de puertas con formato `{ name, qubits, params?, clbits? }`)
  - `runner_mode` ("shot" o "statevector")
  - `shots` (>= 1, solo si `runner_mode === "shot"`)
  - `num_clbits` (>= 0)
  - `noise_model` (`"depolarizing" | "thermal_relaxation" | null`)

- [ ] **Respetar el formato de instrucciones soportado por el backend.**  
  Nombres válidos (`name`) en `backend/core/gate_mapper.py`:
  `H, X, Y, Z, S, T, RX, RY, RZ, CX, SWAP, CXX, HALF_ADD, FULL_ADD, OLD_FULL_ADD, QFT, IQFT, INITIALIZE`  
  - Para `RX/RY/RZ/INITIALIZE`, usar `params` (ej. `{ name:"RX", qubits:[0], params:[1.5708] }`).  
  - Los qubits son **0-indexados**.

- [ ] **No enviar mediciones desde el frontend en modo `shot`.**  
  El backend agrega `MEASURE_ALL` automáticamente en `CircuitInput.dict_builder()`.  
  Para `statevector`, no incluyas mediciones.

- [ ] **Ejemplo de payload válido para `/api/simulations/run`.**
  ```json
  {
    "initial_state": "00",
    "num_qubits": 2,
    "instructions": [
      { "name": "H", "qubits": [0] },
      { "name": "CX", "qubits": [0, 1] }
    ],
    "shots": 1024,
    "num_clbits": 2,
    "noise_model": null,
    "runner_mode": "shot"
  }
  ```

- [ ] **Manejar la respuesta en el frontend.**  
  Respuesta exitosa:
  ```json
  { "status": "success", "data": { "measure": {}, "real_probabilities": {}, "state_vector": null } }
  ```
  - En `shot`: `measure` trae conteos y `real_probabilities` probabilidades.  
  - En `statevector`: `measure` llega vacío y `real_probabilities` se calcula desde amplitudes.

- [ ] **Manejo de errores y validaciones.**  
  - `400` si el circuito no es válido para el simulador.  
  - `422` si el input es inválido.  
  Mostrar `detail` en la UI y validar inputs antes de enviar.

- [ ] **(Opcional) Definir persistencia de circuitos.**  
  `POST /api/circuits/` hoy solo devuelve un mensaje.  
  Si quieres guardar circuitos, define un esquema, almacén (archivo/DB) y devuelve un `id`.
