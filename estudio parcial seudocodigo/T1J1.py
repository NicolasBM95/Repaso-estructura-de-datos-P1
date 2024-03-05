def es_multiplo(n, m):
    if m == 0:
        print("m no puede ser cero.")
        return 
    while n >= m:
        n -= m
    if n == 0:
            print("es multiplo")
    else:
            print("no es multiplo")
        

# Ejemplos de uso
n = 15
m = 2
print(es_multiplo(n, m))  # True, ya que 15 es múltiplo de 5