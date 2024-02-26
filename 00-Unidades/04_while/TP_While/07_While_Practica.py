import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT)  

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
    # Inicializacion
        seguir = True

        contador_masculino_IOT_IA = 0

        contador_IOT = 0
        contador_IA = 0
        contador_RV_RA = 0

        contador_masculino = 0
        contador_femeninos = 0
        contador_otros = 0

        contador_IOT_edad = 0

        contador_femeninos_IA = 0
        acumulador_edad_femenino_IA = 0

        menor_edad_RV_RA = 0

    # Ingreso de datos:
        while seguir == True:
            nombre = input("Ingrese nombre: ")

            edad = input("Ingrese edad: ")
            edad = int(edad)
            while edad < 18:
                edad = input("Reingrese edad: ")
                edad = int(edad)
                
            genero = input("Ingrese genero: ")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reingrese genero: ")
                
            tecnologia = input("Ingrese tecnologia: ")
            while tecnologia != "IA" and tecnologia != "IOT" and tecnologia != "RV/RA":
                tecnologia = input("Reingrese tecnologia: ")
            
        # Procesamiento de datos (Se repite):
            match tecnologia:
                case "IA":
                    contador_IA += 1
                case "IOT":
                    contador_IOT += 1
                    if (edad > 18 and edad < 25) or (edad > 33 and edad < 42):
                        contador_IOT_edad += 1
                case _:
                    contador_RV_RA += 1
                    if edad < menor_edad_RV_RA or contador_RV_RA == 1 :
                        nombre_RV_RA = nombre
                        genero_RV_RA = genero      
                        menor_edad_RV_RA = edad

            match genero:
                case "Masculino":
                    contador_masculino += 1
                    if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
                        contador_masculino_IOT_IA += 1
                case "Femenino": 
                    contador_femeninos += 1
                    if tecnologia == "IA":
                        contador_femeninos_IA += 1
                        acumulador_edad_femenino_IA += edad
                case _:
                    contador_otros += 1     
            
            seguir = question("Seguir", "Ingresa otro empleado: ")
            
    # Procesamiento de datos (No se repite):
        if contador_IA == contador_IOT and contador_IA == contador_RV_RA:
            tecnologia_mas_votada = "Hubo empate entre los 3"
        elif contador_IA == contador_IOT:
            tecnologia_mas_votada = "Hubo empate entre IOT e IA"
        elif contador_IA == contador_RV_RA: 
            tecnologia_mas_votada = "Hubo empate entre IA y RV_RA"
        elif contador_IOT == contador_RV_RA: 
            tecnologia_mas_votada = "Hubo empate entre IOT Y RV_RA"
        elif contador_IOT > contador_IA and contador_IOT > contador_RV_RA: 
            tecnologia_mas_votada = "Se voto mas IOT"
        elif contador_IA > contador_RV_RA: 
            tecnologia_mas_votada = "Se voto mas IA"
        else:
            tecnologia_mas_votada = "Se voto mas RV/RA"

        total_empleados = contador_masculino = contador_femeninos + contador_otros

        porcentaje_masculinos = (porcentaje_masculinos * 100) / total_empleados
        porcentaje_femeninos = (porcentaje_femeninos * 100) / total_empleados
        porcentaje_otro = 100 - (porcentaje_masculinos + porcentaje_femeninos)

        porcentaje_IOT_edad = (porcentaje_IOT_edad * 100) / contador_IOT

        promedio_edad_femenino_IA = acumulador_edad_femenino_IA / contador_femeninos_IA

   # Salidas
        print(f"1. Cantidad masculino que votaron IOT/IA en el rango de edad: {contador_masculino_IOT_IA}")
        print(f"2. {tecnologia_mas_votada}")
        print(f"3. Porcentaje:\n\tMasculino: {porcentaje_masculinos}\n\Femenino: {porcentaje_femeninos}\n\Otros: {porcentaje_otro}")
        print(f"4. Porcentaje IOT rango edad: {porcentaje_IOT_edad}")
        print(f"5. Promedio de edad de los empleados de genero Femenino que votaron por IA: {promedio_edad_femenino_IA}")
        print(f"6. Nombre y género del empleado que voto por RV/RA con menor edad: {menor_edad_RV_RA}, {nombre_RV_RA}, {genero_RV_RA}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
