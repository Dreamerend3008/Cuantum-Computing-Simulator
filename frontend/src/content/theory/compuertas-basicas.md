---
title: Compuertas básicas
description: H, X, Y, Z, rotaciones y puertas de dos qubits que usa Kuantum.
order: 2
---

Esta lección repasa las puertas más habituales. En el simulador las colocarás sobre los qubits correspondientes; aquí importa **qué hace cada una** y **cuántos qubits** necesita.

Recuerda: el **primer qubit es el 0**, el segundo el 1, etc. (véase [Introducción](/teoria/introduccion/)).

## Puertas de un qubit

### H (Hadamard)

Crea **superposición**. Si el qubit está en |0⟩, tras **H** queda en una mezcla equilibrada de |0⟩ y |1⟩ (aproximadamente 50 % / 50 % al medir).

- **Qubits:** 1  
- **Uso típico:** primer paso para generar aleatoriedad cuántica o preparar entrelazamiento.

### X (Pauli-X)

Es el **NOT cuántico**: intercambia |0⟩ y |1⟩.

- **Qubits:** 1  
- **Uso típico:** poner un qubit en |1⟩ si empezaba en |0⟩, o invertir un bit ya preparado.

### Y e Z (Pauli-Y y Pauli-Z)

Actúan sobre **fase** y combinaciones de amplitud; no cambian las probabilidades de medir 0 o 1 en todos los casos, pero sí la información de fase del estado.

- **Qubits:** 1 cada una  
- **Uso típico:** algoritmos más avanzados; en circuitos introductorios **Z** aparece a menudo para marcar una diferencia de signo.

### S y T

Son **puertas de fase** (raíz de Z y raíz cuarta de Z). Son habituales en corrección de errores y algoritmos estándar.

- **Qubits:** 1 cada una  
- **Uso típico:** construcciones avanzadas; no son imprescindibles en tus primeros circuitos.

### RX, RY y RZ (rotaciones)

Giran el estado del qubit en torno a un eje. Llevan un **parámetro en radianes** (por ejemplo π ≈ 3.1416, π/2 ≈ 1.5708).

- **Qubits:** 1  
- **Uso típico:** ajustar ángulos con precisión; **RX(π/2)** o **RY(π/2)** pueden preparar superposiciones distintas de **H**.

## Puertas de dos o más qubits

### CX (CNOT)

**Controlado-NOT:** si el qubit de **control** está en |1⟩, aplica **X** al qubit **objetivo**; si el control está en |0⟩, no cambia el objetivo.

- **Qubits:** 2 (control, objetivo)  
- **Uso típico:** entrelazamiento, sumadores cuánticos, [circuito de Bell](/teoria/circuito-bell/).

Orden habitual al describirlo: “**CX** con control en el qubit 0 y objetivo en el qubit 1”.

### SWAP

Intercambia el estado de **dos** qubits.

- **Qubits:** 2  
- **Uso típico:** reordenar información en el circuito cuando las líneas no coinciden con la lógica que quieres.

### CXX (Toffoli)

Compuerta **controlada por dos qubits**: aplica **X** al objetivo solo si **ambos** controles están en |1⟩.

- **Qubits:** 3 (control 1, control 2, objetivo)  
- **Uso típico:** lógica reversible de tres qubits; nivel intermedio.

## Bloques compuestos (avanzado)

Kuantum también puede incluir bloques predefinidos como **QFT**, **IQFT**, sumadores (**HALF_ADD**, **FULL_ADD**) o **INITIALIZE** (preparar un estado concreto). Son circuitos hechos con puertas más simples por dentro; los verás en lecciones o ejemplos posteriores.

## Resumen rápido

| Puerta | Qubits | Idea en una frase |
|--------|--------|-------------------|
| H | 1 | Superposición |
| X | 1 | Invierte \|0⟩ ↔ \|1⟩ |
| Y, Z | 1 | Fase / Pauli |
| S, T | 1 | Fase fina |
| RX, RY, RZ | 1 | Rotación con ángulo |
| CX | 2 | NOT controlado |
| SWAP | 2 | Intercambia dos qubits |
| CXX | 3 | Toffoli |

## Practicar

En el simulador, prueba en este orden:

1. **X** sobre un qubit en |0⟩ → deberías obtener siempre |1⟩ (salvo medición en otro modo).  
2. **H** sobre |0⟩ → resultados repartidos entre 0 y 1.  
3. **CX** con control en |1⟩ y objetivo en |0⟩ → el objetivo pasa a |1⟩.

Siguiente paso natural: combinar **H** y **CX** en el [circuito de Bell](/teoria/circuito-bell/).
