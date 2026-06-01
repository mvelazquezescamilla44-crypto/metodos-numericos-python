import math

def f(x):
    return eval(funcion)

print("Método de Bisección")

funcion = input("Ingresa la función f(x): ")
a = float(input("Ingresa el límite inferior a: "))
b = float(input("Ingresa el límite superior b: "))
tol = float(input("Ingresa la tolerancia: "))

if f(a) * f(b) > 0:
    print("Error: no hay cambio de signo en el intervalo")
else:
    iteracion = 0

    print("\nIteración\t a\t\t b\t\t c\t\t f(c)\t\t Error")

    while True:
        c = (a + b) / 2
        error = abs(b - a) / 2
        iteracion += 1

        print(iteracion, "\t\t", round(a, 6), "\t", round(b, 6),
              "\t", round(c, 6), "\t", round(f(c), 6), "\t", round(error, 6))

        if abs(f(c)) == 0 or error < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nRaíz aproximada =", round(c, 6))