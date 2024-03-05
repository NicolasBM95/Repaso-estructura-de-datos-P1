#Dado un arreglo A[ ] de enteros. Presente un algoritmo que invierta los elementos del arreglo. Por ejemplo, dado
#el arreglo A = [5 10 27 30], la salida es [30 27 10 5].

def inv_arreglo(arr):
    inicio = 0
    fin = len(arr)-1

    while inicio<fin:
        arr[inicio], arr[fin] = arr[fin], arr[inicio]
        inicio += 1
        fin -= 1

A = [5, 10, 27, 30]
print("Arreglo original:", A)
inv_arreglo(A)
print("Arreglo invertido:", A)