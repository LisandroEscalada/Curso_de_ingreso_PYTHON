
'''
nombre: Lisandro 
apellido: Escalada
---
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:
 
    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''
repetir_compra = 1

contador_cedear = 0
contador_bonos = 0
contador_mep = 0

cantidad_50_200_mep = 0

contador_no_cedear = 0

nombre_primer_cedear_bonos = ""
cantidad_primer_cedear_bonos = 0

promedio_dinero_cedear = 0
total_dinero_cedear = 0

promedio_intrumentos_mep = 0
total_intrumentos_mep = 0

while repetir_compra <= 2:
    print(f"Operacion de compra Nº{repetir_compra}")
    nombre = input("Nombre: ")

    monto_pesos = input("Monto de pesos de la operacion: $")
    monto_pesos = int(monto_pesos)

    while monto_pesos < 10000:
        monto_pesos = input("No puede ser menor a $10000: $")
        monto_pesos = int(monto_pesos)

    tipo_intrumento = input("Tipo de instrumento: ")
    while tipo_intrumento != "CEDEAR" and tipo_intrumento != "BONOS" and tipo_intrumento != "MEP":
        tipo_intrumento = input("El intrumento debe ser CEDEAR, BONOS o MEP: ")
    cantidad_instrumento = input("Cantidad de instrumentos: ")
    cantidad_instrumento = int(cantidad_instrumento)

    while cantidad_instrumento < 0:
        cantidad_instrumento = input("Cantidad de instrumentos no puede ser menor a 0: ")
        cantidad_instrumento = int(cantidad_instrumento)

    match tipo_intrumento:
        case "CEDEAR":
            contador_cedear += 1
            total_dinero_cedear += monto_pesos 
            if contador_cedear == 1:
                nombre_primer_cedear_bonos = nombre
                cantidad_primer_cedear_bonos = monto_pesos    
        case "BONOS":
            contador_bonos += 1
            contador_no_cedear += 1
            if contador_bonos == 1:
                nombre_primer_cedear_bonos = nombre
                cantidad_primer_cedear_bonos = monto_pesos
        case _:
            contador_mep += 1
            contador_no_cedear += 1
            total_intrumentos_mep += cantidad_instrumento
            if 90 <= cantidad_instrumento <= 200:
                cantidad_50_200_mep += 1
        
    repetir_compra += 1
        
if contador_cedear == contador_bonos and contador_cedear == contador_mep:
    intrumento_menos_opero = "Hubo empate entre los 3"
elif contador_cedear == contador_bonos:
    intrumento_menos_opero = "Hubo empate entre CEDEAR y BONOS"
elif contador_cedear == contador_mep: 
    intrumento_menos_opero = "Hubo empate entre CEDEAR y MEP"
elif contador_bonos == contador_mep:
    intrumento_menos_opero = "Hubo empate entre BONOS y MEP"
elif contador_cedear < contador_bonos and contador_cedear < contador_mep:
    intrumento_menos_opero = "CEDEAR"
elif contador_bonos < contador_cedear and contador_bonos < contador_mep:
    intrumento_menos_opero = "BONOS"
else:
    intrumento_menos_opero = "MEP"
    
empate_cedear = contador_cedear == contador_bonos
empate_bonos = contador_cedear == contador_mep
empate_mep = contador_bonos == contador_mep
    
intrumento_menos_opero = (
    "Hubo empate entre los 3" if empate_cedear and empate_bonos and empate_mep

    else "Hubo empate entre CEDEAR y BONOS" if empate_cedear

    else "Hubo empate entre CEDEAR y MEP" if empate_bonos

    else "Hubo empate entre BONOS y MEP" if empate_mep

    else "CEDEAR" if contador_cedear < contador_bonos and contador_cedear < contador_mep

    else "BONOS" if contador_bonos < contador_cedear and contador_bonos < contador_mep

    else "MEP"
)

if contador_cedear > 0:
    promedio_dinero_cedear = total_dinero_cedear / contador_cedear
else:
    promedio_dinero_cedear = "No hubo compras de CEDEAR"

if contador_mep > 0:
    promedio_intrumentos_mep = total_intrumentos_mep / contador_mep
else:
    promedio_intrumentos_mep = "No hubo compras de MEP"

print(f"INFORME:\n1. Tipo de instrumento que menos se operó en total: {intrumento_menos_opero}.")
print(f"2. Cantidad de usuarios que compraron entre 50 y 200 MEP: {cantidad_50_200_mep}.")
print(f"3. Cantidad de usuarios que no compraron CEDEAR: {contador_no_cedear}.")
print(f"4. Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR: {nombre_primer_cedear_bonos}, ${cantidad_primer_cedear_bonos}.")
print(f"5. Nombre y posicion del usuario que invirtio menos dinero: {intrumento_menos_opero}.")
print(f"6. Promedio de dinero en CEDEAR ingresado en total: {promedio_dinero_cedear}.")
print(f"7. Promedio de cantidad de instrumentos MEP vendidos en total: {promedio_intrumentos_mep}.")
