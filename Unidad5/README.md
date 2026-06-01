# Unidad 5: Interpolación 

## Objetivo

Implementar el método de interpolación de Lagrange para estimar valores intermedios a partir de un conjunto de puntos conocidos.

## Fundamento Teórico

La interpolación de Lagrange permite construir un polinomio que pasa exactamente por un conjunto de puntos dados.

Este método es útil cuando se desea estimar el valor de una función en un punto que no se conoce directamente, pero que se encuentra dentro del rango de datos disponibles.

## Descripción del Programa

El programa solicita la cantidad de puntos, los valores de x y y para cada punto, y posteriormente pide el valor de x donde se desea evaluar el polinomio interpolante.

## Archivo Principal

lagrange.py

## Algoritmo

1. Ingresar la cantidad de puntos.
2. Capturar los valores de x y y.
3. Solicitar el valor de x a evaluar.
4. Calcular el polinomio de Lagrange.
5. Mostrar el valor aproximado de P(x).

## Evidencias

capturas de:

- Datos ingresados.
- Resultado obtenido.

## Resultados

El programa calcula el valor interpolado mediante el polinomio de Lagrange.

## Conclusiones

El método de Lagrange permite estimar valores intermedios de manera efectiva utilizando puntos conocidos.