---
title: Introducción a la computación cuántica
description: Qubits, circuitos y nociones básicas para usar Kuantum.
order: 1
---

## ¿Qué es un qubit?

En un bit clásico el valor es **0** o **1**. Un **qubit** (quantum bit) puede prepararse en una combinación de ambos estados. Lo habitual es escribirlo así:

|0⟩ y |1⟩

Un estado general se escribe **α|0⟩ + β|1⟩**, donde α y β son números complejos y |α|² + |β|² = 1. Al **medir**, solo verás 0 o 1; las probabilidades son |α|² y |β|².

En Kuantum prepararás cada qubit en |0⟩ o |1⟩ antes de aplicar puertas. Con varios qubits, el estado inicial se describe como una secuencia de ceros y unos (por ejemplo `00` = ambos en |0⟩).

## ¿Qué es un circuito cuántico?

Un circuito es una secuencia de **puertas** aplicadas a uno o más qubits:

- Cada **línea horizontal** es un qubit.
- Las **puertas** se aplican en orden (de izquierda a derecha en los diagramas habituales).
- Algunas puertas actúan sobre varios qubits a la vez (por ejemplo **CX**, también llamada CNOT).

El **simulador** de Kuantum servirá para montar ese circuito de forma visual. En la práctica: eliges cuántos qubits hay, colocas puertas y ejecutas la simulación para ver el resultado.

## Cómo se numeran los qubits

En la mayoría de herramientas cuánticas —incluido Kuantum— el **primer** qubit es el **0**, el segundo es el **1**, y así sucesivamente:

| Orden habitual | Índice |
|----------------|--------|
| Primer qubit   | 0      |
| Segundo qubit  | 1      |
| Tercer qubit   | 2      |

Si el circuito tiene **2 qubits**, solo existen los índices **0** y **1**. Referirse a un “tercer qubit” en ese caso no tiene sentido y la simulación no podrá ejecutarse correctamente.

## Medición y tipos de resultado

Según cómo quieras ver el resultado, Kuantum podrá ofrecer enfoques como estos (los nombres exactos en pantalla los definirá la interfaz gráfica):

- **Varias ejecuciones (estilo “shots”):** el circuito se corre muchas veces y obtienes **probabilidades** de leer cada cadena de bits (por ejemplo 50 % `0` y 50 % `1` con un qubit en superposición).
- **Estado completo (estilo “statevector”):** ves las **amplitudes** del estado cuántico antes de resumirlo en estadísticas de medición.

En el primer caso suele medirse al final; en el segundo se trabaja con el estado sin pasar por muchas mediciones repetidas.

## Primer experimento sugerido

Cuando uses el simulador, un buen primer paso es:

1. Un circuito de **1 qubit** preparado en |0⟩.
2. Aplicar la puerta **H** (Hadamard) a ese qubit.
3. Ejecutar la simulación y observar el resultado.

La puerta **H** lleva |0⟩ a una superposición equilibrada entre |0⟩ y |1⟩: es el ejemplo más simple para ver probabilidades distintas de 0 % y 100 %.

Continúa con [Compuertas básicas](/teoria/compuertas-basicas/), el [circuito de Bell](/teoria/circuito-bell/) y [Leer resultados de la simulación](/teoria/leer-resultados/).
