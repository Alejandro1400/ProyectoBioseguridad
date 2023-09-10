import sqlite3
import pandas as pd
import tkinter as tk
from tkinter import filedialog  # Importa el módulo de diálogo de selección de archivos
from zonas import Zona
from usuarios import Usuario
from accesos import Acceso

#------------------------------------------------------------
# Inicialización de la base de datos	
#------------------------------------------------------------

def drop_tables(conn):
    conn.execute('DROP TABLE IF EXISTS usuarios')
    conn.execute('DROP TABLE IF EXISTS zonas')
    conn.execute('DROP TABLE IF EXISTS accesos')

def create_tables(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id TEXT PRIMARY KEY,
            nombre TEXT,
            rol TEXT
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS zonas (
            id TEXT PRIMARY KEY,
            nombre TEXT UNIQUE,
            descripcion TEXT,
            animales TEXT,
            restricciones TEXT,
            roles_permitidos TEXT
        )
    ''')

    conn.execute('''
        CREATE TABLE IF NOT EXISTS accesos (
            id_entrada INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario TEXT,
            id_zona TEXT,
            fecha_acceso TEXT,
            bandera_entrada_salida TEXT CHECK (bandera_entrada_salida IN ('entrada', 'salida'))
            estado_acceso TEXT CHECK (estado_acceso IN ('aceptado', 'denegado'))
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
            FOREIGN KEY (id_zona) REFERENCES zonas(id)
        )
    ''')

#------------------------------------------------------------
# Funciones para insertar datos en la base de datos
#------------------------------------------------------------

def insertar_usuario(conn, usuario):
    conn.execute('''
        INSERT INTO usuarios (id, nombre, rol)
        VALUES (?, ?, ?, ?)
    ''', (usuario.id, usuario.nombre, usuario.rol, ', '.join(usuario.zonas_permiso)))

def insertar_zona(conn, zona):
    conn.execute('''
        INSERT INTO zonas (id, nombre, descripcion, animales, restricciones, roles_permitidos)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (zona.id, zona.nombre, zona.descripcion, ', '.join(zona.animales), ', '.join(zona.restricciones), ', '.join(zona.acceso_usuarios)))

def insertar_acceso(conn, acceso):
    conn.execute('''
        INSERT INTO accesos (id_usuario, id_zona, fecha_acceso, bandera_entrada_salida, estado_acceso)
        VALUES (?, ?, ?, ?, ?)
    ''', (acceso.id_usuario, acceso.id_zona, acceso.fecha_acceso, acceso.bandera_entrada_salida, acceso.estado_acceso))


#------------------------------------------------------------
# Funciones para cargar datos desde un excel
# Datos de usuarios y zonas
#------------------------------------------------------------

def cargar_datos_usuarios(db_name, excel_file):
    conn = sqlite3.connect(db_name)

    try:
        # Lee el archivo Excel
        df = pd.read_excel(excel_file)

        # Inserta usuarios
        for _, row in df.iterrows():
            usuario = Usuario(
                id=row['id'],
                nombre=row['nombre'],
                rol=row['rol']
            )
            insertar_usuario(conn, usuario)

        conn.commit()
        print("Datos de usuarios cargados exitosamente.")
    except Exception as e:
        conn.rollback()
        print(f"Error al cargar datos de usuarios desde el archivo Excel: {str(e)}")
    finally:
        conn.close()

def cargar_datos_zonas(db_name, excel_file):
    conn = sqlite3.connect(db_name)

    try:
        # Lee el archivo Excel
        df = pd.read_excel(excel_file)

        # Inserta zonas
        for _, row in df.iterrows():
            zona = Zona(
                id=row['id'],
                nombre=row['nombre'],
                descripcion=row['descripcion'],
                animales=row['animales'].split(';'),  # Divide los valores separados por ';'
                restricciones=row['restricciones'].split(';'),  # Divide los valores separados por ';'
                roles_permitidos=row['acceso_usuarios'].split(';')  # Divide los valores separados por ';'
            )
            insertar_zona(conn, zona)

        conn.commit()
        print("Datos de zonas cargados exitosamente.")
    except Exception as e:
        conn.rollback()
        print(f"Error al cargar datos de zonas desde el archivo Excel: {str(e)}")
    finally:
        conn.close()

#------------------------------------------------------------
# Funciones para mostrar datos de la base de datos
#------------------------------------------------------------

def mostrar_usuarios(conn):
    cursor = conn.cursor()

    # Fetch data from usuarios table
    cursor.execute('SELECT * FROM usuarios')
    usuarios_data = cursor.fetchall()
    print("Usuarios:")
    for row in usuarios_data:
        print(row)

def mostrar_zonas(conn):
    cursor = conn.cursor()

    # Fetch data from zonas table
    cursor.execute('SELECT * FROM zonas')
    zonas_data = cursor.fetchall()
    print("\nZonas:")
    for row in zonas_data:
        print(row)

def mostrar_accesos(conn):
    cursor = conn.cursor()

    # Fetch data from accesos table
    cursor.execute('SELECT * FROM accesos')
    accesos_data = cursor.fetchall()
    print("\nAccesos:")
    for row in accesos_data:
        print(row)


#------------------------------------------------------------
# Funciones para obtener en sus clases los datos de la base de datos
#------------------------------------------------------------

def obtener_usuarios(conn):
    cursor = conn.cursor()

    # Fetch data from usuarios table
    cursor.execute('SELECT * FROM usuarios')
    usuarios_data = cursor.fetchall()
    usuarios = []
    for row in usuarios_data:
        usuario = Usuario(
            id=row[0],
            nombre=row[1],
            rol=row[2]
        )
        usuarios.append(usuario)
    return usuarios

def obtener_zonas(conn):
    cursor = conn.cursor()

    # Fetch data from zonas table
    cursor.execute('SELECT * FROM zonas')
    zonas_data = cursor.fetchall()
    zonas = []
    for row in zonas_data:
        zona = Zona(
            id=row[0],
            nombre=row[1],
            descripcion=row[2],
            animales=row[3].split(', '),
            restricciones=row[4].split(', '),
            roles_permitidos=row[5].split(', ')
        )
        zonas.append(zona)
    return zonas

def obtener_accesos(conn):
    cursor = conn.cursor()

    # Fetch data from accesos table
    cursor.execute('SELECT * FROM accesos')
    accesos_data = cursor.fetchall()
    accesos = []
    for row in accesos_data:
        acceso = Acceso(
            id_entrada=row[0],
            id_usuario=row[1],
            id_zona=row[2],
            fecha_acceso=row[3],
            bandera_entrada_salida=row[4],
            estado_acceso=row[5]
        )
        accesos.append(acceso)
    return accesos

#------------------------------------------------------------
# Funciones para mostrar el diálogo de selección de archivos
#------------------------------------------------------------

# Función para mostrar el diálogo de selección de archivos
def seleccionar_archivo_excel():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de tkinter
    file_path = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=[("Archivos Excel", "*.xlsx")])
    return file_path

#------------------------------------------------------------
# Función principal
#------------------------------------------------------------

def main():

    # Prompt user for the name of the place and the database filename
    db_filename = input("Enter the desired database filename (without extension): ")  
    db_name = f"{db_filename}.db"  
    conn = sqlite3.connect(db_name)

    # Enable FOREIGN KEY constraint enforcement
    conn.execute('PRAGMA foreign_keys = ON;')

    create_tables(conn)

    # Utiliza el diálogo de selección de archivos para obtener la ruta del archivo Excel de usuarios
    print("Selecciona el archivo Excel de usuarios")
    excel_file_usuarios = seleccionar_archivo_excel()

    if excel_file_usuarios:
        cargar_datos_usuarios(db_name, excel_file_usuarios)

        # Utiliza el diálogo de selección de archivos para obtener la ruta del archivo Excel de zonas
        print("Selecciona el archivo Excel de zonas")
        excel_file_zonas = seleccionar_archivo_excel()

        if excel_file_zonas:
            cargar_datos_zonas(db_name, excel_file_zonas)


    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()

