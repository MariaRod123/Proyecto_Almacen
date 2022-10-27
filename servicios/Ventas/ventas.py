from datos.modelos import Venta as modelos_Venta

def listar_ventas():
    return modelos_Venta.listar_ventas()


def obtener_venta(num_venta):
    venta = modelos_Venta.buscar_venta(num_venta)
    if len(venta) == 0:
        raise Exception("No hay venta para mostrar")
    return venta[0]

def buscar_venta_tipo(tipo_venta):
    venta = modelos_Venta.buscar_venta_tipo(tipo_venta)
    if len(venta) == 0:
        raise Exception("No se encuentra el tipo de venta")
    return venta[0]


def crear_nueva_venta(fecha_venta, cantidad, subtotal, total, tipo_venta, id_producto, id_cliente):
    modelos_Venta.agregar_venta(fecha_venta, cantidad, subtotal, total, tipo_venta, id_producto, id_cliente)

def actualizar_venta(num_venta, datos_venta):
    modelos_Venta.modificar_venta(num_venta, datos_venta)

def borrar_venta(num_venta):
    modelos_Venta.borrar_venta(num_venta)

