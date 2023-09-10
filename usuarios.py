class Usuario:
    def __init__(self, id, nombre, rol):
        self.id = id
        self.nombre = nombre
        self.rol = rol

# Definir usuarios
usuario1 = Usuario("051111407592", "Juan", "empleado", ["Zona A", "Zona B"])
usuario2 = Usuario("1234567890", "Maria", "empleado", ["Zona B", "Zona C"])
usuario3 = Usuario("29033706", "Pedro", "invitado", ["Zona A"])
usuarios = [usuario1, usuario2, usuario3]
