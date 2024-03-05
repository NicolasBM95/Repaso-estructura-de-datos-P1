#Dado un arreglo A[ ] de enteros. Presente un algoritmo de ordenamiento, donde los elementos queden
#organizados de mayor a menor. Por ejemplo, para el arreglo A = [8 5 7 0 3 9], la salida es [9 8 7 5 3 0].

def ordenamiento(arr):
    n = len(arr)

    for i in range (n):
        for j in range (0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


A = [8, 5, 7, 0, 3, 9]
print("Arreglo original:", A)
ordenamiento(A)
print("Arreglo ordenado de mayor a menor:", A)