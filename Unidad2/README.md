# Unidad 2: Métodos para la Solución de Ecuaciones No Lineales

## Objetivo

Implementar métodos numéricos para aproximar raíces de ecuaciones no lineales utilizando técnicas iterativas.

## Métodos Implementados

### Método de Bisección

El método de bisección localiza una raíz dentro de un intervalo donde existe cambio de signo. En cada iteración divide el intervalo a la mitad hasta alcanzar la precisión deseada.

Archivo:

biseccion.py

### Método de Newton-Raphson

El método de Newton-Raphson utiliza la función y su derivada para aproximar rápidamente una raíz mediante iteraciones sucesivas.

Archivo:

newton.py

## Descripción General

Los programas permiten encontrar raíces aproximadas de ecuaciones no lineales mediante distintos métodos numéricos.

## Algoritmos Utilizados

### Método de Bisección

1. Ingresar la función.
2. Definir intervalo inicial.
3. Verificar cambio de signo.
4. Calcular punto medio.
5. Actualizar intervalo.
6. Repetir hasta cumplir la tolerancia.

### Método de Newton-Raphson

1. Ingresar función y derivada.
2. Definir valor inicial.
3. Calcular nueva aproximación.
4. Evaluar error.
5. Repetir hasta cumplir la tolerancia.

## Evidencias

### Método de Bisección

![Bisección](../img/unidad2/biseccion_resultado.png)

### Método de Newton-Raphson

![Newton-Raphson](../img/unidad2/newton_resultado.png)

## Resultados

Ambos métodos permiten aproximar raíces de ecuaciones no lineales. El método de bisección ofrece una convergencia garantizada cuando existe cambio de signo, mientras que Newton-Raphson suele converger más rápidamente cuando se dispone de una buena aproximación inicial.

## Conclusiones

* Se implementaron métodos iterativos para la solución de ecuaciones no lineales.
* Se compararon técnicas de convergencia distintas.
* Se observó la importancia de la selección de parámetros iniciales.
* Los algoritmos desarrollados permiten obtener aproximaciones confiables de raíces matemáticas.
