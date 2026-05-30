---
title: Bloques Cuánticos Avanzados
description: Aprende qué hacen los bloques cuánticos avanzados y cómo se usan en circuitos más complejos
order: 5
---
 
Los bloques cuánticos avanzados son combinaciones de compuertas básicas que realizan operaciones más complejas. En vez de construir esas operaciones desde cero cada vez, se agrupan en un solo bloque reutilizable.
 
> **Recuerda:** Estos bloques se construyen encadenando compuertas básicas como H, X, CX, entre otras. Si aún no las conoces, te recomendamos leer primero la lección de [Compuertas Básicas](/teoria/compuertas-basicas/).
 
---
 
## Bloques Aritméticos
 
Estos bloques realizan operaciones matemáticas sobre qubits, equivalentes a las sumas que hace un computador clásico pero en el mundo cuántico.
 
---
 
### HALF ADD — Medio Sumador
 
![Diagrama del bloque Half Adder](/images/theory/half-add.png)
 
**¿Para qué sirve?**
Suma dos bits cuánticos y produce dos resultados: la **suma** y el **acarreo** (carry). El acarreo es el "me llevo uno" que ocurre cuando la suma supera lo que un solo bit puede representar. Es el bloque más simple de aritmética cuántica.
 
**Entradas:**
- **Qubit A:** primer número a sumar
- **Qubit B:** segundo número a sumar

**Salidas:**
- **Suma:** el resultado de A + B (sin contar el acarreo)
- **Acarreo:** indica si hubo desbordamiento

| **A (entrada)** | **B (entrada)** | **Suma (salida)** | **Acarreo (salida)** |
|----------------|----------------|------------------|---------------------|
| \|0⟩ | \|0⟩ | \|0⟩ | \|0⟩ |
| \|0⟩ | \|1⟩ | \|1⟩ | \|0⟩ |
| \|1⟩ | \|0⟩ | \|1⟩ | \|0⟩ |
| \|1⟩ | \|1⟩ | \|0⟩ | \|1⟩ |
 
**Analogía:** Es como sumar dos números de un solo dígito: 1 + 1 = 0 y me llevo 1.
 
---
 
### FULL ADD — Sumador Completo
 
![Diagrama del bloque Full Adder](/images/theory/full-add.png)
 
**¿Para qué sirve?**
Es una versión extendida del medio sumador. Suma **tres bits**: dos números y un acarreo de entrada (proveniente de una suma anterior). Esto permite encadenar varios sumadores para sumar números más grandes.
 
**Entradas:**
- **Qubit A:** primer número a sumar
- **Qubit B:** segundo número a sumar
- **Qubit Cin:** acarreo de entrada (carry-in)

**Salidas:**
- **Suma:** el resultado de A + B + Cin
- **Acarreo (Cout):** acarreo de salida para la siguiente etapa

| **A** | **B** | **Cin** | **Suma (salida)** | **Cout (salida)** |
|-------|-------|---------|------------------|------------------|
| \|0⟩ | \|0⟩ | \|0⟩ | \|0⟩ | \|0⟩ |
| \|0⟩ | \|0⟩ | \|1⟩ | \|1⟩ | \|0⟩ |
| \|0⟩ | \|1⟩ | \|0⟩ | \|1⟩ | \|0⟩ |
| \|0⟩ | \|1⟩ | \|1⟩ | \|0⟩ | \|1⟩ |
| \|1⟩ | \|0⟩ | \|0⟩ | \|1⟩ | \|0⟩ |
| \|1⟩ | \|0⟩ | \|1⟩ | \|0⟩ | \|1⟩ |
| \|1⟩ | \|1⟩ | \|0⟩ | \|0⟩ | \|1⟩ |
| \|1⟩ | \|1⟩ | \|1⟩ | \|1⟩ | \|1⟩ |
 
---
 
### OLD FULL ADD — Sumador Completo Clásico
 
![Diagrama del bloque Old Full Adder](/images/theory/old-full-add.png)
 
**¿Para qué sirve?**
Es una implementación alternativa del sumador completo, basada en un diseño más antiguo. Realiza la misma operación que el FULL ADD (suma A + B + Cin), pero usando una combinación diferente de compuertas internamente. Se incluye como referencia para comparar distintas formas de construir el mismo circuito.
 
**Entradas:**
- **Qubit A:** primer número a sumar
- **Qubit B:** segundo número a sumar
- **Qubit Cin:** acarreo de entrada

**Salidas:**
- **Suma:** el resultado de A + B + Cin
- **Acarreo (Cout):** acarreo de salida
> **Nota:** Las entradas y salidas son idénticas a las del FULL ADD. La diferencia está en cómo se construye internamente el circuito, lo que puede afectar el rendimiento o la profundidad del circuito en hardware real.
 
---
 
## Bloques de Transformada
 
Estos bloques realizan transformaciones matemáticas sobre grupos de qubits, y son piezas clave en algoritmos cuánticos avanzados como el de Shor.
 
---
 
### QFT — Transformada de Fourier Cuántica
 
![Diagrama del bloque QFT](/images/theory/qft.png)
 
**¿Para qué sirve?**
La Transformada de Fourier Cuántica (Quantum Fourier Transform) convierte la información almacenada en los estados de los qubits al **dominio de frecuencias**. Es el equivalente cuántico de la Transformada de Fourier clásica, pero exponencialmente más rápida.
 
En términos simples: toma un patrón de estados cuánticos y lo reexpresa en términos de sus componentes de frecuencia, lo que permite detectar periodicidades ocultas en los datos.
 
**Entradas:**
- **n qubits** en cualquier estado cuántico

**Salidas:**
- **n qubits** con la representación en el dominio de frecuencias
**¿Dónde se usa?**
Es un componente fundamental del algoritmo de Shor (para factorizar números grandes) y de otros algoritmos de estimación de fase.
 
> **Nota:** La QFT no produce resultados directamente legibles al medir. Su utilidad está en combinarse con otras operaciones antes de la medición final.
 
---
 
### IQFT — Transformada de Fourier Cuántica Inversa
 
![Diagrama del bloque IQFT](/images/theory/iqft.png)
 
**¿Para qué sirve?**
Es la operación inversa de la QFT. Convierte información del **dominio de frecuencias** de vuelta al dominio original. Se usa para extraer el resultado final después de que la QFT y otras operaciones han procesado los datos.
 
**Entradas:**
- **n qubits** en el dominio de frecuencias

**Salidas:**
- **n qubits** de vuelta al dominio original

**Relación con la QFT:**
 
| **Bloque** | **Direccion** | **Uso tipico** |
|-----------|--------------|----------------|
| QFT | Original → Frecuencias | Inicio del procesamiento |
| IQFT | Frecuencias → Original | Extraccion del resultado final |
 
> **Nota:** En la mayoria de los algoritmos, la QFT y la IQFT se usan juntas: la QFT transforma, se hacen operaciones en el dominio de frecuencias, y la IQFT devuelve el resultado interpretable.
 
---
 
## Bloques de Aritmetica Modular
 
---
 
### MOD EXP — Exponenciacion Modular
 
![Diagrama del bloque Mod Exp](/images/theory/mod-exp.png)
 
**¿Para qué sirve?**
Calcula la **exponenciación modular**: eleva un número a una potencia y luego aplica una operación de módulo (el residuo de una división). Es decir, calcula a^x mod N.
 
Aunque suena muy matemático, es el corazón del **algoritmo de Shor**, que permite a un computador cuántico factorizar números grandes mucho más rápido que cualquier computador clásico.
 
**Entradas:**
- **Registro de exponente:** qubits que representan el valor de x
- **Registro de resultado:** qubits inicializados en \|1⟩ donde se escribe el resultado
- **Parametros a y N:** el número base y el módulo (son fijos, es decir, ya vienen preestablecidos dentro del bloque MOD EXP)

**Salida:**
- **Registro de resultado:** contiene el valor de a^x mod N

**¿Por qué es importante?**
La dificultad de factorizar números grandes es la base de la seguridad de muchos sistemas de cifrado actuales (como RSA). El MOD EXP cuántico, combinado con la QFT, es lo que hace al algoritmo de Shor una amenaza potencial para esa seguridad.
 
> **Nota:** Este bloque opera sobre **superposiciones** de muchos valores de x al mismo tiempo, lo que le da al computador cuántico su ventaja sobre los computadores clásicos.
 
---
 
## Resumen rápido
 
| Bloque | Qubits de entrada | ¿Qué hace? |
|--------|------------------|-----------|
| **HALF ADD** | 2 | Suma dos bits, produce suma y acarreo |
| **FULL ADD** | 3 | Suma dos bits mas un acarreo de entrada |
| **OLD FULL ADD** | 3 | Igual que FULL ADD, con diseño de circuito alternativo |
| **QFT** | n | Convierte estados al dominio de frecuencias |
| **IQFT** | n | Convierte de vuelta desde el dominio de frecuencias |
| **MOD EXP** | n + parametros | Calcula a^x mod N sobre superposiciones |
 
[Ir al simulador para practicar](/simulador/)
 