# Matriz con datos de clientes
clientes = [
    ["C001", 250, 10],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 200, 9],
    ["C005", 50, 6]
]

# Función para clasificar compromiso
def clasificar_compromiso(duracion, clics):

    if duracion > 180 and clics > 8:
        return "Alto"

    elif duracion < 60 or clics < 3:
        return "Bajo"

    else:
        return "Medio"


# Mostrar informe
print("INFORME DE CLASIFICACIÓN")
print("----------------------------")

for cliente in clientes:

    id_cliente = cliente[0]
    duracion = cliente[1]
    clics = cliente[2]

    clasificacion = clasificar_compromiso(
        duracion,
        clics
    )

    print("Cliente:", id_cliente)
    print("Clasificación:", clasificacion)
    print("----------------------------")
