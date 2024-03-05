#Dado un número entero n, solicite un valor por consola que se va acumulando hasta que el número ingresado
#por consola es igual a n.

def acumular_hasta_n(n):
    acumulador = 0
    while True:
        valor=int(input("ingrese el valor: "))
        acumulador += valor
        if valor == n:
            break
    return acumulador

n = int(input("Ingrese el valor de n: "))
resultado=acumular_hasta_n(n)
print(resultado)