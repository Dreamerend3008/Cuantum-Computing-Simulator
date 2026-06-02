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
 
### RX — Rotación alrededor del eje X
 
![Diagrama de la puerta RX](/images/theory/rx-gate.png)
 
**¿Para qué sirve?**
Rota el estado del qubit un **ángulo θ** alrededor del eje X. Puedes controlar exactamente cuánto lo rotas, lo que la hace muy flexible.
 
**Parámetros de entrada:**
- 1 qubit
- Un ángulo **θ** (en radianes)

| Caso especial | Equivale a |
|---------------|------------|
| **θ = π** (180°) | **Puerta X** |
| **θ = π/2** (90°) | **Media rotación X** |
 
---
 
### RY — Rotación alrededor del eje Y
 
![Diagrama de la puerta RY](/images/theory/ry-gate.png)
 
**¿Para qué sirve?**
Rota el estado del qubit un **ángulo θ** alrededor del eje Y. Es útil para preparar estados con probabilidades controladas (no necesariamente 50/50).
 
**Parámetros de entrada:**
- 1 qubit
- Un ángulo **θ** (en radianes)

| Caso especial | Equivale a |
|---------------|------------|
| **θ = π** (180°) | **Puerta Y** |
 
---
 
### RZ — Rotación alrededor del eje Z
 
![Diagrama de la puerta RZ](/images/theory/rz-gate.png)
 
**¿Para qué sirve?**
Rota la **fase** del qubit un ángulo θ alrededor del eje Z. No cambia las probabilidades de medir \|0⟩ o \|1⟩, solo afecta la fase.
 
**Parámetros de entrada:**
- 1 qubit
- Un ángulo **θ** (en radianes)

| Caso especial | Equivale a |
|---------------|------------|
| **θ = π** (180°) | **Puerta Z** |
| **θ = π/2** (90°) | **Puerta S** |
| **θ = π/4** (45°) | **Puerta T** |
 
---
 
## Compuertas de dos qubits
 
Estas compuertas toman **dos qubits como entrada** y devuelven **dos qubits como salida**. Uno de los qubits actúa como **control** y el otro como **objetivo**.
 
---
 
### CX — Puerta CNOT (NOT Controlado)
 
![Diagrama de la puerta CX](/images/theory/cx-gate.png)
 
**¿Para qué sirve?**
Es la compuerta de dos qubits más importante. Aplica una puerta X (NOT) al qubit objetivo **solo si** el qubit de control está en \|1⟩. Se usa para crear **entrelazamiento** entre qubits.
 
**Entradas:**
- **Qubit de control:** decide si se aplica la operación
- **Qubit objetivo:** el que puede ser invertido

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
 
---
 
## Compuertas de tres qubits
 
---
 
### CCX — Puerta Toffoli (NOT Doblemente Controlado)
 
![Diagrama de la puerta CCX](/images/theory/ccx-gate.png)
 
**¿Para qué sirve?**
Es como la puerta CX, pero con **dos qubits de control**. Aplica una puerta X al qubit objetivo **solo si ambos** qubits de control están en \|1⟩. Es una compuerta universal: con ella se puede simular cualquier circuito clásico.
 
**Entradas:**
- **Qubit de control 1**
- **Qubit de control 2**
- **Qubit objetivo**

| Control 1 | Control 2 | Objetivo (entrada) | Objetivo (salida) |
|-----------|-----------|-------------------|------------------|
| **\|0⟩** | **cualquiera** | **cualquiera** | **sin cambio** |
| **cualquiera** | **\|0⟩** | **cualquiera** | **sin cambio** |
| **\|1⟩** | **\|1⟩** | **\|0⟩** | **\|1⟩** (invertido) |
| **\|1⟩** | **\|1⟩** | **\|1⟩** | **\|0⟩** (invertido) |
 
---
 
## Resumen rápido
 
| Compuerta | Qubits | ¿Qué hace? |
|-----------|--------|-----------|
| **H** | 1 | Crea superposición |
| **X** | 1 | Invierte el estado (NOT cuántico) |
| **Y** | 1 | Invierte el estado con cambio de fase |
| **Z** | 1 | Cambia la fase del estado \|1⟩ |
| **S** | 1 | Gira la fase 90° |
| **T** | 1 | Gira la fase 45° |
| **RX** | 1 + ángulo θ | Rota alrededor del eje X |
| **RY** | 1 + ángulo θ | Rota alrededor del eje Y |
| **RZ** | 1 + ángulo θ | Rota la fase alrededor del eje Z |
| **CX** | 2 | NOT controlado (crea entrelazamiento) |
| **SWAP** | 2 | Intercambia los estados de dos qubits |
| **CCX** | 3 | NOT doblemente controlado (Toffoli) |

Siguiente paso: combinar **H** y **CX** en el [circuito de Bell](/teoria/circuito-bell/).
