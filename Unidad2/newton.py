import math

def f(x):
    return eval(funcion)

def df(x):
    return eval(derivada)

print("Método de Newton-Raphson")

funcion = input("Ingresa la función f(x): ")
derivada = input("Ingresa la derivada f'(x): ")
x = float(input("Ingresa el valor inicial x0: "))
tol = float(input("Ingresa la tolerancia: "))
max_iter = int(input("Ingresa el número máximo de iteraciones: "))

print("\nIteración\t x\t\t f(x)\t\t f'(x)\t\t Error")

for i in range(1, max_iter + 1):
    fx = f(x)
    dfx = df(x)

    if dfx == 0:
        print("Error: la derivada es cero")
        break

    x_nuevo = x - fx / dfx
    error = abs(x_nuevo - x)

    print(i, "\t\t", round(x_nuevo, 6), "\t", round(fx, 6),
          "\t", round(dfx, 6), "\t", round(error, 6))

    if error < tol:
        x = x_nuevo
        break

    x = x_nuevo

print("\nRaíz aproximada =", round(x, 6))