def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(13):
    print(fibonacci(i))



def cuadrado_lista(numeros):
    return [num ** 2 for num in numeros]

numeros = [1, 2, 3, 4, 5]
numeros_al_cuadrado = cuadrado_lista(numeros)
print(numeros_al_cuadrado)  # Salida: [1, 4, 9, 16, 25]
