def fibonaccI(n):
    """Calculo Fiboncacci iterativo"""
    n0 = 0
    n1 = 1
    fib = 0
    if n == 0 or n == 1:
        fib = n
    else:
        i = 2
        while i < n:
            fib = n0 + n1
            n0 = n1
            n1 = fib
            i += 1
    return fib

# Solicitar al usuario cuántas veces desea calcular la secuencia de Fibonacci
num_veces = int(input("¿Cuántas veces desea calcular la secuencia de Fibonacci? "))

# Iterar sobre el número de veces que el usuario desea calcular la secuencia
for _ in range(num_veces):
    # Solicitar al usuario el inicio y el fin del rango de la secuencia de Fibonacci
    inicio = int(input("Ingrese el número de inicio del rango: "))
    fin = int(input("Ingrese el número de fin del rango: "))

    # Imprimir la secuencia de Fibonacci para el rango dado
    print("Secuencia de Fibonacci para el rango", inicio, "-", fin, ":")
    for i in range(inicio, fin + 1):
        resultado = fibonaccI(i)
        print("Fibonacci(", i, ") =", resultado)
    print()  # Añadir una línea en blanco entre cada conjunto de resultados
