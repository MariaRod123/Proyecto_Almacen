from datos.base_datos import BaseDatos


# Ingresar nuevo cliente

def crear_cliente(nomb_cliente, apellido_cliente, dire_cliente, tel_cliente, tope_credito):
    crear_cliente_sql = f"""
        INSERT INTO CLIENTE (NOMB_CLIENTE, APELLIDO_CLIENTE, DIRE_CLIENTE, TEL_CLIENTE, TOPE_CREDITO)
        VALUES ('{nomb_cliente}', '{apellido_cliente}', '{dire_cliente}', '{tel_cliente}', '{tope_credito}')
    """
    bd = BaseDatos()
    bd.ejecutar_sql(crear_cliente_sql)


# Borrar Cliente

def borrar_cliente(id_cliente):
    borrar_cliente_sql = f"""
        DELETE FROM CLIENTE WHERE ID_CLIENTE = '{id_cliente}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(borrar_cliente_sql)


# Modificar cliente

def modificar_cliente(id_cliente, datos_cliente):
    modificar_cliente_sql = f"""
        UPDATE CLIENTE SET NOMB_CLIENTE='{datos_cliente['nomb_cliente']}', 
                           APELLIDO_CLIENTE='{datos_cliente['apellido_cliente']}',                         
                           DIRE_CLIENTE='{datos_cliente['dire_cliente']}',
                           TEL_CLIENTE='{datos_cliente['tel_cliente']}',
                           TOPE_CREDITO='{datos_cliente['tope_credito']}'
                           WHERE ID_CLIENTE ='{id_cliente}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(modificar_cliente_sql)


# Listar clientes

def listar_clientes():
    listar_clientes_sql = f"""
        SELECT ID_CLIENTE, NOMB_CLIENTE, APELLIDO_CLIENTE, DIRE_CLIENTE, TEL_CLIENTE, TOPE_CREDITO FROM CLIENTE
               
    """
    bd = BaseDatos()
    return [{"id_cliente": registro[0],
             "nomb_cliente": registro[1],
             "apellido_cliente": registro[2],
             "dire_cliente": registro[3],
             "tel_cliente": registro[4],
             "tope_credito": registro[5]
             } for registro in bd.ejecutar_sql(listar_clientes_sql)]


# Buscar cliente por nombre

def buscar_cliente(nomb_cliente):
    buscar_cliente_sql = f"""
        SELECT ID_CLIENTE, NOMB_CLIENTE, APELLIDO_CLIENTE, DIRE_CLIENTE, TEL_CLIENTE, TOPE_CREDITO 
        FROM CLIENTE WHERE NOMB_CLIENTE='{nomb_cliente}'
    """
    bd = BaseDatos()
    return [{"id_cliente": registro[0],
             "nomb_cliente": registro[1],
             "apellido_cliente": registro[2],
             "dire_cliente": registro[3],
             "tel_cliente": registro[4],
             "tope_credito": registro[5]
             } for registro in bd.ejecutar_sql(buscar_cliente_sql)]


# buscar cliente por id

def buscar_id_cliente(id_cliente):
    buscar_id_cliente_sql = f"""
        SELECT ID_CLIENTE, NOMB_CLIENTE, APELLIDO_CLIENTE, DIRE_CLIENTE, TEL_CLIENTE, TOPE_CREDITO 
        FROM CLIENTE WHERE ID_CLIENTE='{id_cliente}'
    """
    bd = BaseDatos()
    return [{"id_cliente": registro[0],
             "nomb_cliente": registro[1],
             "apellido_cliente": registro[2],
             "dire_cliente": registro[3],
             "tel_cliente": registro[4],
             "tope_credito": registro[5]
             } for registro in bd.ejecutar_sql(buscar_id_cliente_sql)]


# buscar cliente por nombre y apellido

'''def obtener_cliente_nombre_apellido(nomb_cliente, apellido_cliente):
    obtener_cliente_sql = f"""
            SELECT ID_CLIENTE, NOMB_CLIENTE, APELLIDO_CLIENTE, DIRE_CLIENTE, TEL_CLIENTE, TOPE_CREDITO
            FROM CLIENTE 
            WHERE NOMB_CLIENTE='{nomb_cliente}' AND APELLIDO_CLIENTE='{apellido_cliente}'
        """
    bd = BaseDatos()
    return [{"id_cliente": registro[0],
             "nomb_cliente": registro[1],
             "apellido_cliente": registro[2],
             "dire_cliente": registro[3],
             "tel_cliente": registro[4],
             "tope_credito": registro[5]
             } for registro in bd.ejecutar_sql(obtener_cliente_sql)]'''
