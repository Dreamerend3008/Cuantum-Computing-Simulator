---
title: Compuertas Básicas
description: Aprende qué hacen las compuertas cuánticas más comunes y cómo transforman los qubits
order: 2
---
 
Las compuertas cuánticas son las operaciones básicas de la computación cuántica. Funcionan de manera similar a las compuertas lógicas clásicas (AND, OR, NOT), pero operan sobre **qubits** y pueden hacer cosas que las compuertas clásicas no pueden, como crear superposición y entrelazamiento.
 
> **Recuerda:** Un qubit puede estar en el estado \|0⟩, en el estado \|1⟩, o en una **superposición** de ambos al mismo tiempo. Las compuertas transforman ese estado.
 
---
 
## Compuertas de un solo qubit
 
Estas compuertas toman **un qubit como entrada** y devuelven **un qubit como salida**.
 
---
 
### H — Puerta Hadamard
 
![Diagrama de la puerta Hadamard](/images/theory/hadamard-gate.png)
 
**¿Para qué sirve?**

Es una de las compuertas más importantes. Crea **superposición**: convierte un qubit que está en un estado definido (\|0⟩ o \|1⟩) en un qubit que está en ambos estados a la vez, con igual probabilidad.
 
| Entrada | Salida |
|---------|--------|
| **\|0⟩** | **Superposición de \|0⟩ y \|1⟩** (50% / 50%) |
| **\|1⟩** | **Superposición de \|0⟩ y \|1⟩** (50% / 50%, con diferencia de fase) |
 
**Analogía:** Es como lanzar una moneda al aire: mientras está en el aire, no es cara ni cruz, sino ambas posibilidades al mismo tiempo.
 
---
 
### X — Puerta NOT (Pauli-X)
 
![Diagrama de la puerta X](/images/theory/x-gate.png)
 
**¿Para qué sirve?**

Es el equivalente cuántico del NOT clásico. **Invierte** el estado del qubit: cambia \|0⟩ por \|1⟩ y viceversa.
 
| Entrada | Salida |
|---------|--------|
| \|0⟩ | \|1⟩ |
| \|1⟩ | \|0⟩ |
 
**Analogía:** Como apagar una luz encendida, o encender una luz apagada.
 
---
 
### Y — Puerta Pauli-Y
 
![Diagrama de la puerta Y](/images/theory/y-gate.png)
 
**¿Para qué sirve?**

Combina una inversión del estado (como X) con un cambio de fase. Es menos intuitiva para principiantes, pero es fundamental en muchos algoritmos cuánticos.
 
| Entrada | Salida |
|---------|--------|
| **\|0⟩** | **\|1⟩** (con cambio de fase) |
| **\|1⟩** | **\|0⟩** (con cambio de fase) |
 
---
 
### Z — Puerta Pauli-Z
 
![Diagrama de la puerta Z](/images/theory/z-gate.png)
 
**¿Para qué sirve?**

No cambia si el qubit es \|0⟩ o \|1⟩, pero **cambia la fase** del estado \|1⟩.
 
| Entrada | Salida |
|---------|--------|
| **\|0⟩** | **\|0⟩** (sin cambio) |
| **\|1⟩** | **\|1⟩** (con fase invertida) |
 
---
 
### S — Puerta de Fase S
 
![Diagrama de la puerta S](/images/theory/s-gate.png)
 
**¿Para qué sirve?**

Aplica un **giro de fase de 90°** al estado \|1⟩. Es la mitad de la puerta Z (que gira 180°).
 
| Entrada | Salida |
|---------|--------|
| **\|0⟩** | **\|0⟩** (sin cambio) |
| **\|1⟩** | **\|1⟩** (con fase girada 90°) |
 
---
 
### T — Puerta T
 
![Diagrama de la puerta T](/images/theory/t-gate.png)
 
**¿Para qué sirve?**

Aplica un **giro de fase de 45°** al estado \|1⟩. Es la mitad de la puerta S. Se usa mucho para construir circuitos cuánticos universales.
 
| Entrada | Salida |
|---------|--------|
| **\|0⟩** | **\|0⟩** (sin cambio) |
| **\|1⟩** | **\|1⟩** (con fase girada 45°) |
 
---
 
## Compuertas de dos qubits
 
Estas compuertas toman **dos qubits como entrada** y devuelven **dos qubits como salida**. Uno de los qubits actúa como **control** y el otro como **objetivo**.
 
---
 
### CX — Puerta CNOT (NOT Controlado)
 
![Diagrama de la puerta CX](/images/theory/cx-gate.png)
 
**¿Para qué sirve?**

Es la compuerta de dos qubits más importante. Aplica una puerta X (NOT) al qubit objetivo **solo si** el qubit de control está en \|1⟩. Se usa para crear **entrelazamiento** entre qubits.
 
**Entradas:**
- **Qubit de control (línea con círculo pequeño):** decide si se aplica la operación
- **Qubit objetivo (línea con círculo grande):** el que puede ser invertido

| Control | Objetivo (entrada) | Objetivo (salida) |
|---------|-------------------|------------------|
| **\|0⟩** | **\|0⟩** | **\|0⟩** (sin cambio) |
| **\|0⟩** | **\|1⟩** | **\|1⟩** (sin cambio) |
| **\|1⟩** | **\|0⟩** | **\|1⟩** (invertido) |
| **\|1⟩** | **\|1⟩** | **\|0⟩** (invertido) |
 
---
 
### SWAP — Puerta de Intercambio
 
![Diagrama de la puerta SWAP](/images/theory/swap-gate.png)
 
**¿Para qué sirve?**

**Intercambia** los estados de dos qubits. El primer qubit pasa a tener el estado del segundo, y viceversa.
 
**Entradas:**
- **Qubit A** y **Qubit B**

| Qubit A (entrada) | Qubit B (entrada) | Qubit A (salida) | Qubit B (salida) |
|------------------|------------------|-----------------|-----------------|
| \|0⟩ | \|0⟩ | \|0⟩ | \|0⟩ |
| \|0⟩ | \|1⟩ | \|1⟩ | \|0⟩ |
| \|1⟩ | \|0⟩ | \|0⟩ | \|1⟩ |
| \|1⟩ | \|1⟩ | \|1⟩ | \|1⟩ |
 
