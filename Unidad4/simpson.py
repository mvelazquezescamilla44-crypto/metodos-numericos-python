import math

def f(x):
    return eval(funcion)

print("Método de Simpson 1/3")

funcion = input("Ingresa la función f(x): ")
a = float(input("Ingresa el límite inferior a: "))
b = float(input("Ingresa el límite superior b: "))
n = int(input("Ingresa el número de intervalos n: "))

if n % 2 != 0:
    print("Error: n debe ser par para Simpson 1/3")
else:
    h = (b - a) / n
    suma = f(a) + f(b)

    print("\nTabla de valores:")
    print("i\t x\t\t f(x)")

    for i in range(n + 1):
        x = a + i * h
        print(i, "\t", round(x, 4), "\t", round(f(x), 6))

    for i in range(1, n):
        x = a + i * h

        if i % 2 == 0:
            suma += 2 * f(x)
        else:
            suma += 4 * f(x)

    resultado = (h / 3) * suma

    print("\nh =", h)
    print("Resultado aproximado =", resultado)