---
title: Introducción a la computación cuántica
description: Qubits y nociones básicas para usar Kuantum.
order: 1
---

La computación cuántica usa **qubits** en lugar de bits clásicos. Un bit clásico solo puede tener el valor **0** o **1**. Un qubit también puede medirse como 0 o 1, pero antes de medirlo puede estar en una **superposición** de ambos estados.

> **Recuerda:** En Kuantum prepararás qubits, aplicarás compuertas y ejecutarás una simulación para observar probabilidades o estados resultantes.

---

## ¿Qué es un qubit?

Un **qubit** (quantum bit) es la unidad básica de información cuántica. Sus dos estados base se escriben como:

| Estado | Significado |
|--------|-------------|
| **\|0⟩** | Estado base cero |
| **\|1⟩** | Estado base uno |

Un estado general se escribe como **α\|0⟩ + β\|1⟩**, donde **α** y **β** son amplitudes. Esas amplitudes indican qué tan probable es obtener 0 o 1 al medir.

| Amplitud | Probabilidad asociada |
|----------|-----------------------|
| **α** | Probabilidad de medir **\|0⟩**: **\|α\|²** |
| **β** | Probabilidad de medir **\|1⟩**: **\|β\|²** |

Para que el estado sea válido, las probabilidades deben sumar 1:

**\|α\|² + \|β\|² = 1**

---

## Superposición

Un qubit no tiene que estar completamente en **\|0⟩** o completamente en **\|1⟩**. Puede estar en una combinación de ambos. Por ejemplo, después de aplicar una puerta **H** (Hadamard) a un qubit en **\|0⟩**, el resultado tiene la misma probabilidad de medirse como 0 o como 1.

| Estado antes | Operación | Resultado esperado al medir |
|--------------|-----------|-----------------------------|
| **\|0⟩** | **H** | 50% **0** y 50% **1** |
| **\|1⟩** | **H** | 50% **0** y 50% **1**, con diferencia de fase |

**Analogía:** Es como una moneda en el aire: todavía no ha caído en cara o cruz, pero ambas posibilidades participan en el resultado.

---

## La esfera de Bloch

La **esfera de Bloch** es una forma visual de representar el estado de un qubit. En la imagen, cada dirección que puede tomar el vector representa un estado posible del qubit.

![Representación de un qubit en la esfera de Bloch](/images/theory/bloch-sphere.png)

| Parte de la esfera | Qué representa |
|--------------------|----------------|
| **Polo norte** | Estado **\|0⟩** |
| **Polo sur** | Estado **\|1⟩** |
| **Ecuador** | Superposiciones equilibradas entre **\|0⟩** y **\|1⟩** |
| **Más cerca del polo norte** | Mayor probabilidad de medir **0** |
| **Más cerca del polo sur** | Mayor probabilidad de medir **1** |
| **Giro alrededor del eje vertical** | Cambio de fase del qubit |

---

## Fase de un qubit

Además de las probabilidades, un qubit tiene **fase**. La fase describe hacia qué lado apunta el vector cuando gira alrededor del eje vertical de la esfera de Bloch. Dos qubits pueden estar a la misma altura en la esfera, y por eso tener la misma probabilidad de medirse como **0** o **1**, pero apuntar hacia lados distintos. Esa diferencia es la fase.

| Cambio | Qué ocurre |
|--------|------------|
| Cambiar amplitudes | Cambia las probabilidades de medir 0 o 1 |
| Cambiar fase | Puede no cambiar las probabilidades inmediatamente, pero afecta futuras operaciones |

> **Importante:** Dos estados pueden tener las mismas probabilidades de medición y aun así comportarse distinto por su fase.

