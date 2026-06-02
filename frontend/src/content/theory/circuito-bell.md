---
title: Circuito de Bell
description: Entrelazamiento con Hadamard y CNOT en dos qubits.
order: 3
---

El **estado de Bell** es el ejemplo clásico de **entrelazamiento**: dos qubits quedan correlacionados de forma que medir uno condiciona el otro, aunque no hayan “intercambiado” información de forma clásica.

Es un circuito corto y muy usado para comprobar que el simulador funciona bien con puertas de uno y dos qubits.

## El circuito

Con **2 qubits**, ambos preparados al inicio en |0⟩ (estado inicial `00`):

1. Aplicar **H** al qubit **0** (el primero).  
2. Aplicar **CX** con **control** en el qubit **0** y **objetivo** en el qubit **1**.

En notación compacta: **H** en 0, luego **CX**(0 → 1).

## Qué ocurre paso a paso

**Tras H en el qubit 0**

- Qubit 0 queda en superposición (|0⟩ + |1⟩) / √2.  
- Qubit 1 sigue en |0⟩.  
- Estado conjunto aproximado: (|00⟩ + |10⟩) / √2.

**Tras CX (control 0, objetivo 1)**

- Cuando el control “ve” |1⟩, invierte el objetivo.  
- El estado pasa a una superposición de |00⟩ y |11⟩:  
  **(|00⟩ + |11⟩) / √2**

Eso es un estado de Bell: **nunca** obtendrás `01` ni `10` al medir ambos qubits a la vez.

## Qué deberías ver al simular

Si ejecutas el circuito **muchas veces** y mides ambos qubits al final:

| Resultado | Probabilidad aproximada |
|-----------|-------------------------|
| `00` | ~50 % |
| `11` | ~50 % |
| `01` | ~0 % |
| `10` | ~0 % |

Los valores exactos pueden variar ligeramente por estadística de muestreo; con suficientes ejecuciones deberías ver solo `00` y `11`.

Si en cambio consultas el **estado cuántico completo** (sin resumir en muchas mediciones), verás amplitudes concentradas en las componentes |00⟩ y |11⟩.

## Errores habituales al montarlo

- **Invertir control y objetivo en CX** cambia el circuito; para el Bell estándar el control es el qubit que ya lleva **H** (el 0).  
- **Usar solo un qubit** o índices fuera de rango (con 2 qubits solo existen 0 y 1).  
- **Confundir el orden de las puertas:** primero **H**, después **CX**.

## Otro ejemplo corto: superposición en un qubit

Antes del Bell, conviene dominar un circuito de **1 qubit**:

- Estado inicial |0⟩.  
- Puerta **H**.  
- Resultado: ~50 % al medir 0 y ~50 % al medir 1.

No hay entrelazamiento aquí; solo un qubit en superposición. El Bell añade el segundo qubit y la correlación.

## Practicar

Monta en el simulador el circuito de Bell descrito arriba (2 qubits, **H** en 0, **CX** 0→1) y compara con la tabla de resultados. Después puedes leer [Leer resultados de la simulación](/teoria/leer-resultados/) para interpretar lo que muestra la interfaz.
