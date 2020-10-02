#encoding: UTF-8

# Autor: Gerardo Arturo Valderrama Quiroz, A01374994
# Descripcion: Dar el total de alumnos y el porcentaje de hombres y mujeres de acuerdo a los datos proporcionados por el usuario

# A partir de aquí escribe tu programa

numhombres = input("Da el número de alumnos inscritos hombres: ")
nummujeres = input("Da el número de alumnos inscritos mujeres: ")
total = int(numhombres)+int(nummujeres)
mujerespor = int(nummujeres)*100/int(total)
hombrespor = int(numhombres)*100/int(total)
print("El total de alumnos inscritos es de: ", total)
print("El porcentaje de mujeres inscritas es de: ", mujerespor,"%")
print("El porcentaje de hombres inscritos es de: ", hombrespor,"%")
