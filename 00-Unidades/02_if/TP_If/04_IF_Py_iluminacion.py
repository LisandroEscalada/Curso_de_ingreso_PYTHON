import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Lisandro
apellido: Escalada
---
TP: IF_Iluminacion
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.

        Entrada:
            Cantidad
            Marca
        Procesos:
            1. Calculamos el precio sin descuento(cantidad * 800)
            2. Averiguar cual ers descuento que tengo que aplicar(Segun cantidad y marca)
            3. Aplicar el descuento
            4. Verificar y aplicar descuento extra

        Salidas:
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = self.combobox_cantidad.get()
        cantidad = int(cantidad) #Parseo

        total_precio = cantidad * 800
        descuento = 0

        # if marca
        # match cantidad

        # if cantidad
        # match marca
        # match marca
        # match cantidad
        
        descuento_aplicar = (total_precio * descuento) / 100
        total = total_precio - descuento
        print(total)


        # if cantidad >= 6:
        #     descuento = (total_precio * 50) / 100
        #     total = total_precio - descuento
        # else:
        #     if cantidad == 5 and marca == "ArgentinaLuz":
        #         descuento = (total_precio * 40) / 100
        #         total = total_precio - descuento
        #     else:
        #         if cantidad == 5 and not(marca == "ArgentinaLuz"):
        #             descuento = (total_precio * 30) / 100
        #             total = total_precio - descuento
        #         else:
        #             if cantidad == 4 and (marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
        #                 descuento = (total_precio * 25) / 100
        #                 total = total_precio - descuento
        #             else:
        #                 if cantidad == 4 and(marca != "ArgentinaLuz" or marca != "FelipeLamparas"):
        #                     descuento = (total_precio * 20) / 100
        #                     total = total_precio - descuento
        #                 else:
        #                     if cantidad == 3 and marca == "ArgentinaLuz":
        #                         descuento = (total_precio * 15) / 100
        #                         total = total_precio - descuento
        #                     else:
        #                         if cantidad == 3 and marca == "FelipeLamparas":
        #                             descuento = (total_precio * 10) / 100
        #                             total = total_precio - descuento
        #                         else:
        #                             if cantidad == 3 and (marca != "ArgentinaLuz" or marca != "FelipeLamparas"):
        #                                 descuento = (total_precio * 5) / 100
        #                                 total = total_precio - descuento
                     
        # print(total)


        # if cantidad >= 6:
        #     descuento = 50
        # elif cantidad == 5 and marca == "ArgentinaLuz":
        #     descuento = 40
        # elif cantidad == 5 and not(marca == "ArgentinaLuz"):
        #     descuento = 30
        # elif cantidad == 4 and(marca == "ArgentinaLuz" or marca == "FelipeLamparas"):
        #     descuento = 25
        # elif cantidad == 4 and(marca != "ArgentinaLuz" or marca != "FelipeLamparas"):
        #     descuento = 20
        # elif cantidad == 3 and marca == "ArgentinaLuz":
        #     descuento = 15
        # elif cantidad == 3 and marca == "FelipeLamparas":
        #     descuento = 10
        # elif cantidad == 3 and(marca != "ArgentinaLuz" or marca != "FelipeLamparas"):
        #     descuento = 5

        # descuento_aplicar = (total_precio * descuento) / 100
        # total = total_precio - descuento_aplicar                 
        # print(total)


        # if cantidad >= 6:
        #     descuento = 50
        # elif cantidad == 5:
        #     if marca == "ArgentinaLuz":
        #         descuento = 40
        #     else: 
        #         descuento = 30
        # elif cantidad == 4:
        #     if marca == "ArgentinaLuz" or marca == "FelipeLamparas":
        #         descuento = 25
        #     else:
        #         descuento = 20
        # elif cantidad == 3:
        #     if marca == "ArgentinaLuz":
        #         descuento = 15
        #     elif marca == "FelipeLamparas":
        #         descuento = 10
        #     else:
        #         descuento = 5
        
        # descuento_aplicar = (total_precio * descuento) / 100
        # total = total_precio - descuento
        # print(total)
 

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()