import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lisandro
apellido: Escalada
---
Ejercicio: Examen parcial sincrónico
---
Enunciado: De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:

Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál es el nivel más alcanzado de los jugadores
Informe B- El Porcentaje de jugadores de la categoría principiante sobre el total
Informe C- La categoría del participante de mayor edad
Informe D- El score y nombre del principiante con mayor score
Informe E- Promedio de score de los participantes intermedios.
'''

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        participantes = 0

        nivel_uno = 0
        nivel_dos = 0
        nivel_tres = 0

        principiante = 0
        intermedio = 0 
        avanzado = 0

        mayor_edad = float("-inf")
        categoria_mayor_edad = ""

        mayor_score = float("-inf")
        nombre_mayor_score = ""

        score_acumulador = 0

        for i in range(50):
            participantes += 1
            print(f"Participante Nº{participantes}/50")
            nombre = prompt("UTN-TETRIS", "Nombre: ")

            categoria = prompt("UTN-TETRIS", "Categoria: ")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria = prompt("Error", "Principiante, Intermedio o Avanzado: ")

            edad = int(prompt("UTN-TETRIS","Edad: "))
            while edad < 18 or edad > 99:
                edad = int(prompt("Error","Entre 18 y 99 inclusive: "))

            score = int(prompt("UTN-TETRIS", "Score: "))
            while score <= 0:
                score = int(prompt("Error","Mayor que 0: "))

            nivel = int(prompt("UTN-TETRIS","Nivel alcanzado: "))
            while nivel != 1 and nivel != 2 and nivel != 3:
                nivel = int(prompt("Error","1, 2 o 3: "))

            if nivel == 1:
                nivel_uno += 1
            elif nivel == 2:
                nivel_dos += 1
            else:
                nivel_tres += 1

            if categoria == "Principiante":
                principiante += 1
            elif categoria == "Intermedio":
                intermedio += 1
                score_acumulador += score
            else:
                avanzado += 1

            if edad > mayor_edad:
                mayor_edad = edad
                categoria_mayor_edad = categoria

            if score > mayor_score:
                mayor_score = score
                nombre_mayor_score = nombre

        if nivel_dos < nivel_uno > nivel_tres:
            nivel_maximo = "Nivel 1"
        elif nivel_uno < nivel_dos > nivel_tres:
            nivel_maximo = "Nivel 2"
        elif nivel_uno < nivel_tres > nivel_dos:
            nivel_maximo = "Nivel 3"

        total_categoria = principiante + intermedio + avanzado
        
        if principiante != 0:
            porcentaje_principiante = (principiante / total_categoria)
        else:
            porcentaje_principiante = 0

        if intermedio != 0:
            promedio_intermedio = score_acumulador / intermedio
        else:
            promedio_intermedio = 0

        print(f"A- Cuál es el nivel más alcanzado de los jugadores: {nivel_maximo}")
        print(f"B- El Porcentaje de jugadores de la categoría principiante sobre el total: {porcentaje_principiante}%")
        print(f"C- La categoría del participante de mayor edad: {categoria_mayor_edad}, {mayor_edad}")
        print(f"D- El score y nombre del principiante con mayor score: {mayor_score}, {nombre_mayor_score}")
        print(f"E- Promedio de score de los participantes intermedios: {promedio_intermedio}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
