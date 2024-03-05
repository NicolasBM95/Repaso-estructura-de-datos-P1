#Dada una cadena que representa una expresión simple matemática, retorne el calculo de la expresión. Por
#ejemplo, si la cadena es “23 + 7” el método debe retornar 30, si la expresión es: “13+2*5”, el método debe retornar
#20. Asuma que la expresión solo tiene operaciones de + , -, *, y /.

def calculadora(expresion):
    try:
        resultado = eval(expresion)
        return resultado
    except Exception as e:
        print("error al evaluar la expresion")

expresion = input("ingrese la expresion matematica: ")
resultado1 = calculadora(expresion)
if resultado1 is not None:
    print(resultado1)