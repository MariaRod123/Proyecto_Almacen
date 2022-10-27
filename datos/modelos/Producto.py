from datos.base_datos import BaseDatos


# Alta de producto

def ingresar_producto(nomb_producto, precio_costo, utilidad, medida, precio_venta, cantidad_stock, vencim_prod,
                      categoria):
    ingresar_producto_sql = f"""
        INSERT INTO PRODUCTO (NOMB_PRODUCTO, 
                                PRECIO_COSTO, 
                                UTILIDAD, MEDIDA, 
                                PRECIO_VENTA, 
                                CANTIDAD_STOCK, 
                                VENCIM_PROD, 
                                CATEGORIA)
                                VALUES ('{nomb_producto}','{precio_costo}','{utilidad}', 
                                '{medida}', '{precio_venta}','{cantidad_stock}',
                                '{vencim_prod}','{categoria}') 
    """
    bd = BaseDatos()
    bd.ejecutar_sql(ingresar_producto_sql)


# Borrar Producto

def borrar_producto(id_producto):
    borrar_producto_sql = f"""
        DELETE FROM PRODUCTO WHERE ID_PRODUCTO = '{id_producto}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(borrar_producto_sql)


# Modificar datos de un producto

def modificar_producto(id_producto, datos_producto):
    modificar_producto_sql = f"""
        UPDATE PRODUCTO SET NOMB_PRODUCTO='{datos_producto['nomb_producto']}', 
                           PRECIO_COSTO='{datos_producto['precio_costo']}',
                           UTILIDAD='{datos_producto['utilidad']}',
                           MEDIDA='{datos_producto['medida']}',
                           PRECIO_VENTA='{datos_producto['precio_venta']}',
                           CANTIDAD_STOCK='{datos_producto['cantidad_stock']}',
                           VENCIM_PROD='{datos_producto['vencim_prod']}',
                           CATEGORIA='{datos_producto['categoria']}' 
                           WHERE ID_PRODUCTO ='{id_producto}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(modificar_producto_sql)


# Listar productos

def listar_productos():
    listar_productos_sql = f"""
        SELECT ID_PRODUCTO,
                NOMB_PRODUCTO, 
                PRECIO_COSTO, 
                UTILIDAD, 
                MEDIDA, 
                PRECIO_VENTA, 
                CANTIDAD_STOCK, 
                VENCIM_PROD, 
                CATEGORIA
                FROM PRODUCTO
    """
    bd = BaseDatos()
    return [{"id_producto": registro[0],
             "nomb_producto": registro[1],
             "precio_costo": registro[2],
             "utilidad": registro[3],
             "medida": registro[4],
             "precio_venta": registro[5],
             "cantidad_stock": registro[6],
             "vencim_prod": registro[7],
             "categoria": registro[8]
             } for registro in bd.ejecutar_sql(listar_productos_sql)]


# Buscar productos (general): nombre, ID y categoria

def buscar_producto(busqueda):
    buscar_producto_sql = f"""
        SELECT ID_PRODUCTO,
                NOMB_PRODUCTO, 
                PRECIO_COSTO, 
                UTILIDAD, 
                MEDIDA, 
                PRECIO_VENTA, 
                CANTIDAD_STOCK, 
                VENCIM_PROD, 
                CATEGORIA 
                FROM PRODUCTO 
                WHERE NOMB_PRODUCTO LIKE'%{busqueda}%'
                OR CATEGORIA LIKE '%{busqueda}%'
    """
    if busqueda.isnumeric():
        buscar_producto_sql += f""" OR ID_PRODUCTO = {busqueda}"""

    bd = BaseDatos()
    return [{"id_producto": registro[0],
             "nomb_producto": registro[1],
             "precio_costo": registro[2],
             "utilidad": registro[3],
             "medida": registro[4],
             "precio_venta": registro[5],
             "cantidad_stock": registro[6],
             "vencim_prod": registro[7],
             "categoria": registro[8]
             } for registro in bd.ejecutar_sql(buscar_producto_sql)]


# Buscar productos por nombre

def busca_prod(nomb_producto):
    buscar_producto_sql = f"""
        SELECT ID_PRODUCTO,
                NOMB_PRODUCTO, 
                PRECIO_COSTO, 
                UTILIDAD, 
                MEDIDA, 
                PRECIO_VENTA, 
                CANTIDAD_STOCK, 
                VENCIM_PROD, 
                CATEGORIA 
                FROM PRODUCTO 
                WHERE NOMB_PRODUCTO='{nomb_producto}'
    """
    bd = BaseDatos()
    return [{"id_producto": registro[0],
             "nomb_producto": registro[1],
             "precio_costo": registro[2],
             "utilidad": registro[3],
             "medida": registro[4],
             "precio_venta": registro[5],
             "cantidad_stock": registro[6],
             "vencim_prod": registro[7],
             "categoria": registro[8]
             } for registro in bd.ejecutar_sql(buscar_producto_sql)]


# buscar producto por id

def buscar_producto_id(id_producto):
    buscar_producto_id_sql = f"""
        SELECT ID_PRODUCTO,
                NOMB_PRODUCTO, 
                PRECIO_COSTO, 
                UTILIDAD, 
                MEDIDA, 
                PRECIO_VENTA, 
                CANTIDAD_STOCK, 
                VENCIM_PROD, 
                CATEGORIA
                FROM PRODUCTO 
                WHERE ID_PRODUCTO='{id_producto}'
    """
    bd = BaseDatos()
    return [{"id_producto": registro[0],
             "nomb_producto": registro[1],
             "precio_costo": registro[2],
             "utilidad": registro[3],
             "medida": registro[4],
             "precio_venta": registro[5],
             "cantidad_stock": registro[6],
             "vencim_prod": registro[7],
             "categoria": registro[8]
             } for registro in bd.ejecutar_sql(buscar_producto_id_sql)]


def obtener_productos_por_categoria(categoria):
    obtener_categoria_sql = f"""
            SELECT ID_PRODUCTO,
                NOMB_PRODUCTO, 
                PRECIO_COSTO, 
                UTILIDAD, 
                MEDIDA, 
                PRECIO_VENTA, 
                CANTIDAD_STOCK, 
                VENCIM_PROD,
                CATEGORIA
                FROM PRODUCTO 
                WHERE CATEGORIA='{categoria}'
        """
    bd = BaseDatos()
    return [{"id_producto": registro[0],
             "nomb_producto": registro[1],
             "precio_costo": registro[2],
             "utilidad": registro[3],
             "medida": registro[4],
             "precio_venta": registro[5],
             "cantidad_stock": registro[6],
             "vencim_prod": registro[7],
             "categoria": registro[8]
             } for registro in bd.ejecutar_sql(obtener_categoria_sql)]
