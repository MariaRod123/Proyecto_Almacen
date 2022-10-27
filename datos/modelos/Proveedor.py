from datos.base_datos import BaseDatos


# Ingresar nuevo proveedor

def agregar_proveedor(nomb_prov, dire_prov, tel_prov):
    crear_proveedor_sql = f"""
        INSERT INTO PROVEEDOR (NOMB_PROV, DIRE_PROV, TEL_PROV)
        VALUES ('{nomb_prov}', '{dire_prov}', '{tel_prov}')
    """
    bd = BaseDatos()
    bd.ejecutar_sql(crear_proveedor_sql)


# Borrar proveedor

def borrar_proveedor(id_prov):
    borrar_proveedor_sql = f"""
        DELETE FROM PROVEEDOR WHERE ID_PROV = '{id_prov}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(borrar_proveedor_sql)


# Modificar proveedor

def modificar_proveedor(id_prov, datos_prov):
    modificar_proveedor_sql = f"""
        UPDATE PROVEEDOR SET NOMB_PROV='{datos_prov['nomb_prov']}', 
                           DIRE_PROV='{datos_prov['dire_prov']}',                         
                           TEL_PROV='{datos_prov['tel_prov']}'
                           WHERE ID_PROV ='{id_prov}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(modificar_proveedor_sql)


# Listar proveedores

def listar_proveedores():
    listar_proveedores_sql = f"""
        SELECT ID_PROV, NOMB_PROV, DIRE_PROV, TEL_PROV FROM PROVEEDOR

    """
    bd = BaseDatos()
    return [{"id_prov": registro[0],
             "nomb_prov": registro[1],
             "dire_prov": registro[2],
             "tel_prov": registro[3]
             } for registro in bd.ejecutar_sql(listar_proveedores_sql)]


# Buscar proveedor por nombre

def buscar_proveedor(nomb_prov):
    buscar_proveedor_sql = f"""
        SELECT ID_PROV, NOMB_PROV, DIRE_PROV, TEL_PROV 
        FROM PROVEEDOR WHERE NOMB_PROV='{nomb_prov}'
    """
    bd = BaseDatos()
    return [{"id_prov": registro[0],
             "nomb_prov": registro[1],
             "dire_prov": registro[2],
             "tel_prov": registro[3]
             } for registro in bd.ejecutar_sql(buscar_proveedor_sql)]


# Buscar proveedor por id

def buscar_proveedor_id(id_prov):
    buscar_proveedor_id_sql = f"""
        SELECT ID_PROV, NOMB_PROV, DIRE_PROV, TEL_PROV 
        FROM PROVEEDOR WHERE ID_PROV='{id_prov}'
    """
    bd = BaseDatos()
    return [{"id_prov": registro[0],
             "nomb_prov": registro[1],
             "dire_prov": registro[2],
             "tel_prov": registro[3]
             } for registro in bd.ejecutar_sql(buscar_proveedor_id_sql)]
