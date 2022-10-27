import requests
from web.servicios import rest_api


def validar_credenciales(nomb_usuario, rol, contrasenia):
    body = {"nomb_usuario": nomb_usuario,
            "rol": rol,
            "contrasenia": contrasenia}
    respuesta = requests.post(f'{rest_api.API_URL}/login', json=body)
    return respuesta.status_code == 200


def crear_usuario(nomb_usuario, email, rol, contrasenia):
    body = {"nomb_usuario": nomb_usuario,
            "email": email,
            "rol": rol,
            "contrasenia": contrasenia}
    respuesta = requests.post(f'{rest_api.API_URL}/usuarios', json=body)
    return respuesta.status_code == 200


def obtener_usuarios():
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios')
    return respuesta.json()

def buscar_nombre_usuario(nomb_usuario):
    respuesta = requests.get(f'{rest_api.API_URL}/usuarios/{nomb_usuario}')
    return respuesta.json()

def modifica_usuario(id_usuario, nomb_usuario, email, rol, contrasenia):
    body = {"nomb_usuario": nomb_usuario,
            "email": email,
            "rol": rol,
            "contrasenia": contrasenia}
    respuesta = requests.put(f'{rest_api.API_URL}/usuarios/{id_usuario}/modificar', json=body)
    return respuesta.status_code == 200


def eliminar_usuario(id_usuario):
    respuesta = requests.delete(f'{rest_api.API_URL}/usuarios/{id_usuario}')
    return respuesta.status_code == 200
