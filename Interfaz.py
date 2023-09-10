import tkinter as tk
from tkinter import ttk

def abrir_ventana(ventana):
    ventana_principal.withdraw()  # Ocultar ventana principal
    ventana.deiconify()          # Mostrar ventana nueva

def volver_a_principal(ventana):
    ventana.withdraw()            # Ocultar ventana actual
    ventana_principal.deiconify() # Mostrar ventana principal

def agregar_usuario():
    nombre = entry_nombre.get()
    cargo = entry_cargo.get()
    identificacion = entry_identificacion.get()

    if nombre and cargo and identificacion:
        tree.insert('', 'end', values=(nombre, cargo, identificacion))
        entry_nombre.delete(0, 'end')
        entry_cargo.delete(0, 'end')
        entry_identificacion.delete(0, 'end')

def agregar_zona():
    nombre_granja = entry_nombre_granja_zona.get()
    nombre_zona = entry_nombre_zona.get()
    codigo_zona = entry_codigo_zona.get()

    if nombre_granja and nombre_zona and codigo_zona:
        tree_zonas.insert('', 'end', values=(nombre_granja, nombre_zona, codigo_zona))
        entry_nombre_granja_zona.delete(0, 'end')
        entry_nombre_zona.delete(0, 'end')
        entry_codigo_zona.delete(0, 'end')

ventana_principal = tk.Tk()
ventana_principal.geometry("1024x728")
ventana_principal.title("Menú Principal")

titulo = tk.Label(ventana_principal, text="Proyecto Bioseguridad", font=("Arial", 25))
titulo.pack(pady=20)

subtitulo = tk.Label(ventana_principal, text="Por TorrSal.", font=("Arial", 15))
subtitulo.pack(pady=10)

boton1 = tk.Button(ventana_principal, text="Escanear", command=lambda: abrir_ventana(ventana_escaneo))
boton2 = tk.Button(ventana_principal, text="Ingresar usuario", command=lambda: abrir_ventana(ventana_ingreso_usuario))
boton3 = tk.Button(ventana_principal, text="Ingresar zona", command=lambda: abrir_ventana(ventana_ingreso_zona))
boton4 = tk.Button(ventana_principal, text="Historial de entradas", command=lambda: abrir_ventana(ventana_historial))

boton1.pack(pady=20)
boton2.pack(pady=20)
boton3.pack(pady=20)
boton4.pack(pady=20)

ventana_escaneo = tk.Toplevel()
ventana_escaneo.geometry("1024x728")
ventana_escaneo.title("Escaneo")

boton_volver_escaneo = tk.Button(ventana_escaneo, text="Volver", command=lambda: volver_a_principal(ventana_escaneo))
boton_volver_escaneo.pack(pady=20)
ventana_escaneo.withdraw()

ventana_ingreso_usuario = tk.Toplevel()
ventana_ingreso_usuario.geometry("1024x728")
ventana_ingreso_usuario.title("Ingreso de Usuarios")

entry_nombre = tk.Entry(ventana_ingreso_usuario, width=30)
entry_cargo = tk.Entry(ventana_ingreso_usuario, width=30)
entry_identificacion = tk.Entry(ventana_ingreso_usuario, width=30)

label_nombre = tk.Label(ventana_ingreso_usuario, text="Nombre:")
label_cargo = tk.Label(ventana_ingreso_usuario, text="Cargo:")
label_identificacion = tk.Label(ventana_ingreso_usuario, text="Número de identificación:")

boton_agregar = tk.Button(ventana_ingreso_usuario, text="Agregar Usuario", command=agregar_usuario)

label_nombre.pack(pady=10)
entry_nombre.pack(pady=10)
label_cargo.pack(pady=10)
entry_cargo.pack(pady=10)
label_identificacion.pack(pady=10)
entry_identificacion.pack(pady=10)
boton_agregar.pack(pady=20)

# Crear tabla para mostrar usuarios
frame_tabla = tk.Frame(ventana_ingreso_usuario)
frame_tabla.pack(pady=20)

tree = ttk.Treeview(frame_tabla, columns=("Nombre", "Cargo", "Número de Identificación"), show="headings")
tree.heading("Nombre", text="Nombre")
tree.heading("Cargo", text="Cargo")
tree.heading("Número de Identificación", text="Número de Identificación")
tree.pack()

boton_volver_usuario = tk.Button(ventana_ingreso_usuario, text="Volver", command=lambda: volver_a_principal(ventana_ingreso_usuario))
boton_volver_usuario.pack(pady=20)
ventana_ingreso_usuario.withdraw()

ventana_ingreso_zona = tk.Toplevel()
ventana_ingreso_zona.geometry("1024x728")
ventana_ingreso_zona.title("Ingreso de Zonas")

entry_nombre_granja_zona = tk.Entry(ventana_ingreso_zona, width=30)
entry_nombre_zona = tk.Entry(ventana_ingreso_zona, width=30)
entry_codigo_zona = tk.Entry(ventana_ingreso_zona, width=30)

label_nombre_granja_zona = tk.Label(ventana_ingreso_zona, text="Nombre de Granja:")
label_nombre_zona = tk.Label(ventana_ingreso_zona, text="Nombre de Zona:")
label_codigo_zona = tk.Label(ventana_ingreso_zona, text="Código de Zona:")

boton_agregar_zona = tk.Button(ventana_ingreso_zona, text="Agregar Zona", command=agregar_zona)

label_nombre_granja_zona.pack(pady=10)
entry_nombre_granja_zona.pack(pady=10)
label_nombre_zona.pack(pady=10)
entry_nombre_zona.pack(pady=10)
label_codigo_zona.pack(pady=10)
entry_codigo_zona.pack(pady=10)
boton_agregar_zona.pack(pady=20)

# Crear tabla para mostrar zonas
frame_tabla_zonas = tk.Frame(ventana_ingreso_zona)
frame_tabla_zonas.pack(pady=20)

tree_zonas = ttk.Treeview(frame_tabla_zonas, columns=("Nombre de Granja", "Nombre de Zona", "Código de Zona"), show="headings")
tree_zonas.heading("Nombre de Granja", text="Nombre de Granja")
tree_zonas.heading("Nombre de Zona", text="Nombre de Zona")
tree_zonas.heading("Código de Zona", text="Código de Zona")
tree_zonas.pack()

boton_volver_zona = tk.Button(ventana_ingreso_zona, text="Volver", command=lambda: volver_a_principal(ventana_ingreso_zona))
boton_volver_zona.pack(pady=20)
ventana_ingreso_zona.withdraw()

ventana_historial = tk.Toplevel()
ventana_historial.geometry("1024x728")
ventana_historial.title("Historial de Ingresos")

boton_volver_historial = tk.Button(ventana_historial, text="Volver", command=lambda: volver_a_principal(ventana_historial))
boton_volver_historial.pack(pady=20)
ventana_historial.withdraw()

ventana_principal.mainloop()
