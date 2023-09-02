class Zona:
    def __init__(self, nombre, descripcion, animales, restricciones, roles_permitidos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.animales = animales
        self.restricciones = restricciones
        self.roles_permitidos = roles_permitidos

# Definir zonas con acceso por rol
zona_a = Zona("Zona A", "Descripción de la Zona A", ["Leones", "Elefantes"], ["No alimentar a los animales"], ["empleado", "invitado"])
zona_b = Zona("Zona B", "Descripción de la Zona B", ["Tigres", "Jirafas"], ["Mantener distancia de seguridad"], ["empleado", "invitado"])
zona_c = Zona("Zona C", "Descripción de la Zona C", ["Monos", "Cocodrilos"], ["No hacer ruido fuerte"], ["empleado"])
zonas = [zona_a, zona_b, zona_c]
