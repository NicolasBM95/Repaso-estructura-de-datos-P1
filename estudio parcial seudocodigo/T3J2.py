#Dado un arreglo A[ ] de enteros. Presente un algoritmo que encuentre un elemento del arreglo que representa un
#pico, es decir, que sus vecinos son menores. Para los elementos en los extremos, solo se considera un vecino. Por
#ejemplo. Para el arreglo A = [3 10 25 11 9], la salida es 25 dado que sus vecinos son el 10 y 11 que son menores a
#25.

def encontrar_pico(arr):
    n= len(arr)
    inicio = 0
    fin = n-1
    while inicio <= fin:
        medio = (inicio + fin) // 2

        if (medio == 0 or arr[medio - 1] <= arr[medio]) and (medio == n - 1 or arr[medio + 1] <= arr[medio]):
            return arr[medio]
        
        elif medio > 0 and arr[medio - 1] > arr[medio]:
            fin = medio - 1

        else:
            inicio = medio + 1

A = [3, 10, 25, 11, 9]
print("Arreglo original:", A)
pico = encontrar_pico(A)
print("Elemento pico:", pico)