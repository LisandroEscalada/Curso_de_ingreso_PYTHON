import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lisandro
apellido: Escalada
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        jr_minor_age = float("inf")
        name_jr_minor_age = "N/A" 
        tecnology_applicants = ""

        nb_asp_js_ssr = 0 

        nb_amount = 0 
        m_amount = 0 
        f_amount = 0 

        nb_age = 0 
        m_age = 0 
        f_age = 0 

        m_average_age = 0 
        f_average_age = 0 
        nb_average_age = 0 

        python_amount = 0 
        js_amount = 0 
        aspnet_amount = 0 
        
        m_percentage_age = 0 
        f_percentage_age = 0 
        nb_percentage_age = 0

        for i in range(2):
            name = input("Nombre: ")
            age = int(input("Edad: "))
            while age < 18:
                age = int(input("Mayor de edad: "))

            gender = input("Genero: ")
            while "F" != gender != "M" and gender != "NB":
                gender = input("F, M o NB: ")
            
            tecnology = input("Tecnologia: ")
            while "PYTHON" != tecnology != "JS" and tecnology != "ASP.NET":
                tecnology = input("PYTHON, JS o ASP.NET")

            position = input("Puesto: ")
            while "JR" != position != "SSR" and position != "SR":
                position = input("JR, SSR O SR: ")

        # c. Promedio de edades por género.
            if gender == "M":
                m_amount += 1
                m_age += age
            elif gender == "F":
                f_amount += 1
                f_age += age
            else:
                nb_amount += 1
                nb_age += age

        # d. Tecnologia con mas postulantes (solo hay una).
            if tecnology == "PYTHON":
                python_amount += 1
            elif tecnology == "JS":
                js_amount += 1
            else:
                aspnet_amount += 1
        # a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
                if position == "SR" and 25 < age < 40 and tecnology == "ASP.NET" or tecnology == "JR":
                    nb_asp_js_ssr += 1

        # b. Nombre del postulante Jr con menor edad.
        if position == "JR":
            if age < jr_minor_age:
                jr_minor_age = age
                name_jr_minor_age = name

        # d. Tecnologia con mas postulantes (solo hay una).
        python_tie = python_amount == js_amount
        js_tie = js_amount == aspnet_amount
        aspnet_tie = aspnet_amount == python_amount

        if aspnet_amount < python_amount > js_amount:
            tecnology_applicants = "PYTHON"
        elif aspnet_amount < js_amount > python_amount:
            tecnology_applicants = "JS"
        elif python_amount < aspnet_amount > js_amount:
             tecnology_applicants = "ASP.NET"
        elif python_amount and js_amount and aspnet_amount:
            tecnology_applicants = "Hubo empate entre los tres"
        elif python_amount:
            tecnology_applicants = "Hubo empate entre python y js"
        elif js_amount: 
            tecnology_applicants = "Hubo empate entre js y asp.net"
        else:
            tecnology_applicants = "Hubo empate entre asp.net y python"   

        # c. Promedio de edades por género.
        m_percentage_age = (m_amount / m_age) * 100 if m_age != 0 else 0
        f_percentage_age = (f_amount / f_age) * 100 if f_age != 0 else 0
        nb_percentage_age = (nb_amount / nb_age) * 100 if nb_age != 0 else 0

        m_average_age = m_age / m_amount if m_age != 0 else 0
        f_average_age = f_age / f_amount if f_age != 0 else 0
        nb_average_age = nb_age / nb_amount if nb_age != 0 else 0

        print(f"A. Cantidad de postulantes de genero (NB) que programan en ASP.NET o JS cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr: {nb_asp_js_ssr}.")
        print(f"B. Nombre del postulante Jr con menor edad: {name_jr_minor_age}.")
        print(f"Promedio de edad masculina: {m_average_age}, femenina: {f_average_age} y no binario: {nb_average_age}.")
        print(f"D. Tecnologia con mas postulantes: {tecnology_applicants}.")
        print(f"Porcentaje de edad masculina: {m_percentage_age}%, femenina: {f_percentage_age}% y no binario: {nb_percentage_age}%.")
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
