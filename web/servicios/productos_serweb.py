import requests

from web.servicios import rest_api


def crear_producto(nomb_producto, precio_costo, utilidad, medida, precio_venta, cantidad_stock, vencim_prod,
                   categoria):
    body = {"nomb_producto": nomb_producto,
            "precio_costo": precio_costo,
            "utilidad": utilidad,
            "medida": medida,
            "precio_venta": precio_venta,
            "cantidad_stock": cantidad_stock,
            "vencim_prod": vencim_prod,
            "categoria": categoria}
    respuesta = requests.post(f'{rest_api.API_URL}/productos', json=body)
    return respuesta.status_code == 200


def obtener_todos_productos():
    respuesta = requests.get(f'{rest_api.API_URL}/productos')
    return respuesta.json()


def buscar_producto_general(busqueda):
    respuesta = requests.get(f'{rest_api.API_URL}/productos?busqueda={busqueda}')
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        return []


def modifica_producto(id_producto, nomb_producto, precio_costo, utilidad, medida, precio_venta, cantidad_stock,
                      vencim_prod, categoria):
    body = {"nomb_producto": nomb_producto,
            "precio_costo": precio_costo,
            "utilidad": utilidad,
            "medida": medida,
            "precio_venta": precio_venta,
            "cantidad_stock": cantidad_stock,
            "vencim_producto": vencim_prod,
            "categoria": categoria}
    respuesta = requests.put(f'{rest_api.API_URL}/productos/{id_producto}', json=body)
    return respuesta.status_code == 200


def eliminar_producto(id_producto):
    respuesta = requests.delete(f'{rest_api.API_URL}/productos/{id_producto}')
    return respuesta.status_code == 200
