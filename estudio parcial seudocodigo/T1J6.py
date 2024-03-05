#Dado el tiempo en segundo que tarda un atleta en recorrer una distancia, se debe retornar el tiempo total en
#horas, minutos y segundos.

def convertir_tiempo(totalseg):
    horas = totalseg // 3600
    minutos = (totalseg % 3600) // 60
    segundos = totalseg % 60
    return horas, minutos, segundos

totalseg = int(input("ingrese el tiempo en segundos: "))

horas, minutos, segundos = convertir_tiempo(totalseg)
print(horas, minutos, segundos)