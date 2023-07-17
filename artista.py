class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def lanzar_cancion(self, cancion):
        self.canciones.append(cancion)

    def generar_tag(self):
        pass