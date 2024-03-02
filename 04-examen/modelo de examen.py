from tkinter.messagebox import askyesno as question

'''
Simulacro Turno Tarde

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

 

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)



No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

other_client = True

kilos_addition = 0
three_days_amount = 0
average_kilos_three = 0

one_days_amount = 0
five_days_amount = 0
average_one_days = 0

height_elderly = float("-inf")
height_elderly_name = "N/A"
height_elderly_age = 0

height_menos = float("inf")
kilos_menor_age = 0
name_menor_age = "N/A"

while other_client == True:
    name = input("Nombre: ")
    age = int(input("Edad: "))
    while age < 12:
        age = int(input("Debe ser mayor a 12: "))
    height = int(input("Altura: "))
    while height < 0:
        height = int(input("No debe ser negativa: "))
    days_asssisted =  input("Días que asiste a la semana: ")
    while "1" != days_asssisted != "3" and days_asssisted != "5":
        days_asssisted =  input("1, 3, 5: ")
    kilos_dead_weight = int(input("Kilos que levanta en peso muerto: "))
    while kilos_dead_weight <= 0:
        kilos_dead_weight = int(input("No debe ser cero, ni negativo: "))

    if days_asssisted == "3":
        kilos_addition += kilos_dead_weight
        three_days_amount += 1
    elif days_asssisted == "1":
        one_days_amount += 1
    else:
        five_days_amount += 1
        if height < height_menos:
            height_menos = height
            kilos_menor_age = kilos_dead_weight
            name_menor_age = name

    if height > height_elderly:
        height_elderly = height
        height_elderly_name = name
        height_elderly_age = age

    print(height_elderly_name)
    print(height_elderly_age)

    other_client = question("Clientes", "Ingresar otro cliente?")

clients_week = one_days_amount + three_days_amount + five_days_amount

average_kilos_three = kilos_addition / three_days_amount if kilos_addition != 0 else 0
average_one_days = one_days_amount / clients_week if one_days_amount != 0 else 0

one_tie = one_days_amount == three_days_amount
three_tie = three_days_amount == five_days_amount
five_tie = five_days_amount == one_days_amount

if five_days_amount < one_days_amount > three_days_amount:
    days_lleno = "1"
elif five_days_amount < three_days_amount > one_days_amount:
    days_lleno = "3"
elif three_days_amount < five_days_amount > one_days_amount:
        days_lleno = "5"
elif one_tie and three_tie and five_tie:
    days_lleno = "Hubo empate entre los tres"
elif one_tie:
    days_lleno = "Hubo empate entre 1 y 3 dias"
elif three_tie: 
    days_lleno = "Hubo empate entre 3 y 5 dias"
else:
    days_lleno = "Hubo empate entre 5 y 1 dia"   
    
print(f"El promedio de kilos que levantan las personas que asisten solo 3 días a la semana: {average_kilos_three}")
print(f"El porcentaje de clientes que asiste solo 1 día a la semana: {average_one_days}")
print(f"Nombre y edad del cliente con más altura: {height_elderly_name}, {height_elderly_age}")
print(f"Determinar si los clientes eligen más ir 1, 3 o 5 días: {days_lleno}")
print(f"Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana: {name_menor_age}, {kilos_menor_age}")
