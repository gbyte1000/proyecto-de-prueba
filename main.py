from appmusica import *
from usuario import *
from cancion import *
from artista import *

artista1 = Artista("Imagine Dragons")
artista2 = Artista("Lucas Cerati")

cancion1 = Cancion("Bones", 120, artista1)
cancion2 = Cancion("Huesos", 160, artista1)
artista1.lanzar_cancion(cancion1)
artista1.lanzar_cancion(cancion2)

cancion3 = Cancion("Te amo", 120, artista2)
cancion4 = Cancion("Ya no", 160, artista2)

usuario1 = Usuario("Damian")
usuario2 = Usuario("Daniel")

usuario1.seguir_artista(artista1)
usuario1.agregar_cancion_playlist(cancion1)
usuario1.agregar_cancion_playlist(cancion2)
cancion_reproducida = usuario1.reproducir_cancion(cancion1)
print(cancion_reproducida)

usuario1.escuchar_artista(artista1)

print("")
print("")
app_musica = AppMusica("Spotify")

app_musica.agregar_usuario(usuario1)
app_musica.agregar_usuario(usuario2)

app_musica.mostrar_usuarios()

print("")
app_musica.agregar_artista(artista1)
app_musica.agregar_artista(artista2)

app_musica.mostrar_artistas()

app_musica.agregar_cancion(cancion1)
app_musica.agregar_cancion(cancion2)
app_musica.agregar_cancion(cancion3)
app_musica.agregar_cancion(cancion4)

app_musica.mostrar_canciones()