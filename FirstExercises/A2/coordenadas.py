#encoding: UTF-8

# Autor: Gerardo Arturo Valderrama Quiroz, A01374994
# Descripcion: Programa que convierte las coordenadass cartesianas a coordenadas polares

# A partir de aquí escribe tu programa
import math

coorX = int(input("Inserta la coordenada x: "))
coorY = int(input("Inserta la coordenada y: "))

valorR = (coorX ** 2 + coorY ** 2) ** (1/2)
valorAng= math.atan2(coorY,coorX)
valorGra= (valorAng*180)/math.pi

print("El valor de r es de: ", valorR)
print("El valor del ángulo es de: ", valorGra)
