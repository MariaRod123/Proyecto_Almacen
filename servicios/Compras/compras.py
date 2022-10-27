from datos.modelos import Compra as modelos_Compra


def listar_compras():
    return modelos_Compra.listar_compras()


def ingresar_compra(num_fact, fecha_compra, nomb_prov, nomb_producto, cant_prod, precio_costo, subtotal_compra,
                    total_compra, tipo_compra):
    modelos_Compra.ingresar_compra(num_fact, fecha_compra, nomb_prov, nomb_producto, cant_prod, precio_costo,
                                   subtotal_compra, total_compra, tipo_compra)


def modificar_compra(id_compras, datos_compras):
    modelos_Compra.modificar_compra(id_compras, datos_compras)


def borrar_compra(id_compra):
    modelos_Compra.borrar_compra(id_compra)
