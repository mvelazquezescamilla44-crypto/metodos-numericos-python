def lagrange(x_valores, y_valores, x):
    n = len(x_valores)
    resultado = 0

    for i in range(n):
        termino = y_valores[i]

        for j in range(n):
            if i != j:
                termino *= (x - x_valores[j]) / (x_valores[i] - x_valores[j])

        resultado += termino

    return resultado


# Pedir cantidad de puntos
n = int(input("Ingrese la cantidad de puntos: "))

x_valores = []
y_valores = []

# Pedir puntos
for i in range(n):
    print(f"\nPunto {i + 1}")
    x = float(input("Ingrese x: "))
    y = float(input("Ingrese y: "))

    x_valores.append(x)
    y_valores.append(y)

# Pedir valor a evaluar
x_eval = float(input("\nIngrese el valor de x para evaluar P(x): "))

# Calcular
resultado = lagrange(x_valores, y_valores, x_eval)

# Mostrar resultado
print("\nResultado:")
print(f"P({x_eval}) = {resultado}")