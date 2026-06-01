# Unidad 3: Solución de Sistemas de Ecuaciones Lineales

## Objetivo

Implementar métodos numéricos para resolver sistemas de ecuaciones lineales mediante técnicas directas e iterativas.

## Métodos Implementados

### Eliminación Gaussiana

Método directo que transforma la matriz del sistema en una matriz triangular superior para posteriormente obtener la solución mediante sustitución hacia atrás.

Archivo:

gaussiana.py

### Método de Jacobi

Método iterativo que calcula aproximaciones sucesivas de la solución hasta alcanzar una precisión aceptable.

Archivo:

jacobi.py

## Descripción General

Los programas permiten ingresar los coeficientes de un sistema de ecuaciones lineales y calcular las incógnitas utilizando diferentes técnicas numéricas.

## Algoritmos Utilizados

### Eliminación Gaussiana

1. Ingresar matriz de coeficientes.
2. Ingresar vector de resultados.
3. Aplicar eliminación hacia adelante.
4. Aplicar sustitución hacia atrás.
5. Mostrar la solución.

### Método de Jacobi

1. Ingresar matriz de coeficientes.
2. Ingresar vector de resultados.
3. Definir número de iteraciones.
4. Calcular nuevas aproximaciones.
5. Mostrar resultados de cada iteración.
6. Presentar solución aproximada.

## Evidencias

 capturas de:

* Datos de entrada.
* Desarrollo del método.
* Resultado final.

## Resultados

Ambos métodos permiten resolver sistemas de ecuaciones lineales. La eliminación gaussiana obtiene una solución directa, mientras que Jacobi genera aproximaciones sucesivas.

## Conclusiones

La implementación de ambos métodos permitió comprender las diferencias entre técnicas directas e iterativas para la solución de sistemas de ecuaciones lineales.
