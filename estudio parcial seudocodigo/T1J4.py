#Dada una cadena, se debe verificar si esta corresponde a un palíndromo
def es_un_palindromo(cadena):
    cadena = cadena.replace(" ","").lower()
    
    return cadena == cadena[::-1]

cadena = input("ingrese la cadena: ")
if es_un_palindromo(cadena):
    print("es un palindromo")
else:
    print("no es un palindromo")