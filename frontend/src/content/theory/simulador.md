---
title: Aprende a usar el simulador
description: Probabilidades, estado dominante, amplitudes y esfera de Bloch.
order: 3
---

> **Recuerda:** Un resultado cuántico no siempre es un único valor fijo. Muchas veces verás una distribución de probabilidades: algunos estados son más probables que otros.

---

## ¿Qué es un Clbit?

Un **Clbit** es un **bit clásico**. Sirve para guardar el resultado de medir un qubit.

| Elemento | Qué hace |
|----------|----------|
| **Qubit** | Guarda información cuántica antes de medir |
| **Clbit** | Guarda el resultado clásico después de medir: **0** o **1** |

Por ejemplo, si tienes **2 qubits** y quieres medir ambos, normalmente necesitas **2 clbits**: uno para guardar el resultado del primer qubit y otro para guardar el resultado del segundo.

---

## Modo Shot y modo Statevector

Kuantum permite elegir entre dos formas de ejecutar la simulación. Internamente no hacen exactamente lo mismo, pero ambas se resumen principalmente como **probabilidades**, por eso pueden verse muy parecidas en el visualizador.

| Modo | Qué calcula | Qué ves en esta pantalla |
|------|-------------|--------------------------|
| **Shot** | Ejecuta el circuito muchas veces y cuenta cuántas veces aparece cada resultado | Probabilidades estimadas a partir de muchas mediciones |
| **Statevector** | Calcula el estado cuántico ideal del circuito antes de medir | Probabilidades calculadas desde el estado ideal |

**¿Cuál usar?**
- Usa **Shot** cuando quieras simular una medición repetida, especialmente si activas ruido.
- Usa **Statevector** cuando quieras ver el resultado ideal del circuito sin variación por número de ejecuciones.

---

## Antes de ejecutar

En el panel de configuración defines cómo se ejecutará la simulación.

![Panel de configuración del simulador](/images/theory/simulation-config.png)

| Campo | Qué significa |
|-------|---------------|
| **Qubits** | Cantidad de qubits del circuito |
| **Clbits** | Cantidad de bits clásicos disponibles para medición |
| **Estado inicial** | Cadena inicial, por ejemplo **00** para dos qubits en **\|00⟩** |
| **Modo** | Tipo de simulación: **Shot** o **Statevector** |
| **Shots** | Número de ejecuciones repetidas cuando usas modo **Shot** |
| **Modelo de ruido** | Simula imperfecciones como ruido depolarizante o relajación térmica |

---

## Estado más probable

La primera tarjeta del resultado muestra el **estado más probable**. Es el estado que tiene la probabilidad más alta después de ejecutar el circuito.

![Tarjeta de estado más probable](/images/theory/result-dominant-state.png)

| Elemento | Cómo leerlo |
|----------|-------------|
| **Estado más probable** | La cadena de bits con mayor probabilidad, por ejemplo **\|00⟩** |
| **Porcentaje** | Qué tan probable es medir ese estado |

Si la tarjeta muestra **\|00⟩** con **100%**, significa que el circuito siempre termina en ese estado. Si muestra **\|0⟩** con **50%**, significa que ese estado es uno de los resultados posibles, pero no el único.

---

## Histograma de probabilidades

El histograma muestra todos los estados que pueden aparecer al medir el circuito y qué probabilidad tiene cada uno.

![Histograma de probabilidades](/images/theory/result-probability-histogram.png)

| Parte del histograma | Qué representa |
|----------------------|----------------|
| **Eje horizontal** | Estados posibles: **\|0⟩**, **\|1⟩**, **\|00⟩**, **\|01⟩**, etc. |
| **Eje vertical** | Probabilidad en porcentaje |
| **Barra más alta** | Resultado más probable |
| **Barras en 0%** | Estados que no deberían aparecer en la medición ideal |

**Ejemplo:** Si aplicas una puerta **H** a un qubit que empieza en **\|0⟩**, lo esperado es ver dos barras parecidas: una para **\|0⟩** y otra para **\|1⟩**, cada una cerca de **50%**.

---

## Tabla de amplitudes

La tabla de **Análisis de Amplitudes** conecta las probabilidades con el tamaño de la amplitud asociada a cada estado.

![Tabla de análisis de amplitudes](/images/theory/result-amplitudes-table.png)

| Columna | Qué significa |
|---------|---------------|
| **Estado** | Estado base que se está analizando, por ejemplo **\|00⟩** |
| **Parte Real** | Componente real de la amplitud |
| **Parte Imag.** | Componente imaginaria de la amplitud |
| **Magnitud** | Tamaño de la amplitud |
| **Probabilidad** | Probabilidad de medir ese estado |

---

## Esfera de Bloch en resultados

Debajo del visualizador aparece la **Esfera de Bloch Interactiva 3D**. Esta vista ayuda a interpretar el estado de los qubits de forma visual.

![Esfera de Bloch en el simulador](/images/theory/result-bloch-sphere.png)

Donde **θ** es el ángulo que forma el vector con el polo norte de la esfera y **φ** es el ángulo que indica dónde está ubicado el vector alrededor del eje vertical.