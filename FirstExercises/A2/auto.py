#encoding: UTF-8

# Autor: Gerardo Arturo Valderrama Quiroz, A01374994
# Descripcion: Calcular determinada distancia y tiempo dada una velocidad por el usuario

# A partir de aquí escribe tu programa

vel = int(input("Inserta una velocidad: "))
distancia6hr = vel*6
distancia10hr = vel*10
tiempo500km = 500/vel
print("Tu distancia en 6 horas es de ", distancia6hr, " km")
print("Tu distancia en 10 horas es de ", distancia10hr, " km")
print("Tu tiempo al recorrer 500 kilometros es de ", tiempo500km, " horas")
