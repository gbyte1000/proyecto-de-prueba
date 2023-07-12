class AppMusica:
    def __init__(self, nombre):
        """
        Inicializa una nueva aplicación de música con un nombre.
        """
        self.nombre = nombre
        self.usuarios = []
        self.artistas = []
        self.canciones = []

    def agregar_usuario(self, usuario):
        """
        Agrega un usuario a la lista de usuarios de la aplicación.
        """
        self.usuarios.append(usuario)

    def agregar_artista(self, artista):
        """
        Agrega un artista a la lista de artistas de la aplicación.
        """
        self.artistas.append(artista)

    def agregar_cancion(self, cancion):
        """
        Agrega una canción a la lista de canciones de la aplicación.
        """
        self.canciones.append(cancion)

    def mostrar_usuarios(self):
        """
        Muestra todos los usuarios de la aplicación.
        """
        for usuario in self.usuarios:
            print(f"Usuario: {usuario.nombre}")

    def mostrar_artistas(self):
        """
        Muestra todos los artistas de la aplicación.
        """
        for artista in self.artistas:
            print(f"Artistas: {artista.nombre}")

    def mostrar_canciones(self):
        """
        Muestra todas las canciones de la aplicación.
        """
        for cancion in self.canciones:
            print(f"Canciones: {cancion.nombre} de {cancion.artista.nombre}")