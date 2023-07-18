class Aplicacion:
    def __init__(self, nombre, version):
        """
        El nombre es una cadena,
        La versión es una cadena con el formato x.y.z en donde x, y, z valen 1-9 únicamente
        La versión mínima es 1.0.0, y la máxima 9.9.9
        """
        self.nombre = nombre
        self.version = version