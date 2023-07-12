class Usuario:
    def __init__(self, nombre):
        """
        Inicializa un nuevo usuario con un nombre.
        """
        self.nombre = nombre
        self.playlist = []
        self.artistas_seguidos = []

    def seguir_artista(self, artista):
        """
        Agrega un artista a la lista de artistas seguidos por el usuario.
        """
        self.artistas_seguidos.append(artista)

    def agregar_cancion_playlist(self, cancion):
        """
        Agrega una canción a la lista de reproducción del usuario.
        """
        self.playlist.append(cancion)

    def eliminar_cancion_playlist(self, cancion):
        """
        Elimina una canción de la lista de reproducción del usuario.
        """
        self.playlist.remove(cancion)

    def reproducir_cancion(self, cancion):
        """
        Simula la reproducción de una canción por parte del usuario.
        Ejemplo: Maxi está reproduciendo Bones de Imagine Dragons.
        """
        return f"{self.nombre} está reproduciendo {cancion.nombre} de {cancion.artista.nombre}"

    def escuchar_artista(self, artista):
        """
        Reproduce todas las canciones del artista si el usuario sigue al artista.
        Ejemplo: Maxi está escuchando todas las canciones de Imagine Dragons.
        Se reproduce cada una de las canciones luego de ese mensaje.
        Debe considerar el caso en el que el usuario no siga al artista y
        manejar ese caso individualmente.
        """
        if artista in self.artistas_seguidos:
            print(f"{self.nombre} está reproduciendo todas las canciones de {artista.nombre}")
            for cancion in artista.canciones:
                print(f"Ahora estas escuchando {cancion.nombre} de {artista.nombre} ")
        else:
            print("Usted no sigue a ese artista :) ")