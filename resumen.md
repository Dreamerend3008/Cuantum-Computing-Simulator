# Resumen de APIs

**Base API:** todas las rutas están bajo `/api`.

## POST `/api/circuits/`
**Descripción:** crea/guarda un circuito (sin validación de esquema).

**Entrada JSON:** cualquier objeto (`dict`).

**Salida JSON:**
```json
{"message":"Circuit Saved :D"}
```

## POST `/api/simulations/`
**Descripción:** crea/guarda una simulación (sin validación de esquema).

**Entrada JSON:** cualquier objeto (`dict`).

**Salida JSON:**
```json
{"message":"Simulation saved"}
```

## POST `/api/simulations/run`
**Descripción:** ejecuta la simulación.

**Entrada JSON (schema real):**
```json
{
  "initial_state": "0101",
  "num_qubits": 4,
  "instructions": [
    {"name": "H", "qubits": [0]},
    {"name": "CX", "qubits": [0, 1]},
    {"name": "MEASURE_ALL"}
  ],
  "shots": 1024,
  "num_clbits": 4,
  "noise_model": "depolarizing",
  "runner_mode": "shot"
}
```

**Salida JSON (éxito):**
```json
{
  "status": "success",
  "data": {
    "probabilities": {
      "0000": 0.5,
      "1111": 0.5
    }
  }
}
```

**Salida JSON (error):**
```json
{"detail":"<mensaje de error>"}
```
