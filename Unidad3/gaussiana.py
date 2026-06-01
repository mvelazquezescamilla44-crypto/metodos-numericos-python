def eliminacion_gaussiana(A, b):
    n = len(A)

    # Eliminación hacia adelante
    for i in range(n):
        pivote = A[i][i]

        if pivote == 0:
            print("Error: pivote cero")
            return None

        for j in range(i + 1, n):
            factor = A[j][i] / pivote

            for k in range(i, n):
                A[j][k] = A[j][k] - factor * A[i][k]

            b[j] = b[j] - factor * b[i]

    # Sustitución hacia atrás
    x = [0] * n

    for i in range(n - 1, -1, -1):
        suma = 0

        for j in range(i + 1, n):
            suma += A[i][j] * x[j]

        x[i] = (b[i] - suma) / A[i][i]

    return x


n = int(input("Número de incógnitas: "))

A = []
b = []

print("\nIngresa los coeficientes:")

for i in range(n):
    fila = []

    for j in range(n):
        valor = float(input(f"A[{i+1}][{j+1}]: "))
        fila.append(valor)

    resultado = float(input(f"Resultado b[{i+1}]: "))

    A.append(fila)
    b.append(resultado)

solucion = eliminacion_gaussiana(A, b)

if solucion is not None:
    print("\nSolución:")
    for i in range(n):
        print(f"x{i+1} = {round(solucion[i], 4)}")