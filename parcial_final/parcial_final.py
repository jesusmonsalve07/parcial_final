from tkinter import Tk, Label, Frame, Canvas, Button, StringVar, Entry, Toplevel

#---------------------------
#------plano cartesiano-----
#---------------------------


base = 480
altura = 400 

def mostrar_posicion():
(x,y) = frame_graficacion.winfo_pointerxy()
root_x = frame_graficacion.winfo_rootx()
root_y = frame_graficacion.winfo_rooty()
ancho_pantalla = frame_graficacion.winfo_width()
altura_pantalla = frame_graficacion.winfo_height() 
mouse_x = x - root_x
mouse_y = y - root_y 
if mouse_x < 0 or mouse_x > ancho_pantalla or mouse_y < 0 or mouse_y > altura_pantalla: 
    mouse_x = -1
    mouse_y = -1


etiqueta.configure (text=str(mouse_x) + "," + str(mouse_y)) 
frame_graficacion.after(10, mostrar_posicion) 


def calcular_pendiente():
    print("hola :D")
 

def graficas():
    C.create_line(14, 18, 250, 210, fill = "blue", width=5)
 

 #----------------------------
 # VENTANA PRINCIPAL
 #----------------------------


ventana_principal = Tk()
ventana_principal.title("Plano cartesiano")
ventana_principal.resizable(False, False)
ventana_principal.config(bg = "green")
ventana_principal.geometry("600x600")

#--------------------------------
# FRAME GRAFICACION
#-------------------------------


frame_graficacion = Frame(ventana_principal) 
frame_graficacion.config(bg = "white", width="480", height = "400")
frame_graficacion.pack(fill = BOTH, padx= 10, pady=10)


#------------------------------
# CREAR CANVA 
#-----------------------------

C = Canvas(frame_graficacion, width = BASE, height = ALTURA)
C.place(X =10, Y = 10)

#----------------------------
# BOTON
#----------------------------

boton = Button(text="Calcular pendiente", padx=10,  fg="white", bg="green", command=calcular_pendiente)
boton.pack(side="left", padx=10, pady=10)
graficar = Button(text="Graficar", padx=10,  fg="white", bg="green", command=graficas)
graficar.pack(side="right", padx=10, pady=10)

# ----------------------
# LINEAS
#-----------------------

linea3 = C.create_line(BASE/2, 0, BASE/2, ALTURA/2, BASE/2, ALTURA, BASE/2, ALTURA/2, fill = "blue", width = 5)
linea4 = C.create_line(BASE, ALTURA/2, BASE/2, ALTURA/2, 0, ALTURA/2, BASE/2, ALTURA/2, fill = "green", width = 5)

# ----------------------
# COORDENADAS
# ----------------------
etiqueta = Label(text="-1, -1", font=("Arial", 20, "bold"))
etiqueta.pack(expand=True)
mostrar_posicion()

# ----------------------
# RECOLECTAR DATOS
# ----------------------


ventana_principal.mainloop()























root.mainloop()