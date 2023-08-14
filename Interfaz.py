import tkinter as tk

def abrir_ventana(ventana):
    ventana_principal.withdraw()  # Ocultar ventana principal
    ventana.deiconify()          # Mostrar ventana nueva

def escanear():
    print("Escaneando en la ventana 1...")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Interfaz con Botones")

# Función para volver a la ventana principal
def volver_a_principal(ventana):
    ventana.withdraw()            # Ocultar ventana actual
    ventana_principal.deiconify() # Mostrar ventana principal

# Ventana 1
ventana1 = tk.Toplevel()
ventana1.title("Ventana 1")
boton_escanear = tk.Button(ventana1, text="Escanear", command=escanear)
boton_volver1 = tk.Button(ventana1, text="Volver", command=lambda: volver_a_principal(ventana1))
boton_escanear.pack(pady=10)
boton_volver1.pack(pady=5)

# Ventana 2
ventana2 = tk.Toplevel()
ventana2.title("Ventana 2")
mensaje2 = tk.Label(ventana2, text="Hola")
mensaje2.pack(pady=20)
boton_volver2 = tk.Button(ventana2, text="Volver", command=lambda: volver_a_principal(ventana2))
boton_volver2.pack(pady=5)

# Ventana 3
ventana3 = tk.Toplevel()
ventana3.title("Ventana 3")
mensaje3 = tk.Label(ventana3, text="Chao")
mensaje3.pack(pady=20)
boton_volver3 = tk.Button(ventana3, text="Volver", command=lambda: volver_a_principal(ventana3))
boton_volver3.pack(pady=5)

# Botones en la ventana principal
boton1 = tk.Button(ventana_principal, text="Botón 1", command=lambda: abrir_ventana(ventana1))
boton2 = tk.Button(ventana_principal, text="Botón 2", command=lambda: abrir_ventana(ventana2))
boton3 = tk.Button(ventana_principal, text="Botón 3", command=lambda: abrir_ventana(ventana3))
boton1.pack(pady=10)
boton2.pack(pady=5)
boton3.pack(pady=5)

# Iniciar el bucle principal de la interfaz gráfica
ventana_principal.mainloop()
