from tkinter.messagebox import askyesno as question

'''
nombre: Lisandro 
apellido: Escalada
---
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

seguir = True
precio = 0
valor_descuento = 0
descuento_aplicado = 0

masculino_entrada = 0
femenino_entrada = 0
otro_entrada = 0
genero_mas_frecuente_campo = "-"
general_cantidad = 0
general_credito = 0
suma_edad = 0
edad_promedio = 0
platea_debito = 0
mayor_precio_general_debito = 0
nombre_general_debito = ""
edad_general_debito = 0
platea_cantidad_primos = 0
edad_primo = 0
primo = True
edad_multi_seis = 0
platea_cantidad_multi_seis = 0
total_platea_debito = 0

while seguir == True:
    nombre = input("Nombre: ")

    edad = input("Edad: ")
    edad = int(edad)
    while edad < 16:
        edad = input("No menor a 16: ")
        edad = int(edad)

    genero = input("Genero: ")
    while genero != "masculino" and genero != "femenino" and genero != "otro":
        genero = input("Masculino, femenino u otro: ")

    entrada = input("Tipo de entrada: ")
    while entrada != "general" and entrada != "campo delantero" and entrada != "platea":
        entrada = input("General, campo delantero o platea: ")

    pago = input("Medio de pago: ")
    while pago != "credito" and pago != "efectivo" and pago != "debito":
        pago = input("Crédito, efectivo o débito: ")

    if genero == "masculino":
        masculino_entrada += 1
    elif genero == "femenino":
        femenino_entrada += 1
    else:
        otro_entrada += 1

    empate_masculino = masculino_entrada == femenino_entrada
    empate_femenino = femenino_entrada == otro_entrada
    empate_otro = otro_entrada == masculino_entrada

    if entrada == "general":
        precio = 16000
        general_cantidad += 1
        if pago == "credito":
            general_credito += 1
            suma_edad += edad
        elif pago == "debito":
            if precio > mayor_precio_general_debito:
                mayor_precio_general_debito = precio
                nombre_general_debito = nombre
                edad_general_debito = edad
    elif entrada == "campo delantero":
        precio = 25000 
        if masculino_entrada > femenino_entrada and masculino_entrada > otro_entrada:
            genero_mas_frecuente_campo = "Masculinos"
        elif femenino_entrada > masculino_entrada and femenino_entrada > otro_entrada:
            genero_mas_frecuente_campo = "Femeninos"
        elif otro_entrada > masculino_entrada and otro_entrada > femenino_entrada:
             genero_mas_frecuente_campo = "Otros"
        elif empate_masculino and empate_femenino and empate_otro:
            genero_mas_frecuente_campo = "Hubo empate entre los tres"
        elif empate_masculino:
            genero_mas_frecuente_campo = "Hubo empate entre masculinos y femenino"
        elif empate_femenino: 
            genero_mas_frecuente_campo = "Hubo empate entre femenino y otros"
        else:
            genero_mas_frecuente_campo = "Hubo empate entre otros y masculino"         
    else:
        precio = 30000
        if pago == "debito":
            platea_debito += 1    
            edad_multi_seis = edad
            if edad_multi_seis % 6 == 0:
                total_platea_debito += precio
        edad_primo = edad
        if edad_primo < 2:
            primo = False
        else:
            for numeros in range(2, edad_primo):
                if edad_primo % numeros == 0:
                    primo = False
                    break
            if primo:
                platea_cantidad_primos += 1

    if pago == "credito":
        valor_descuento = precio * 20 / 100
        descuento_aplicado = precio - valor_descuento
    elif pago == "debito":
        valor_descuento = precio * 15 / 100
        descuento_aplicado = precio - valor_descuento
    if general_cantidad > 1:
        edad_promedio = suma_edad / general_cantidad
    else:
        edad_promedio = 0   

    seguir = question("", "Seguir comprando?")

total_personas = femenino_entrada + masculino_entrada + otro_entrada
porcentaje_platea_debito = (platea_debito / total_personas) * 100

print(f"1. Género más frecuente de los que compraron entradas al campo: {genero_mas_frecuente_campo}.")
print(f"2. Personas que compraron entradas de general con tarjeta de crédito: {general_credito} y su edad promedio: {edad_promedio}.")
print(f"3. Porcentaje de entradas a la platea con débito respecto al total de personas: {porcentaje_platea_debito}")
print(f"4. Total de descuentos de crédito en pesos: {valor_descuento} ")
print(f"5. Nombre y edad del que pagó el precio más alto por una entrada de general y con débito: {nombre_general_debito}, {edad_general_debito}.")
print(f"6. Cantidad de personas que compraron entradas a la platea y cuya edad es un número primo: {platea_cantidad_primos}.")
print(f"7. Monto total por la venta de entradas a la platea y pagadas con debito por personas cuyas edades son múltiplos de 6: {total_platea_debito}.")