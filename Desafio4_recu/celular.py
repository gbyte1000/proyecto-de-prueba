class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.aplicaciones = []
        self.contactos = []

    def instalar_aplicacion(self, aplicacion):
        self.aplicaciones.append(aplicacion)

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def mostrar_aplicaciones(self):
        """
        Muestra todas las aplicaciones instaladas en el celular con el formato Nombre vVersion.
        Ejemplo Instagram v1.2.3
        """
        for aplicacion in self.aplicaciones:
            print(f"{aplicacion.nombre} v{aplicacion.version}")

    def mostrar_contactos(self):
        """
        Muestra todos los contactos guardados en el celular con el formato Nombre - Numero
        """
        for contacto in self.contactos:
            print(f"{contacto.nombre} - {contacto.numero}")

    def actualizar_aplicacion(self, aplicacion, nueva_version):
        """
        Actualiza la versión de una aplicación específica.
        Si la aplicación no está instalada en el celular, se debe manejar ese caso de manera adecuada.
        """
        if aplicacion in self.aplicaciones:
                aplicacion.version = nueva_version
                print("La app se actualizo")
        else:
                print(f"La app {aplicacion.nombre} no esta instalada")            

            
    def limpiar_aplicaciones(self, version_minima):
        """
        Elimina las aplicaciones que tengan una versión inferior a la especificada.
        Las versiones serán siempre del tipo x.y.z, en donde x, y, z pueden valer un solo dígito 1-9.
        La mínima versión posible será la 1.0.0, y la máxima 9.9.9
        """
        for app in self.aplicaciones:
            if app.version < version_minima:
                self.aplicaciones.remove(app)

    def eliminar_contacto(self, contacto):
        """
        Elimina un contacto de la lista de contactos del celular.
        Si el contacto no existe en la lista de contactos del celular, se debe manejar ese caso de manera adecuada.
        """
        if contacto in self.contactos:
            self.contactos.remove(contacto)
            print("contacto eliminado correctamente")
        else:
            print(f"El contacto {contacto.nombre} no existe")