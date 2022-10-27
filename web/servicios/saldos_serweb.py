import requests

from web.servicios import rest_api

def obtener_saldos_clientes():
    respuesta = requests.get(f'{rest_api.API_URL}/saldos')
    return respuesta.json()
