import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lisandro 
apellido: Escalada
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
    # Inicializacion:
        seguir = True

        mayor_votos = 0

        suma_edades = 0
        cantidad_candidatos = 0
        total_votos = 0
    
    # Ingreso de datos:
        while seguir == True:
            nombre = input("Nombre del candidato: ")
            edad = input("Edad del candidato: ")
            edad = int(edad)  
            while edad < 25:
                edad = input("Debe ser mayor de 25 años: ")    
                edad = int(edad)     
            cantidad_votos = input("Cantidad de votos del candidato: ")
            cantidad_votos = int(cantidad_votos)
            while cantidad_votos < 0:
                cantidad_votos = input("No menor a cero: ")
                cantidad_votos = int(cantidad_votos)

        # Procesamiento de datos (Se repite):
            cantidad_candidatos += 1
            total_votos += cantidad_votos
            suma_edades += edad
    
            seguir = question("Seguir", "Ingresa otro candidato")

        # Procesamiento de datos (No se repite):

        promedio_edad = suma_edades / cantidad_candidatos

        # Salidas: 
        print(f"A. Nombre de candidato mas votado: ")
        print(f"B. Nombre y edad de candidato menos votado: ")
        print(f"C. Promedio de edad: {promedio_edad}")
        print(f"D. Total de votos: {total_votos}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
