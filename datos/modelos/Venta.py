from datos.base_datos import BaseDatos

# Ingresar nueva venta

def agregar_venta(fecha_venta, cantidad, subtotal, total, tipo_venta, id_producto, id_cliente):
    crear_venta_sql = f"""
        INSERT INTO VENTA (FECHA_VENTA, CANTIDAD, SUBTOTAL, TOTAL, TIPO_VENTA,  ID_PRODUCTO, ID_CLIENTE)
        VALUES ('{fecha_venta}', '{cantidad}','{subtotal}','{total}', '{tipo_venta}', '{id_producto}', '{id_cliente}')
    """
    bd = BaseDatos()
    bd.ejecutar_sql(crear_venta_sql)


# Borrar venta

def borrar_venta(num_venta):
    borrar_venta_sql = f"""
        DELETE FROM VENTA WHERE NUM_VENTA = '{num_venta}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(borrar_venta_sql)


# Modificar venta

def modificar_venta(num_venta, datos_venta):
    modificar_venta_sql = f"""
        UPDATE VENTA SET FECHA_VENTA='{datos_venta['fecha_venta']}',                         
                        CANTIDAD='{datos_venta['cantidad']}',
                        SUBTOTAL='{datos_venta['subtotal']}',
                        TOTAL='{datos_venta['total']}',
                        TIPO_VENTA='{datos_venta['tipo_venta']}',
                        ID_PRODUCTO='{datos_venta['id_producto']},
                        ID_CLIENTE='{datos_venta['id_cliente']}
                        WHERE NUM_VENTA ='{num_venta}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(modificar_venta_sql)


# Listar ventas

def listar_ventas():
    listar_ventas_sql = f"""
        SELECT VENTA.NUM_VENTA, VENTA.FECHA_VENTA, VENTA.CANTIDAD, VENTA.SUBTOTAL, VENTA.TOTAL, VENTA.TIPO_VENTA, PRODUCTO.NOMB_PRODUCTO, CLIENTE.NOMB_CLIENTE 
        FROM VENTA
            INNER JOIN PRODUCTO ON VENTA.ID_PRODUCTO = PRODUCTO.ID_PRODUCTO 
            INNER JOIN CLIENTE ON VENTA.ID_CLIENTE = CLIENTE.ID_CLIENTE
    """
    bd = BaseDatos()
    return [{"num_venta": registro[0],
             "fecha_venta": registro[1],
             "cantidad": registro[2],
             "subtotal": registro[3],
             "total": registro[4],
             "tipo_venta": registro[5],
             "nomb_producto": registro[6],
             "nomb_cliente": registro[7]
             } for registro in bd.ejecutar_sql(listar_ventas_sql)]


# Buscar venta por número de venta

def buscar_venta(num_venta):
    buscar_venta_sql = f"""
        
        SELECT NUM_VENTA, FECHA_VENTA, CANTIDAD, SUBTOTAL, TOTAL, TIPO_VENTA, ID_PRODUCTO, ID_CLIENTE FROM VENTA 
        WHERE NUM_VENTA='{num_venta}'
    """
    bd = BaseDatos()
    return [{"num_venta": registro[0],
             "fecha_venta": registro[1],
             "cantidad": registro[2],
             "subtotal": registro[3],
             "total": registro[4],
             "tipo_venta": registro[5],
             "id_producto": registro[6],
             "id_cliente": registro[7]
             } for registro in bd.ejecutar_sql(buscar_venta_sql)]


# Buscar tipo venta

def buscar_venta_tipo(tipo_venta):
    buscar_venta_tipo_sql = f"""
        SELECT NUM_VENTA, FECHA_VENTA, CANTIDAD, SUBTOTAL, TOTAL, TIPO_VENTA, ID_PRODUCTO, ID_CLIENTE FROM VENTA
        WHERE TIPO_VENTA='{tipo_venta}'
    """
    bd = BaseDatos()
    return [{"num_venta": registro[0],
             "fecha_venta": registro[1],
             "cantidad": registro[2],
             "subtotal": registro[3],
             "total": registro[4],
             "tipo_venta": registro[5],
             "id_producto": registro[6],
             "id_cliente": registro[7]
             } for registro in bd.ejecutar_sql(buscar_venta_tipo_sql)]
