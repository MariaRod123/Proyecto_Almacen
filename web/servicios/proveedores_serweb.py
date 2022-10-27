import requests

from web.servicios import rest_api


def crear_proveedor(nombre, direccion, telefono):
    body = {"nomb_prov": nombre,
            "dire_prov": direccion,
            "tel_prov": telefono}
    respuesta = requests.post(f'{rest_api.API_URL}/proveedores', json=body)
    return respuesta.status_code == 200


def obtener_todos_proveedores():
    respuesta = requests.get(f'{rest_api.API_URL}/proveedores')
    return respuesta.json()


def modifica_proveedor(id_prov, nomb_prov, dire_prov, tel_prov):
    body = {"nomb_prov": nomb_prov,
            "dire_prov": dire_prov,
            "tel_prov": tel_prov}
    respuesta = requests.put(f'{rest_api.API_URL}/proveedores/{id_prov}/modificar', json=body)
    return respuesta.status_code == 200


def eliminar_proveedor(id_prov):
    respuesta = requests.delete(f'{rest_api.API_URL}/proveedores/{id_prov}')
    return respuesta.status_code == 200
