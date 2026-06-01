def jacobi():
    n = int(input("Ingresa el número de incógnitas: "))

    A = []
    b = []

    print("\nIngresa los coeficientes del sistema:")
    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f"A[{i+1}][{j+1}]: "))
            fila.append(valor)
        A.append(fila)

        resultado = float(input(f"Resultado de la ecuación {i+1}: "))
        b.append(resultado)

    x = [0.0 for _ in range(n)]

    iteraciones = int(input("\nIngresa el número de iteraciones: "))

    print("\nIteraciones del método de Jacobi:")
    print("Iteración\tValores")

    for k in range(iteraciones):
        nuevo_x = x.copy()

        for i in range(n):
            suma = 0

            for j in range(n):
                if j != i:
                    suma += A[i][j] * x[j]

            nuevo_x[i] = (b[i] - suma) / A[i][i]

        x = nuevo_x.copy()

        print(f"{k+1}\t\t{x}")

    print("\nResultado aproximado:")
    for i in range(n):
        print(f"x{i+1} = {x[i]:.6f}")


jacobi()