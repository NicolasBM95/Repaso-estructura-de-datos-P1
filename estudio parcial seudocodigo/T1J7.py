#Se ha implementado un programa social que otorga un subsidio familiar bajo las siguientes características: (i) Si
#una familia tiene hasta 2 hijos recibe $70.000 por mes, entre 3 a 5 hijos $120.000 por mes, si tiene más de 6 hijos
#recibe $150.000 al mes; (ii) por cada hijo en edad escolar (entre 6 a 18 años) recibe $10.000 adicionales, y (iii) si la
#familia solo esta conformada por la madre cabeza de hogar recibe un 50% adicional del valor asignado por la regla
#(i) y (ii). Diseñe el método que permita realizar este cálculo definiendo que variables de entrada se requieren.

def calcular_subsidio(num_hijos, num_hijos_escolar, madre_cabeza_de_hogar=False):
    if madre_cabeza_de_hogar:
        if num_hijos <= 2:    
            subsidio = ((num_hijos_escolar * 10000)+70000) * 1.5
        elif 3 <= num_hijos <= 5:
            subsidio = ((num_hijos_escolar * 10000)+120000) * 1.5
        else:
            subsidio = ((num_hijos_escolar * 10000)+150000) * 1.5
    else:
        if num_hijos <= 2:
            subsidio = (num_hijos_escolar * 10000)+70000
        elif 3 <= num_hijos <= 5:
            subsidio = (num_hijos_escolar * 10000)+120000
        else:
            subsidio = (num_hijos_escolar * 10000)+150000

    return subsidio

num_hijos = int(input("Ingrese el número de hijos: "))
num_hijos_escolar = int(input("Ingrese el número de hijos en edad escolar: "))
madre_cabeza_de_hogar = input("¿La familia está conformada únicamente por la madre cabeza de hogar? (s/n): ").lower() == 's'

subsidio = calcular_subsidio(num_hijos, num_hijos_escolar, madre_cabeza_de_hogar)
print("El subsidio familiar es de $", subsidio)