import tkinter as tk

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Interfaz con Botones")
        self.ventana.geometry("400x300")

        self.boton1 = tk.Button(self.ventana, text="Escanear", command=self.abrir_ventana1)
        self.boton2 = tk.Button(self.ventana, text="Ingresar invitado", command=self.abrir_ventana2)
        self.boton3 = tk.Button(self.ventana, text="Historial de entradas", command=self.abrir_ventana3)
        
        self.boton1.pack(pady=10)
        self.boton2.pack(pady=5)
        self.boton3.pack(pady=5)
        
    def abrir_ventana1(self):
        self.ventana.withdraw()
        ventana1 = tk.Toplevel(self.ventana)
        ventana1.title("Ventana 1")
        ventana1.geometry("400x300")
        
        boton_escanear = tk.Button(ventana1, text="Escanear", command=self.escanear)
        boton_volver1 = tk.Button(ventana1, text="Volver", command=lambda: self.volver_a_principal(ventana1))
        
        boton_escanear.pack(pady=10)
        boton_volver1.pack(pady=5)
    
    def abrir_ventana2(self):
        self.ventana.withdraw()
        ventana2 = tk.Toplevel(self.ventana)
        ventana2.title("Ventana 2")
        ventana2.geometry("400x300")
        
        mensaje2 = tk.Label(ventana2, text="Ingresar Invitado")
        boton_volver2 = tk.Button(ventana2, text="Volver", command=lambda: self.volver_a_principal(ventana2))
        
        mensaje2.pack(pady=20)
        boton_volver2.pack(pady=5)
    
    def abrir_ventana3(self):
        self.ventana.withdraw()
        ventana3 = tk.Toplevel(self.ventana)
        ventana3.title("Ventana 3")
        ventana3.geometry("400x300")
        
        mensaje3 = tk.Label(ventana3, text="Historial de entradas")
        boton_volver3 = tk.Button(ventana3, text="Volver", command=lambda: self.volver_a_principal(ventana3))
        
        mensaje3.pack(pady=20)
        boton_volver3.pack(pady=5)
    
    def escanear(self):
        print("Escaneando en la ventana 1...")
    
    def volver_a_principal(self, ventana):
        ventana.withdraw()
        self.ventana.deiconify()
    
    def main(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = Interfaz(ventana_principal)
    app.main()
