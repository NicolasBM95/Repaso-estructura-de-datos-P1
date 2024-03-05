# Dado un número entero n, retorne la suma de todos los enteros positivos impares menores a n

def suma_enteros_n(n):
    
    suma = 0
    
    for i in range(1, n, 2):
        suma += i
    return suma
    
num = 10
resultado = suma_enteros_n(num)
print(resultado)