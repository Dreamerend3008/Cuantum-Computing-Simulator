---
title: Leer resultados de la simulación
description: Probabilidades, estado cuántico y cómo interpretar las salidas.
order: 4
---

Después de montar un circuito en el simulador y pulsar ejecutar, Kuantum te mostrará algún tipo de **salida numérica o gráfica**. Esta lección explica qué significan las dos formas habituales de presentar resultados, sin depender de cómo esté dibujada la interfaz concreta.

## Dos formas de ver el mismo circuito

### 1. Varias ejecuciones (a menudo llamado “shots”)

El simulador **repite** el circuito muchas veces (cientos o miles). En cada repetición **mide** los qubits al final y anota una cadena de bits, por ejemplo `0`, `1`, `00`, `11`.

Al terminar obtienes **conteos** o **probabilidades**:

| Lectura | Significado |
|---------|-------------|
| `0` → 512, `1` → 512 (de 1024 ejecuciones) | ~50 % / 50 % para un qubit con **H** |
| Solo `00` y `11` en un Bell | Entrelazamiento; no deberían aparecer `01` ni `10` |

**Cuándo usarlo:** cuando quieres comportamiento parecido a un experimento repetido o comparar con probabilidades teóricas.

**Qué tener en cuenta:** con pocas ejecuciones los porcentajes **fluctúan**; con más ejecuciones se acercan a los valores ideales.

### 2. Estado cuántico completo (a menudo “statevector”)

En lugar de muchas mediciones, el simulador muestra las **amplitudes** del estado antes de (o sin) resumir en estadísticas. Para *n* qubits hay 2^*n* componentes posibles (|00⟩, |01⟩, …).

Cada amplitud es un número (en general complejo); la **probabilidad** de medir esa cadena es el **cuadrado del valor absoluto** de su amplitud.

**Cuándo usarlo:** para ver con precisión si un estado es superposición, entrelazado o tiene amplitudes nulas en ciertas bases.

**Qué tener en cuenta:** no es una tabla de “cuántas veces salió cada resultado”; es la descripción matemática del estado en ese momento.

## Cómo leer una tabla de probabilidades

Si la salida es del estilo:

```
00: 0.50
11: 0.50
```

Significa: al medir, ~50 % de las veces `00` y ~50 % `11`. Las claves son cadenas de **0** y **1**, una posición por qubit (el orden concreto lo indicará la interfaz de vuestro equipo; lo habitual es alinearlo con la numeración 0, 1, …).

Si aparece una sola clave con probabilidad 1 (o ~100 %), el estado medido es **determinista** en esa base: por ejemplo solo `0` tras preparar |0⟩ sin puertas, o solo `1` tras **X** desde |0⟩.

## Relación con circuitos que ya conoces

| Circuito | Tipo de salida útil | Qué esperar |
|----------|---------------------|-------------|
| 1 qubit, \|0⟩, sin puertas | Cualquiera | Solo `0` |
| 1 qubit + **H** | Shots o statevector | ~50 % `0` y ~50 % `1` (shots); amplitudes iguales en statevector |
| Bell (2 qubits) | Shots | ~50 % `00`, ~50 % `11`, resto ~0 |
| Bell | Statevector | Amplitudes no nulas solo en \|00⟩ y \|11⟩ |

## Ruido (simulación realista)

Algunos simuladores permiten añadir **ruido**: pequeñas imperfecciones que alejan el resultado del ideal. Si activáis algo como “depolarizing” o “thermal relaxation”, las probabilidades pueden **apartarse** ligeramente del 50/50 perfecto aunque el circuito sea el mismo.

Interpretación: no es que el circuito esté mal montado; es un modelo de hardware imperfecto.

## Cuando algo “no cuadra”

Revisa en este orden:

1. **Número de qubits** coherente con las puertas (con 2 qubits, solo índices 0 y 1).  
2. **Orden de las puertas** (en Bell: **H** antes que **CX**).  
3. **Control y objetivo** en **CX** (para Bell estándar: control = qubit 0).  
4. **Tipo de resultado:** ¿estás comparando muchas ejecuciones con amplitudes exactas? No son la misma vista.  
5. **Pocas ejecuciones:** en modo repetido, espera variación; aumenta el número de repeticiones si la interfaz lo permite.

## Practicar

1. Simula **H** en un qubit y anota las probabilidades de `0` y `1`.  
2. Simula el [circuito de Bell](/teoria/circuito-bell/) y comprueba que solo aparecen `00` y `11`.  
3. Si el simulador ofrece ambos modos, repite el mismo circuito en “varias ejecuciones” y en “estado completo” y relaciona ambas vistas con esta lección.
