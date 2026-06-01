import math

def error_absoluto_relativo():
    print("\n--- ERROR ABSOLUTO Y RELATIVO ---")

    valor_real = float(input("Ingresa el valor real: "))
    valor_aprox = float(input("Ingresa el valor aproximado: "))

    ea = abs(valor_real - valor_aprox)
    er = (ea / valor_real) * 100

    print(f"\nError Absoluto = {ea}")
    print(f"Error Relativo = {er:.4f}%")

def cifras_significativas():
    print("\n--- CIFRAS SIGNIFICATIVAS ---")

    numero = input("Ingresa un número: ")

    if "." in numero:
        numero = numero.lstrip("0")
        numero = numero.replace(".", "")
    else:
        numero = numero.lstrip("0")

    cifras = len(numero)

    print(f"\nEl número tiene {cifras} cifras significativas")

def propagacion_errores():
    print("\n--- PROPAGACIÓN DE ERRORES ---")

    print("\n1. Suma/Resta")
    print("2. Multiplicación")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        da = float(input("Ingresa Δa: "))
        db = float(input("Ingresa Δb: "))

        resultado = da + db

        print(f"\nΔ(a±b) = {resultado}")

    elif opcion == 2:
        a = float(input("Ingresa valor de a: "))
        da = float(input("Ingresa Δa: "))

        b = float(input("Ingresa valor de b: "))
        db = float(input("Ingresa Δb: "))

        resultado = ((da / a) + (db / b)) * 100

        print(f"\nΔ(ab)/(ab) ≈ {resultado:.2f}%")

    else:
        print("Opción no válida")

def menu():
    while True:

        print("\n========= MENÚ =========")
        print("1. Error absoluto y relativo")
        print("2. Cifras significativas")
        print("3. Propagación de errores")
        print("4. Salir")

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
            error_absoluto_relativo()

        elif opcion == 2:
            cifras_significativas()

        elif opcion == 3:
            propagacion_errores()

        elif opcion == 4:
            print("\nPrograma finalizado")
            break

        else:
            print("\nOpción inválida")

menu()