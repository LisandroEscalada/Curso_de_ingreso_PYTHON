import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lisandro
apellido: Escalada
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_positivo = 0
        suma_negativo = 0
        cero_cantidad = 0
        positivo_cantidad = 0
        negativo_cantidad = 0
        diferencia = 0

        while True:
            numero = prompt("", "Ingrese su numero")
            if numero == None:
                break

            numero = float(numero)
         
            if numero > 0:
                suma_positivo += numero
                positivo_cantidad += 1
            if numero < 0:
                suma_negativo += numero
                negativo_cantidad += 1
            if numero == 0:
                cero_cantidad += 1

            diferencia = diferencia = positivo_cantidad - negativo_cantidad
                
        alert("Resultados", f"La suma acumulada de los negativos: {suma_negativo}, La suma acumulada de los positivos: {suma_positivo}, Cantidad de números positivos ingresados: {positivo_cantidad}, Cantidad de números negativos ingresados: {negativo_cantidad}, Cantidad de ceros: {cero_cantidad}, Diferencia entre la cantidad de los números positivos ingresados y los negativos: {diferencia}")
    
        # print(f"La suma acumulada de los negativos: {suma_negativo}")
        # print(f"La suma acumulada de los positivos: {suma_positivo}")
        # print(f"Cantidad de números positivos ingresados: {positivo_cantidad}")
        # print(f"Cantidad de números negativos ingresados: {negativo_cantidad}")
        # print(f"Cantidad de ceros: {cero_cantidad}")
        # print(f"Diferencia entre la cantidad de los números positivos ingresados y los negativos: {diferencia}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
