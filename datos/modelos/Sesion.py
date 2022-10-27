from datos.base_datos import BaseDatos


# Crear sesión

def crear_sesion(dt_string, id_usuario):
    crear_sesion_sql = f"""
        INSERT INTO SESION (FECHA_HORA, ID_USUARIO)
        VALUES ('{dt_string}', '{id_usuario}')
           """
    bd = BaseDatos()
    return bd.ejecutar_sql(crear_sesion_sql, True)


# Mostrar datos de sesión

def obtener_sesion(id_sesion):
    obtener_sesion_sql = f"""
        SELECT ID_SESION, FECHA_HORA, ID_USUARIO FROM SESION WHERE ID_SESION = '{id_sesion}'
    """
    bd = BaseDatos()
    return [{"id_sesion": registro[0],
             "fecha_hora": registro[1],
             "id_usuario": registro[2]}
            for registro in bd.ejecutar_sql(obtener_sesion_sql)]
