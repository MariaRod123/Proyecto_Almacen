from datos.modelos import Usuario as modelos_Usuario



def existe_usuario(nomb_usuario):
    usuarios = modelos_Usuario.buscar_usuario_nomb(nomb_usuario)
    return not len(usuarios) == 0

def existe_id_usuario(id_usuario):
    usuarios = modelos_Usuario.buscar_usuario_id(id_usuario)
    return not len(usuarios) == 0

def obtener_usuarios():
    return modelos_Usuario.listar_usuarios()


def obtener_usuario(id_usuario):
    usuario = modelos_Usuario.buscar_usuario_id(id_usuario)
    if len(usuario) == 0:
        raise Exception("El usuario no existe")
    return usuario[0]


def buscar_usuario(nomb_usuario):
    usuario = modelos_Usuario.buscar_usuario_nomb(nomb_usuario)
    if len(usuario) == 0:
        raise Exception("El usuario no existe")
    return usuario[0]


def crear_usuario(nomb_usuario, email, rol, contrasenia):
    if not existe_usuario(nomb_usuario):
        return modelos_Usuario.crear_usuario(nomb_usuario, email, rol, contrasenia)
    else:
        raise Exception("Ya existe este usuario")


def actualizar_usuario(id_usuario, datos_usuario):
    modelos_Usuario.modificar_usuario(id_usuario, datos_usuario)



def borrar_usuario(id_usuario):
    modelos_Usuario.borrar_usuario(id_usuario)


def login(nomb_usuario, rol, contrasenia):
    print(nomb_usuario, rol, contrasenia)  # ESTA LINEA SE AGREGÓ Y ANDA EL LOGIN
    if not existe_usuario(nomb_usuario):
        return "Nombre de usuario no encontrado"
    if existe_usuario(nomb_usuario):
        print(modelos_Usuario.buscar_datos_login(nomb_usuario))  # ESTA LINEA SE AGREGÓ
        return modelos_Usuario.buscar_datos_login(nomb_usuario)[0]






