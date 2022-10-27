from datos.modelos import Cliente as modelos_Cliente


def obtener_clientes():
    return modelos_Cliente.listar_clientes()


def obtener_nombre_cliente(nomb_cliente):
    cliente = modelos_Cliente.buscar_cliente(nomb_cliente)
    if len(cliente) == 0:
        raise Exception("El cliente que busca no existe")
    return cliente[0]


def obtener_id_cliente(id_cliente):
    cliente = modelos_Cliente.buscar_id_cliente(id_cliente)
    if len(cliente) == 0:
        raise Exception("El cliente que busca no existe")
    return cliente[0]


def crear_cliente_nuevo(nomb_cliente, apellido_cliente, dire_cliente, tel_cliente, tope_credito):
    modelos_Cliente.crear_cliente(nomb_cliente, apellido_cliente, dire_cliente, tel_cliente, tope_credito)


def modificar_cliente(id_cliente, datos_cliente):
    modelos_Cliente.modificar_cliente(id_cliente, datos_cliente)


def borrar_cliente(id_cliente):
    modelos_Cliente.borrar_cliente(id_cliente)



