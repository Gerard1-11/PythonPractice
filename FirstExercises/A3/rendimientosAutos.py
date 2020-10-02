#encoding: UTF-8

#gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula cuanto kilometros por litro y millas por galon rinde de acuerdo a lo indicado por el usario, aproximar
# cuantos litro se necsita por una cantidad de kilometos dada por el usuario.

#funcion que calgula el rendimiento del aunto en kilometros por litro
def calcularrendimientoKmL(km, l):
    rendimientoKilometroLitro = km / l
    return rendimientoKilometroLitro

#Funcion que convierte los kilometros a Millas
def convertirKmaMi(km):
    kilometroconvertido = km / 1.609344
    return kilometroconvertido

#Función que convierte los litros a Galones
def convertirLaGal(l):
    litrosconvertidos = l * .264172051
    return litrosconvertidos

#Función que calcula el rendimiento del auto en Millas por Galon
def calcularrendimientoMiGal(Mi,Gal):
    rendimientoMillaGalon = Mi / Gal
    return rendimientoMillaGalon

#Función que calcula los litros esperados de caurdo a determinada cantidad de kilometros  que se recorreran
def calcularaproximadoL(km1,l,kmesp):
    prediccionlitros = (kmesp*l)/km1
    return prediccionlitros

#Función principal main que lee inputs, llama a las demas funciones e imprime
def main():
    kilometros = float(input("Teclea los kilómetros recorridos: "))
    litros = float(input("Teclea los litros utilizados: "))
    print("Si recorres %.2f Kms con %.2f litros de gasolina, el rendimiento es:" % (kilometros,litros))

    rendiKml = calcularrendimientoKmL(kilometros,litros)
    print("%.2f km/l" % rendiKml)

    millas = convertirKmaMi(kilometros)
    galones = convertirLaGal(litros)
    rendiMiGal = calcularrendimientoMiGal(millas,galones)
    print("%.2f Mi/gal" % rendiMiGal)

    kilometrosesperados = float(input("¿Cuántos kilómetrso va a recorrer?: "))
    aproximacionL = calcularaproximadoL(kilometros,litros,kilometrosesperados)
    print("para recorrer %.2f kilometros usted necesita %.2f litros de gasolina" % (kilometrosesperados, aproximacionL))

main()
