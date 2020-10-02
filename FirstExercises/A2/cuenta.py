#encoding: UTF-8

# Autor: Gerardo Arturo Valderrama Quiroz, A01374994
# Descripcion: De acuerdo al costo de una comida, darle al usuario su subtotal, la propina que debe de dar, el IVA y el total de la comida

# A partir de aquí escribe tu programa

costo = input("Inserta el costo de la comida: ")
subtotal = costo
propina = float(costo)*.12
iva = float(costo)*.16
total= float(subtotal)+propina+iva
print("Su subtotal es de $", subtotal)
print("La propina es de $", propina)
print("El IVA es de $", iva)
print("Su Total es de $", total)
