from datos.modelos import Proveedor as modelos_Proveedor

def obtener_proveedores():
    return modelos_Proveedor.listar_proveedores()


def obtener_prov(nomb_prov):
    proveedor = modelos_Proveedor.buscar_proveedor(nomb_prov)
    if len(proveedor) == 0:
        raise Exception("No hay proveedor con este nombre")
    return proveedor[0]

def buscar_prov(id_prov):
    proveedor = modelos_Proveedor.buscar_proveedor_id(id_prov)
    if len(proveedor) == 0:
        raise Exception("No existe proveedor")
    return proveedor[0]

def existe_proveedor(nomb_prov):
    proveedor = modelos_Proveedor.buscar_proveedor(nomb_prov)
    return not len(proveedor) == 0

def crear_nuevo_proveedor(nomb_prov, dire_prov, tel_prov):
    if not existe_proveedor(nomb_prov):
        modelos_Proveedor.agregar_proveedor(nomb_prov, dire_prov,tel_prov)
    else:
        raise Exception("Ya existe proveedor con ese nombre")


def modificacion_proveedor(id_prov, datos_prov):
    modelos_Proveedor.modificar_proveedor(id_prov, datos_prov)

def borrar_proveedor(id_prov):
    modelos_Proveedor.borrar_proveedor(id_prov)

