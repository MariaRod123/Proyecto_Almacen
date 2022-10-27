import requests

from web.servicios import rest_api


def crear_compra(num_fact, fecha_compra, nomb_prov, nomb_producto, cant_prod, precio_costo, subtotal_compra,
                 total_compra, tipo_compra):
    body = {"num_fact": num_fact,
            "fecha_compra": fecha_compra,
            "nomb_prov": nomb_prov,
            "nomb_producto": nomb_producto,
            "cant_prod": cant_prod,
            "precio_costo": precio_costo,
            "subtotal_compra": subtotal_compra,
            "total_compra": total_compra,
            "tipo_compra": tipo_compra}
    respuesta = requests.post(f'{rest_api.API_URL}/compras', json=body)
    return respuesta.status_code == 200


def obtener_todas_compras():
    respuesta = requests.get(f'{rest_api.API_URL}/compras')
    return respuesta.json()


def modificar_compra(id_compra, num_fact, fecha_compra, nomb_prov, nomb_producto, cant_prod, precio_costo,
                     subtotal_compra, total_compra, tipo_compra):
    body = {"num_fact": num_fact,
            "fecha_compra": fecha_compra,
            "nomb_prov": nomb_prov,
            "nomb_producto": nomb_producto,
            "cant_prod": cant_prod,
            "precio_costo": precio_costo,
            "subtotal_compra": subtotal_compra,
            "total_compra": total_compra,
            "tipo_compra": tipo_compra}
    respuesta = requests.put(f'{rest_api.API_URL}/compras/{id_compra}', json=body)
    return respuesta.status_code == 200


def eliminar_compra(id_compra):
    respuesta = requests.delete(f'{rest_api.API_URL}/compras/{id_compra}')
    return respuesta.status_code == 200
