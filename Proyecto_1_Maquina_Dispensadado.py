#Proyecto Programado 1
#Hecho por Manuel Antonio Zapata Zamora
#Modulos usados Tkinter, time.

#Importación de Modulos para el manejo de interfaz
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import math
from threading import *
import time
from timeit import default_timer
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

#Definición de la Ventana Principal del Menú
ventana =Tk()
ventana.title("Máquina Dispensadora")
ventana.configure(background="#CCCCFF")
ventana.geometry("1000x650")
ventana.resizable(False,False)


#Definición de ventanas secundarias y sus funciones
def comprar_w():
    ventana.withdraw()
    comprarWindow=Toplevel()
    comprarWindow.title("Comprar/Buy")
    comprarWindow.minsize(800,550)
    comprarWindow.configure(background="#CCCCFF")
    comprarWindow.resizable(width=NO,height=NO)
    lienzo=Canvas(comprarWindow,width=700,height=400,bg="#CCCCFF")
    lienzo.place(x=50,y=60)
    #Aca van las funciones para la ventana de ventas
    
    
    
    def Pagar():#Funcion para generar ventana de metodo de pago del producto, así como el vuelto
        comprarWindow.withdraw()
        ventanaPago=Toplevel()
        ventanaPago.title("Pagar/Pay")
        ventanaPago.minsize(600,550)
        ventanaPago.configure(background="#CCCCFF")
        ventanaPago.resizable(width=NO,height=NO)
        print(var.get())
        lienzo=Canvas(ventanaPago,width=500,height=400,bg="#CCCCFF")
        lienzo.place(x=50,y=60)
        def finalizarCompra():#Funcion que finaliza la compra y genera el vuelto de la persona, luego se regresa a ventana principal
            tipo_moneda=moneda.get()
            if tipo_moneda==1:
                print(tipo_moneda)
            elif tipo_moneda==2:
                print(tipo_moneda)
            elif tipo_moneda==3:
                print(tipo_moneda)
            ventanaPago.destroy()
            ventana.deiconify()##Reaparece la ventana principal
        def boton_pago():
            opcion=moneda.get()
            if opcion==0:
                botonHome = Button(ventanaPago, text="Finalizar Compra", command=finalizarCompra,bg="#BF1134",fg="white",font=("Helvetica",15),state="disable")
                botonHome.place(x=50,y=475)
            else:
                botonHome = Button(ventanaPago, text="Finalizar Compra", command=finalizarCompra,bg="#BF1134",fg="white",font=("Helvetica",15),state="normal")
                botonHome.place(x=50,y=475)
            
        
          
        #Variabe de tipo mondeda
        moneda=IntVar()
        #Seleccion de método de Pago billete de mil, billete de 500 y moneda de 500
        radiobutton1=tk.Radiobutton(lienzo,text="Billete ₡1000",bg="#CCCCFF",  variable=moneda, value=1, command=boton_pago)
        radiobutton1.deselect()
        radiobutton1.place(x=10,y=20)
        radiobutton2=tk.Radiobutton(lienzo,text="Billete ₡500",bg="#CCCCFF",  variable=moneda, value=2, command=boton_pago)
        radiobutton2.deselect()
        radiobutton2.place(x=10,y=50)
        radiobutton3=tk.Radiobutton(lienzo,text="Moneda ₡500",bg="#CCCCFF",  variable=moneda, value=3, command=boton_pago)
        radiobutton3.deselect()
        radiobutton3.place(x=10,y=80)

        label1=tk.Label(ventanaPago,text="Seleccione el tipo de Pago",font=("Times New Roman","15"),foreground="Black",width=25, height=1, bg="#CCCCFF")
        label1.place(x=15,y=30)
        
            

        
        
        
        
        


        ventanaPago.mainloop()
        
    def close():#Funcion para cerrar el programa
        comprarWindow.destroy()
        ventana.deiconify()##Reaparece la ventana principal
    def GetVariable():#Funcion que captura el codigo del producto a comprar y habilita el boton de compra
        opcion=var.get()
        if opcion==0:
            botonHome = Button(comprarWindow, text="Pagar", command=close,bg="#BF1134",fg="white",font=("Helvetica",15),state="disable")
            botonHome.place(x=50,y=475)
        else:
            botonPagar=Button(comprarWindow, text="Pagar", command=Pagar,bg="#BF1134",fg="white",font=("Helvetica",15),state="normal")
            botonPagar.place(x=50,y=475)
            
            
        
        print(opcion)
    

    
        
    a_file = open("productos.txt", "r")#Leyendo el archivo de texto de productos disponibles

    m_datos = [] #Variable que lee el archivo de texto con los productos disponibles
    for line in a_file:#Ciclo que genera una matriz con los datos leidos del archivo .txt de los producto disponibles
        stripped_line = line.strip()
        line_list = stripped_line.split()
        m_datos.append(line_list)
    #print("-----Lista Generada------")
    #print(m_datos)
    #print(type(m_datos[1][2]))
    a_file.close()

    
    var=IntVar()
   
    #Etiquetas para la ventana de Compras
    
    label1=tk.Label(comprarWindow,text="Producto/Product",font=("Times New Roman","10"),foreground="Black",width=15, height=1, bg="#CCCCFF")
    label1.place(x=52,y=35)
    label2=tk.Label(comprarWindow,text="Precio/Price",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label2.place(x=185,y=35)
    label3=tk.Label(comprarWindow,text="Producto/Product",font=("Times New Roman","10"),foreground="Black",width=15, height=1, bg="#CCCCFF")
    label3.place(x=400,y=35)
    label4=tk.Label(comprarWindow,text="Precio/Price",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label4.place(x=540,y=35)
    label5=tk.Label(comprarWindow,text="Disponible",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label5.place(x=280,y=35)
    label6=tk.Label(comprarWindow,text="Disponible",font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label6.place(x=635,y=35)
    label7=tk.Label(lienzo,text=m_datos[1][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label7.place(x=215,y=20)
    label8=tk.Label(lienzo,text=m_datos[2][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label8.place(x=215,y=50)
    label9=tk.Label(lienzo,text=m_datos[3][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label9.place(x=215,y=80)
    label10=tk.Label(lienzo,text=m_datos[4][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label10.place(x=215,y=110)
    label11=tk.Label(lienzo,text=m_datos[5][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label11.place(x=215,y=140)
    label12=tk.Label(lienzo,text=m_datos[6][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label12.place(x=215,y=170)
    label13=tk.Label(lienzo,text=m_datos[7][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label13.place(x=215,y=200)
    label14=tk.Label(lienzo,text=m_datos[8][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label14.place(x=215,y=230)
    label15=tk.Label(lienzo,text=m_datos[9][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label15.place(x=560,y=20)
    label16=tk.Label(lienzo,text=m_datos[10][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label16.place(x=560,y=50)
    label17=tk.Label(lienzo,text=m_datos[11][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label17.place(x=560,y=80)
    label18=tk.Label(lienzo,text=m_datos[12][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label18.place(x=560,y=110)
    label19=tk.Label(lienzo,text=m_datos[13][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label19.place(x=560,y=140)
    label20=tk.Label(lienzo,text=m_datos[14][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label20.place(x=560,y=170)
    label21=tk.Label(lienzo,text=m_datos[15][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label21.place(x=560,y=200)
    label22=tk.Label(lienzo,text=m_datos[9][2],font=("Times New Roman","10"),foreground="Black",width=10, height=1, bg="#CCCCFF")
    label22.place(x=560,y=230)

    
    #Definición de botones en ventana de compras
    
    
    botonHome = Button(comprarWindow, text="Cancelar", command=close,bg="#BF1134",fg="white",font=("Helvetica",15),state="normal")
    botonHome.place(x=650,y=475)
    radiobutton1=tk.Radiobutton(lienzo,text="1 Coca Lata                ₡500",bg="#CCCCFF",  variable=var, value=1, command=GetVariable)
    radiobutton1.deselect()
    radiobutton1.place(x=10,y=20)
    radiobutton2 = tk.Radiobutton(lienzo,text="2 Coca Lata Light      ₡500",bg="#CCCCFF", variable=var, value=2, command=GetVariable)
    radiobutton2.deselect()
    radiobutton2.place(x=10,y=50)
    radiobutton3 = tk.Radiobutton(lienzo,text="3 Coca Desechable   ₡1000",bg="#CCCCFF", variable=var, value=3, command=GetVariable)
    radiobutton3.deselect()
    radiobutton3.place(x=10,y=80)
    radiobutton4 = tk.Radiobutton(lienzo,text="4 Fanta Lata               ₡500",bg="#CCCCFF", variable=var, value=4, command=GetVariable)
    radiobutton4.deselect()
    radiobutton4.place(x=10,y=110)
    radiobutton5 = tk.Radiobutton(lienzo,text="5 Fanta Desechable  ₡500",bg="#CCCCFF", variable=var, value=5, command=GetVariable)
    radiobutton5.deselect()
    radiobutton5.place(x=10,y=140)
    radiobutton6 = tk.Radiobutton(lienzo,text="6 Pepsi Lata               ₡500",bg="#CCCCFF", variable=var, value=6, command=GetVariable)
    radiobutton6.deselect()
    radiobutton6.place(x=10,y=170)
    radiobutton7 = tk.Radiobutton(lienzo,text="7 Pepsi Desechable  ₡500", bg="#CCCCFF",variable=var, value=7, command=GetVariable)
    radiobutton7.deselect()
    radiobutton7.place(x=10,y=200)
    radiobutton8 = tk.Radiobutton(lienzo,text="8 Gin Lata                  ₡500", bg="#CCCCFF",variable=var, value=8, command=GetVariable)
    radiobutton8.deselect()
    radiobutton8.place(x=10,y=230)
    radiobutton9 = tk.Radiobutton(lienzo,text="9 Coca Desechable         ₡500", bg="#CCCCFF",variable=var, value=9, command=GetVariable)
    radiobutton9.deselect()
    radiobutton9.place(x=350,y=20)
    radiobutton10 = tk.Radiobutton(lienzo,text="10 Fresco Leche              ₡500", bg="#CCCCFF",variable=var, value=10, command=GetVariable)
    radiobutton10.deselect()
    radiobutton10.place(x=350,y=50)
    radiobutton11 = tk.Radiobutton(lienzo,text="11 Galleta Chiki               ₡500", bg="#CCCCFF",variable=var, value=11, command=GetVariable)
    radiobutton11.deselect()
    radiobutton11.place(x=350,y=80)
    radiobutton12 = tk.Radiobutton(lienzo,text="12 Pinguino                     ₡500", bg="#CCCCFF",variable=var, value=12, command=GetVariable)
    radiobutton12.deselect()
    radiobutton12.place(x=350,y=110)
    radiobutton13 = tk.Radiobutton(lienzo,text="13 Platanitos verdes       ₡500", bg="#CCCCFF",variable=var, value=13, command=GetVariable)
    radiobutton13.deselect()
    radiobutton13.place(x=350,y=140)
    radiobutton14 = tk.Radiobutton(lienzo,text="14 Platanitos maduros   ₡500", bg="#CCCCFF",variable=var, value=14, command=GetVariable)
    radiobutton14.deselect()
    radiobutton14.place(x=350,y=170)
    radiobutton15 = tk.Radiobutton(lienzo,text="15 Takis                            ₡500", bg="#CCCCFF",variable=var, value=15, command=GetVariable)
    radiobutton15.deselect()
    radiobutton15.place(x=350,y=200)
    radiobutton16 = tk.Radiobutton(lienzo,text="16 Papas                          ₡500", bg="#CCCCFF",variable=var, value=16, command=GetVariable)
    radiobutton16.deselect()
    radiobutton16.place(x=350,y=230)
    
    


    comprarWindow.mainloop()
    
    
    
    


#Definicón de Labels en la ventana Principal
Label1=tk.Label(text="Welcome/Bienvenido",font=("Times New Roman","20"),foreground="Black",width=30, height=1, bg="#CCCCFF")

#Definición de Botones para la ventana Principal
boton_comprar=Button(ventana,text="Buy/Comprar",font=("Helvetica",15),background="Magenta",command=comprar_w)
boton_admin=Button(ventana,text="Administrador/Administrator",font=("Helvetica",15),background="Magenta",command=None)
boton_about=Button(ventana,text="About",font=("Helvetica",15),background="Magenta",command=None)


#Colacación de los Label y botones en ventana principal
#Labeles
Label1.place(x=250,y=50)
#Botones
boton_comprar.place(x=400, y= 150)
boton_admin.place(x=350,y=250)
boton_about.place(x=430,y=350)



ventana.mainloop()
