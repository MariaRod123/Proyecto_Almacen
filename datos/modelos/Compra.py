from datos.base_datos import BaseDatos


# Ingresar Compra
def ingresar_compra(num_fact, fecha_compra, nomb_prov, nomb_producto, cant_prod, precio_costo, subtotal_compra,
                    total_compra, tipo_compra):
    ingresar_compra_sql = f"""
        INSERT INTO COMPRA (NUM_FACT, 
                            FECHA_COMPRA, 
                            NOMB_PROV, 
                            NOMB_PRODUCTO, 
                            CANT_PROD, 
                            PRECIO_COSTO, 
                            SUBTOTAL_COMPRA, 
                            TOTAL_COMPRA, 
                            TIPO_COMPRA) 
        VALUES('{num_fact}',
                '{fecha_compra}',
                '{nomb_prov}', 
                '{nomb_producto}',
                '{cant_prod}', 
                '{precio_costo}', 
                '{subtotal_compra}',
                '{total_compra}',
                '{tipo_compra}') 
        
    """
    bd = BaseDatos()
    bd.ejecutar_sql(ingresar_compra_sql)


# Borrar Compra
def borrar_compra(id_compra):
    borrar_compra_sql = f"""
        DELETE FROM COMPRA WHERE ID_COMPRA = '{id_compra}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(borrar_compra_sql)


# Modificar Compra
def modificar_compra(id_compra, datos_compra):
    modificar_compra_sql = f"""
        UPDATE COMPRA SET NUM_FACT='{datos_compra['num_fact']}', 
                        FECHA_COMPRA='{datos_compra['fecha_compra']}',
                        NOMB_PROV='{datos_compra['nomb_prov']}',
                        NOMB_PRODUCTO='{datos_compra['nomb_producto']}',
                        CANT_PROD='{datos_compra['cant_prod']}',
                        PRECIO_COSTO='{datos_compra['precio_costo']}',
                        SUBTOTAL_COMPRA='{datos_compra['subtotal_compra']}',
                        TOTAL_COMPRA='{datos_compra['total_compra']}' 
                        WHERE ID_COMPRA ='{id_compra}'

    """
    bd = BaseDatos()
    bd.ejecutar_sql(modificar_compra_sql)


# listar Compras
def listar_compras():
    listar_compras_sql = f""" 
        SELECT ID_COMPRA, 
                NUM_FACT, 
                FECHA_COMPRA, 
                NOMB_PROV, 
                NOMB_PRODUCTO, 
                CANT_PROD, 
                PRECIO_COSTO, 
                SUBTOTAL_COMPRA, 
                TOTAL_COMPRA, 
                TIPO_COMPRA 
                FROM COMPRA 
    """
    bd = BaseDatos()
    return [{"id_compra": registro[0],
             "num_fact": registro[1],
             "fecha_compra": registro[2],
             "nomb_prov": registro[3],
             "nomb_producto": registro[4],
             "cant_prod": registro[5],
             "precio_costo": registro[6],
             "subtotal_compra": registro[7],
             "total_compra": registro[8],
             "tipo_compra": registro[9]
             } for registro in bd.ejecutar_sql(listar_compras_sql)]


# Buscar compra por tipo compra
def buscar_compra_tipo(tipo_compra):
    buscar_compra_tipo_sql = f""" 
        SELECT ID_COMPRA, 
                NUM_FACT, 
                FECHA_COMPRA, 
                NOMB_PROV, 
                NOMB_PRODUCTO, 
                CANT_PROD, 
                PRECIO_COSTO, 
                SUBTOTAL_COMPRA, 
                TOTAL_COMPRA, 
                TIPO_COMPRA 
                FROM COMPRA WHERE TIPO_COMPRA='{tipo_compra}'
            """
    bd = BaseDatos()
    return [{"id_compra": registro[0],
             "num_fact": registro[1],
             "fecha_compra": registro[2],
             "nomb_prov": registro[3],
             "nomb_producto": registro[4],
             "cant_prod": registro[5],
             "precio_costo": registro[6],
             "subtotal_compra": registro[7],
             "total_compra": registro[8],
             "tipo_compra": registro[9]
             } for registro in bd.ejecutar_sql(buscar_compra_tipo_sql)]
