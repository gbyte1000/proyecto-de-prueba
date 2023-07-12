class Artista:
    def __init__(self, nombre):
        """
        Inicializa un nuevo artista con un nombre.
        """
        self.nombre = nombre
        self.canciones = []

    def lanzar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones del artista.
        """
        self.canciones.append(cancion)