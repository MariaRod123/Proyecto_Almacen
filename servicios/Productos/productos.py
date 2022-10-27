from datos.modelos import Producto as modelos_Producto


def obtener_productos():
    return modelos_Producto.listar_productos()


def obtener_producto_gral(busqueda):
    producto = modelos_Producto.buscar_producto(busqueda)
    return producto


def crear_nuevo_producto(nomb_producto, precio_costo, utilidad, medida, precio_venta, cantidad_stock, vencim_prod,
                         categoria):
    modelos_Producto.ingresar_producto(nomb_producto, precio_costo, utilidad, medida, precio_venta, cantidad_stock,
                                       vencim_prod,
                                       categoria)


def modificacion_producto(id_producto, datos_producto):
    modelos_Producto.modificar_producto(id_producto, datos_producto)


def borrar_producto(id_producto):
    modelos_Producto.borrar_producto(id_producto)
