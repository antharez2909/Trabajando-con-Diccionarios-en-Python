# Crear un Diccionario :
# Se crea un diccionario llamado informacion_personal que almacena información sobre una persona con las claves: "nombre", "edad", "ciudad" y "profesion".
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Quito",
    "profesion": "Ingeniero"
}

# Acceder y Modificar Valores:
# Se accede al valor de la clave "ciudad" y se cambia de "Quito" a "Guayaquil".
# También se modifica la profesión de "Ingeniero" a "Arquitecto".

informacion_personal["ciudad"] = "Guayaquil"  # Modificar ciudad
informacion_personal["profesion"] = "Arquitecto"  # Cambiar profesión

# Verificar Existencia de Claves:
# Se verifica si la clave "telefono" no está en el diccionario. Si no está, se añade con un número ficticio.

if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0999999999"  # Agregar teléfono

# Eliminar una Clave:
#Se comprueba si la clave "edad" existe en el diccionario. Si existe, se elimina del diccionario.
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Eliminar edad

# Imprimir el Diccionario Final:
#Finalmente, se imprime el diccionario actualizado, mostrando solo las claves y valores restantes.
print(informacion_personal)
