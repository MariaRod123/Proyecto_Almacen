from datos.base_datos import BaseDatos


# Alta de Usuario

def crear_usuario(nomb_usuario, email, rol, contrasenia):
    crear_usuario_sql = f"""
        INSERT INTO USUARIO (NOMB_USUARIO, EMAIL, ROL, CONTRASENIA)
        VALUES ('{nomb_usuario}','{email}','{rol}', '{contrasenia}')
    """
    bd = BaseDatos()
    bd.ejecutar_sql(crear_usuario_sql)


# Borrar Usuario

def borrar_usuario(id_usuario):
    borrar_usuario_sql = f"""
        DELETE FROM USUARIO WHERE ID_USUARIO = '{id_usuario}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(borrar_usuario_sql)


# Modificar datos usuario

def modificar_usuario(id_usuario, datos_usuario):
    modificar_usuario_sql = f"""
        UPDATE USUARIO SET NOMB_USUARIO='{datos_usuario['nomb_usuario']}', 
                           EMAIL='{datos_usuario['email']}',
                           ROL='{datos_usuario['rol']}',
                           CONTRASENIA='{datos_usuario['contrasenia']}'
                           WHERE ID_USUARIO ='{id_usuario}'
    """
    bd = BaseDatos()
    bd.ejecutar_sql(modificar_usuario_sql)


# Listar usuarios

def listar_usuarios():
    listar_usuarios_sql = f"""
        SELECT ID_USUARIO, NOMB_USUARIO, EMAIL, ROL FROM USUARIO
    """
    bd = BaseDatos()
    return [{"id_usuario": registro[0],
             "nomb_usuario": registro[1],
             "email": registro[2],
             "rol": registro[3]
             }
            for registro in bd.ejecutar_sql(listar_usuarios_sql)]


# Buscar usuario por nombre

def buscar_usuario_nomb(nomb_usuario):
    buscar_usuario_nomb_sql = f"""
        SELECT ID_USUARIO, NOMB_USUARIO, EMAIL, ROL, CONTRASENIA FROM USUARIO WHERE NOMB_USUARIO='{nomb_usuario}'
    """
    bd = BaseDatos()
    return [{"id_usuario": registro[0],
             "nomb_usuario": registro[1],
             "email": registro[2],
             "rol": registro[3],
             "contrasenia": registro[4]
             }
            for registro in bd.ejecutar_sql(buscar_usuario_nomb_sql)]


# buscar usuario por id

def buscar_usuario_id(id_usuario):
    buscar_usuario_id_sql = f"""
        SELECT ID_USUARIO, NOMB_USUARIO, EMAIL, ROL, CONTRASENIA FROM USUARIO WHERE ID_USUARIO='{id_usuario}'
    """
    bd = BaseDatos()
    return [{"id_usuario": registro[0],
             "nomb_usuario": registro[1],
             "email": registro[2],
             "rol": registro[3],
             "contrasenia": registro[4]
             } for registro in bd.ejecutar_sql(buscar_usuario_id_sql)]


# Buscar datos usuario  para login

def buscar_datos_login(nomb_usuario):
    buscar_datos_login_sql = f"""
            SELECT NOMB_USUARIO, ROL, CONTRASENIA
            FROM USUARIO 
            WHERE NOMB_USUARIO='{nomb_usuario}'
                        
        """
    bd = BaseDatos()
    return [{"nomb_usuario": registro[0],
             "rol": registro[1],
             "contrasenia": registro[2]}
            for registro in bd.ejecutar_sql(buscar_datos_login_sql)]

