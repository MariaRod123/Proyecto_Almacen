import requests

from web.servicios import rest_api


def ingresar_nueva_venta(fecha_venta, cantidad, subtotal, total, tipo_venta, id_producto, id_cliente):
    body = {"fecha_venta": fecha_venta,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "total": total,
            "tipo_venta": tipo_venta,
            "id_producto": id_producto,
            "id_cliente": id_cliente}
    respuesta = requests.post(f'{rest_api.API_URL}/ventas', json=body)
    return respuesta.status_code == 200


def obtener_todas_ventas():
    respuesta = requests.get(f'{rest_api.API_URL}/ventas')
    return respuesta.json()


def modificacion_venta(num_venta, fecha_venta, cantidad, subtotal, total, tipo_venta, id_producto, id_cliente):
    body = {"fecha_venta": fecha_venta,
            "cantidad": cantidad,
            "subtotal": subtotal,
            "total": total,
            "tipo_venta": tipo_venta,
            "id_producto": id_producto,
            "id_cliente": id_cliente}
    respuesta = requests.put(f'{rest_api.API_URL}/ventas/{num_venta}', json=body)
    return respuesta.status_code == 200


def eliminar_venta(num_venta):
    respuesta = requests.delete(f'{rest_api.API_URL}/ventas/{num_venta}')
    return respuesta.status_code == 200
