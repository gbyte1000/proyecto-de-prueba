from aplicacion import *
from celular import *
from contacto import *

# Tarea 1: Instanciar un objeto Celular, dos Aplicaciones y dos Contactos.
moto99 = Celular("Motorola", "X99")
replit = Aplicacion("Replit", "1.0.2") 
vscode = Aplicacion("VSCode", "2.0.0") 
vim = Aplicacion("VIM", "3.0.0") 

ivana = Contacto("Ivana", 387123123)
maria = Contacto("Maria", 387321321)
damian = Contacto("Damian", 387321321)

# Tarea 2: Instalar las dos aplicaciones en el celular.
moto99.instalar_aplicacion(replit)
moto99.instalar_aplicacion(vscode)


# Tarea 3: Agregar los dos contactos al celular.
moto99.agregar_contacto(ivana)
moto99.agregar_contacto(maria)

# Tarea 4: Mostrar todas las aplicaciones instaladas en el celular.
moto99.mostrar_aplicaciones()

# Tarea 5: Mostrar todos los contactos guardados en el celular.
moto99.mostrar_contactos()

# Tarea 6: Actualizar la versión de una de las aplicaciones instaladas en el celular.
moto99.actualizar_aplicacion(vim, "1.0.0")

# Tarea 7: Eliminar uno de los contactos del celular.
moto99.eliminar_contacto(damian)

# Tarea 8: Eliminar aplicaciones con versiones anteriores a la 1.5.0
moto99.limpiar_aplicaciones("1.5.0")
moto99.mostrar_aplicaciones()


