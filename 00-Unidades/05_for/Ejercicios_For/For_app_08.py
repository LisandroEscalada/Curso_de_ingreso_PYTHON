import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lisandro
apellido: Escalada
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(input("Ingrese un numero: "))
        primo = True
        cantidad_num_primo = 0

        for i in range(2, numero):
            if numero % i == 0:
                primo = False
                break

        print(f"Números primos entre 1 y {numero}:")
        for num in range(2, numero + 1):
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                cantidad_num_primo += 1
                print(num)
        print(f"Cantidad de numeros primos: {cantidad_num_primo}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()