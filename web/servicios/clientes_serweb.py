import requests

from web.servicios import rest_api


def crear_cliente(nomb_cliente, apellido_cliente, dire_cliente, tel_cliente, tope_credito):
    body = {"nomb_cliente": nomb_cliente,
            "apellido_cliente": apellido_cliente,
            "dire_cliente": dire_cliente,
            "tel_cliente": tel_cliente,
            "tope_credito": tope_credito}
    respuesta = requests.post(f'{rest_api.API_URL}/clientes', json=body)
    return respuesta.status_code == 200


def obtener_todos_clientes():
    respuesta = requests.get(f'{rest_api.API_URL}/clientes')
    return respuesta.json()


def modificar_cliente(id_cliente, nomb_cliente, apellido_cliente, dire_cliente, tel_cliente, tope_credito):
    body = {"nomb_cliente": nomb_cliente,
            "apellido_cliente": apellido_cliente,
            "dire_cliente": dire_cliente,
            "tel_cliente": tel_cliente,
            "tope_credito": tope_credito}
    respuesta = requests.put(f'{rest_api.API_URL}/clientes/{id_cliente}/modificar', json=body)
    return respuesta.status_code == 200


def eliminar_cliente(id_cliente):
    respuesta = requests.delete(f'{rest_api.API_URL}/clientes/{id_cliente}')
    return respuesta.status_code == 200
