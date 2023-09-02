#Definicion de clase de accesos
class Acceso:
    def __init__(self, id_usuario, id_zona, fecha_acceso, bandera_entrada_salida, estado_acceso):
        self.id_usuario = id_usuario
        self.id_zona = id_zona
        self.fecha_acceso = fecha_acceso
        self.bandera_entrada_salida = bandera_entrada_salida
        self.estado_acceso = estado_acceso