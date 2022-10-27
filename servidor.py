from flask import Flask, request, jsonify
from flask import render_template
from servicios.Autenticacion import autenticacion
from servicios.Clientes import clientes
from servicios.Proveedores import proveedores
from servicios.Productos import productos
from servicios.Compras import compras
from servicios.Ventas import ventas
from servicios.Saldos import saldos_clientes

app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('index.html'), 200


##################### Usuarios ############################################

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.get_json()
    if 'nomb_usuario' not in datos_usuario or datos_usuario['nomb_usuario'] == '':
        return 'El nombre de usuario es requerido', 400
    if 'email' not in datos_usuario or datos_usuario['email'] == '':
        return 'Email es requerido', 400
    if 'rol' not in datos_usuario or datos_usuario['rol'] == '':
        return ' Rol es obligatorio', 400
    if 'contrasenia' not in datos_usuario or datos_usuario['contrasenia'] == '':
        return 'La contraseña es requerida', 400
    autenticacion.crear_usuario(datos_usuario['nomb_usuario'], datos_usuario['email'], datos_usuario['rol'],
                                datos_usuario['contrasenia'])
    return 'Usuario ingresado exitosamente', 200


@app.route('/usuarios/<int:id_usuario>/modificar', methods=['PUT'])
def modificacion_usuario(id_usuario):
    datos_usuario = request.get_json()
    if 'nomb_usuario' not in datos_usuario or datos_usuario['nomb_usuario'] == '':
        return 'El nombre de usuario es requerido', 400
    if 'email' not in datos_usuario or datos_usuario['email'] == '':
        return 'Email es requerido', 400
    if 'rol' not in datos_usuario or datos_usuario['rol'] == '':
        return ' Rol es obligatorio', 400
    if 'contrasenia' not in datos_usuario:
        return 'La contraseña es requerida', 400
    autenticacion.actualizar_usuario(id_usuario, datos_usuario)
    return 'Datos de usuario actualizados', 200


@app.route('/usuarios', methods=['GET'])
def obtener_usuarios_todos():
    return jsonify(autenticacion.obtener_usuarios())


@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obtener_usuario_id(id_usuario):
    try:
        usuario = autenticacion.obtener_usuario(id_usuario)
        return jsonify(usuario), 200
    except Exception:
        return 'Usuario no encontrado', 404


@app.route('/usuarios/<string:nomb_usuario>', methods=['GET'])
def buscar_nombre_usuario(nomb_usuario):
    try:
        usuario = autenticacion.buscar_usuario(nomb_usuario)
        return jsonify(usuario), 200
    except Exception:
        return 'Usuario no encontrado', 404


@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def borrar_usuario(id_usuario):
    autenticacion.borrar_usuario(id_usuario)
    return "El usuario ha sido eliminado", 200


@app.route('/login', methods=['POST'])
def login():
    datos_usuario = request.get_json()
    if 'nomb_usuario' not in datos_usuario or datos_usuario['nomb_usuario'] == '':
        return 'El nombre de usuario es requerido', 400
    if 'rol' not in datos_usuario or datos_usuario['rol'] == '':
        return 'Rol es requerido', 400
    if 'contrasenia' not in datos_usuario or datos_usuario['contrasenia'] == '':
        return 'La contraseña es requerido', 400
    if autenticacion.login(datos_usuario['nomb_usuario'], datos_usuario['rol'], datos_usuario['contrasenia']):
        return "Usuario logueado", 200
    return " Datos incorrectos", 404


######################### Clientes ##########################################

@app.route('/clientes', methods=['POST'])
def crear_cliente_nuevo():
    datos_cliente = request.get_json()
    if 'nomb_cliente' not in datos_cliente or datos_cliente['nomb_cliente'] == '':
        return 'El nombre de cliente es requerido', 400
    if 'apellido_cliente' not in datos_cliente or datos_cliente['apellido_cliente'] == '':
        return 'El apellido es requerido', 400
    if 'dire_cliente' not in datos_cliente or datos_cliente['dire_cliente'] == '':
        return ' La dirección del cliente es obligatoria', 400
    if 'tel_cliente' not in datos_cliente or datos_cliente['tel_cliente'] == '':
        return 'Teléfono  del cliente es requerido', 400
    if 'tope_credito' not in datos_cliente or datos_cliente['tope_credito'] == '':
        return 'El tope de crédito es requerido', 400
    clientes.crear_cliente_nuevo(datos_cliente['nomb_cliente'], datos_cliente['apellido_cliente'],
                                 datos_cliente['dire_cliente'], datos_cliente['tel_cliente'],
                                 datos_cliente['tope_credito'])
    return 'Cliente ingresado exitosamente', 200


@app.route('/clientes/<int:id_cliente>/modificar', methods=['PUT'])
def modificar_dato_cliente(id_cliente):
    datos_cliente = request.get_json()
    if 'nomb_cliente' not in datos_cliente or datos_cliente['nomb_cliente'] == '':
        return 'El nombre de cliente es requerido', 400
    if 'apellido_cliente' not in datos_cliente or datos_cliente['apellido_cliente'] == '':
        return 'El apellido es requerido', 400
    if 'dire_cliente' not in datos_cliente or datos_cliente['dire_cliente'] == '':
        return ' La dirección es obligatoria', 400
    if 'tel_cliente' not in datos_cliente or datos_cliente['tel_cliente'] == '':
        return 'Teléfono del cliente es requerido', 400
    if 'tope_credito' not in datos_cliente or datos_cliente['tope_credito'] == '':
        return 'El tope de crédito del cliente es requerido', 400
    clientes.modificar_cliente(id_cliente, datos_cliente)
    return ' Datos de cliente actualizados ', 200


@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    return jsonify(clientes.obtener_clientes())


@app.route('/clientes/<string:nomb_cliente>/buscar', methods=['GET'])
def obtener_cliente_nombre(nomb_cliente):
    try:
        cliente = clientes.obtener_nombre_cliente(nomb_cliente)
        return jsonify(cliente), 200
    except Exception:
        return 'No se encuentra el cliente', 404


@app.route('/clientes/<int:id_cliente>/buscar', methods=['GET'])
def obtener_cliente(id_cliente):
    try:
        cliente = clientes.obtener_id_cliente(id_cliente)
        return jsonify(cliente), 200
    except Exception:
        return 'No se encuentra cliente', 404


@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def borrar_cliente(id_cliente):
    clientes.borrar_cliente(id_cliente)
    return "Cliente eliminado con éxito", 200


############## Proveedores ##################################################

@app.route('/proveedores', methods=['POST'])
def ingresar_proveedor():
    datos_prov = request.get_json()
    if 'nomb_prov' not in datos_prov or datos_prov['nomb_prov'] == '':
        return 'El nombre del proveedor es requerido', 400
    if 'dire_prov' not in datos_prov or datos_prov['dire_prov'] == '':
        return ' La dirección es obligatoria', 400
    if 'tel_prov' not in datos_prov or datos_prov['tel_prov'] == '':
        return 'Teléfono es requerido', 400
    proveedores.crear_nuevo_proveedor(datos_prov['nomb_prov'], datos_prov['dire_prov'], datos_prov['tel_prov'])
    return 'Proveedor ingresado exitosamente', 200


@app.route('/proveedores/<int:id_prov>/modificar', methods=['PUT'])
def modificar_datos_prov(id_prov):
    datos_prov = request.get_json()
    if 'nomb_prov' not in datos_prov or datos_prov['nomb_prov'] == '':
        return 'El nombre del proveedor es requerido', 400
    if 'dire_prov' not in datos_prov or datos_prov['dire_prov'] == '':
        return ' La dirección es obligatoria', 400
    if 'tel_prov' not in datos_prov or datos_prov['tel_prov'] == '':
        return 'Teléfono es requerido', 400
    proveedores.modificacion_proveedor(id_prov, datos_prov)
    return 'Datos del proveedor actualizados', 200


@app.route('/proveedores', methods=['GET'])
def obtener_lista_proveedores():
    return jsonify(proveedores.obtener_proveedores())


@app.route('/proveedores/<string:nomb_prov>/buscar', methods=['GET'])
def obtener_datos_proveedor(nomb_prov):
    try:
        proveedor = proveedores.obtener_prov(nomb_prov)
        return jsonify(proveedor), 200
    except Exception:
        return 'No se encuentra proveedor', 404


@app.route('/proveedores/<int:id_prov>/buscar', methods=['GET'])
def buscar_proveedor(id_prov):
    try:
        proveedor = proveedores.buscar_prov(id_prov)
        return jsonify(proveedor), 200
    except Exception:
        return 'No se encuentra proveedor', 404


@app.route('/proveedores/<int:id_prov>', methods=['DELETE'])
def eliminar_proveedor(id_prov):
    proveedores.borrar_proveedor(id_prov)
    return "Proveedor eliminado con éxito", 200


################### Productos ####################################################

@app.route('/productos', methods=['POST'])
def ingresar_producto():
    datos_producto = request.get_json()
    if 'nomb_producto' not in datos_producto or datos_producto['nomb_producto'] == '':
        return 'Nombre de producto es requerido', 400
    if 'precio_costo' not in datos_producto or datos_producto['precio_costo'] == '':
        return 'El costo es requerido', 400
    if 'utilidad' not in datos_producto or datos_producto['utilidad'] == '':
        return 'Utilidad es requerida', 400
    if 'medida' not in datos_producto or datos_producto['medida'] == '':
        return 'Unidad de medida es requerida', 400
    if 'precio_venta' not in datos_producto or datos_producto['precio_venta'] == '':
        return 'El precio de venta es requerido', 400
    if 'cantidad_stock' not in datos_producto or datos_producto['cantidad_stock'] == '':
        return 'Cantidad  es requerida', 400
    if 'vencim_prod' not in datos_producto or datos_producto['vencim_prod'] == '':
        return 'Fecha de vencimiento del producto es requerido', 400
    if 'categoria' not in datos_producto or datos_producto['categoria'] == '':
        return 'Categoria de  producto es requerido', 400

    productos.crear_nuevo_producto(datos_producto['nomb_producto'], datos_producto['precio_costo'],
                                   datos_producto['utilidad'], datos_producto['medida'], datos_producto['precio_venta'],
                                   datos_producto['cantidad_stock'], datos_producto['vencim_prod'],
                                   datos_producto['categoria'])
    return 'Producto ingresado exitosamente', 200


@app.route('/productos/<int:id_producto>', methods=['PUT'])
def actualizacion_producto(id_producto):
    datos_producto = request.get_json()
    if 'nomb_producto' not in datos_producto or datos_producto['nomb_producto'] == '':
        return 'Nombre de producto es requerido', 400
    if 'precio_costo' not in datos_producto or datos_producto['precio_costo'] == '':
        return 'El costo es requerido', 400
    if 'utilidad' not in datos_producto or datos_producto['utilidad'] == '':
        return 'Utilidad es requerida', 400
    if 'medida' not in datos_producto or datos_producto['medida'] == '':
        return 'Unidad de medida es requerida', 400
    if 'precio_venta' not in datos_producto or datos_producto['precio_venta'] == '':
        return 'El precio de venta es requerido', 400
    if 'cantidad_stock' not in datos_producto or datos_producto['cantidad_stock'] == '':
        return 'Cantidad  es requerida', 400
    if 'vencim_prod' not in datos_producto or datos_producto['vencim_prod'] == '':
        return 'Fecha de vencimiento del producto es requerido', 400
    if 'categoria' not in datos_producto or datos_producto['categoria'] == '':
        return 'Categoria de  producto es requerido', 400
    productos.modificacion_producto(id_producto, datos_producto)
    return 'Los datos del producto han sido modificados', 200


@app.route('/productos', methods=['GET'])
def listar_todos_productos():
    if 'busqueda' in request.args:
        producto = productos.obtener_producto_gral(request.args.get('busqueda'))
        return jsonify(producto), 200
    else:
        return jsonify(productos.obtener_productos())


@app.route('/productos/<string:busqueda>/buscar', methods=['GET'])
def buscar_producto_gral(busqueda):
    try:
        producto = productos.obtener_producto_gral(busqueda)
        return jsonify(producto), 200
    except Exception:
        return 'No existe el producto', 404


@app.route('/productos/<int:id_producto>', methods=['DELETE'])
def borrar_producto(id_producto):
    productos.borrar_producto(id_producto)
    return "Producto eliminado", 200


################ Compras #####################################

@app.route('/compras', methods=['POST'])
def ingresar_compra():
    datos_compra = request.get_json()
    if 'num_fact' not in datos_compra or datos_compra['num_fact'] == '':
        return 'El número de factura es requerido', 400
    if 'fecha_compra' not in datos_compra or datos_compra['fecha_compra'] == '':
        return 'La fecha de compra es requerida', 400
    if 'nomb_prov' not in datos_compra or datos_compra['nomb_prov'] == '':
        return 'Nombre de proveedor es requerido', 400
    if 'nomb_producto' not in datos_compra or datos_compra['nomb_producto'] == '':
        return 'El nombre de producto es requerido', 400
    if 'cant_prod' not in datos_compra or datos_compra['cant_prod'] == '':
        return 'La cantidad de producto es requerido', 400
    if 'precio_costo' not in datos_compra or datos_compra['precio_costo'] == '':
        return 'El costo de producto es requerido', 400
    if 'subtotal_compra' not in datos_compra or datos_compra['subtotal_compra'] == '':
        return 'Subtotal es requerido', 400
    if 'total_compra' not in datos_compra or datos_compra['total_compra'] == '':
        return 'Total es requerido', 400
    if 'tipo_compra' not in datos_compra or datos_compra['tipo_compra'] == '':
        return 'Tipo de compra es requerida', 400

    compras.ingresar_compra(datos_compra['num_fact'], datos_compra['fecha_compra'], datos_compra['nomb_prov'],
                            datos_compra['nomb_producto'], datos_compra['cant_prod'], datos_compra['precio_costo'],
                            datos_compra['subtotal_compra'], datos_compra['total_compra'], datos_compra['tipo_compra'])
    return 'Compra ingresada correctamente', 200


@app.route('/compras/<int:id_compra>', methods=['PUT'])
def modificar_compra(id_compra):
    datos_compra = request.get_json()
    if 'num_fact' not in datos_compra or datos_compra['num_fact'] == '':
        return 'El número de factura es requerido', 400
    if 'fecha_compra' not in datos_compra or datos_compra['fecha_compra'] == '':
        return 'La fecha de compra es requerida', 400
    if 'nomb_prov' not in datos_compra or datos_compra['nomb_prov'] == '':
        return 'Nombre de proveedor es requerido', 400
    if 'nomb_producto' not in datos_compra or datos_compra['nomb_producto'] == '':
        return 'El nombre de producto es requerido', 400
    if 'cant_prod' not in datos_compra or datos_compra['cant_prod'] == '':
        return 'La cantidad de producto es requerido', 400
    if 'precio_costo' not in datos_compra or datos_compra['precio_costo'] == '':
        return 'El costo de producto es requerido', 400
    if 'subtotal_compra' not in datos_compra or datos_compra['subtotal_compra'] == '':
        return 'Subtotal es requerido', 400
    if 'total_compra' not in datos_compra or datos_compra['total_compra'] == '':
        return 'Total es requerido', 400
    if 'tipo_compra' not in datos_compra or datos_compra['tipo_compra'] == '':
        return 'Tipo de compra es requerida', 400
    compras.modificar_compra(id_compra, datos_compra)
    return 'Datos de compra modificados correctamente', 200


@app.route('/compras', methods=['GET'])
def listar_compras_todas():
    return jsonify(compras.listar_compras())


@app.route('/compras/<int:id_compra>', methods=['DELETE'])
def borrar_compra(id_compra):
    compras.borrar_compra(id_compra)
    return "La compra ha sido eliminada", 200


##################### Ventas #########################################################

@app.route('/ventas', methods=['POST'])
def ingresar_venta():
    datos_venta = request.get_json()

    if 'fecha_venta' not in datos_venta or datos_venta['fecha_venta'] == '':
        return 'Fecha de venta es requerida', 400
    if 'cantidad' not in datos_venta or datos_venta['cantidad'] == '':
        return 'Cantidad es requerida', 400
    if 'subtotal' not in datos_venta or datos_venta['subtotal'] == '':
        return 'Subtotal es requerido', 400
    if 'total' not in datos_venta or datos_venta['total'] == '':
        return 'Total es requerido', 400
    if 'tipo_venta' not in datos_venta or datos_venta['tipo_venta'] == '':
        return 'Tipo de venta es requerido', 400
    if 'id_producto' not in datos_venta or datos_venta['id_producto'] == '':
        return ' id_ producto es requerido', 400
    if 'id_cliente' not in datos_venta or datos_venta['id_cliente'] == '':
        return 'id_cliente es requerido', 400
    ventas.crear_nueva_venta(datos_venta['fecha_venta'], datos_venta['cantidad'], datos_venta['subtotal'],
                             datos_venta['total'], datos_venta['tipo_venta'], datos_venta['id_producto'],
                             datos_venta['id_cliente'])
    return 'Venta ingresada correctamente', 200


@app.route('/ventas/<int:num_venta>/modificar', methods=['PUT'])
def modificar_datos_venta(num_venta):
    datos_venta = request.get_json()
    if 'fecha_venta' not in datos_venta or datos_venta['fecha_venta'] == '':
        return 'Fecha de venta es requerida', 400
    if 'cantidad' not in datos_venta or datos_venta['cantidad'] == '':
        return 'Cantidad de producto es requerido', 400
    if 'subtotal' not in datos_venta or datos_venta['subtotal'] == '':
        return 'Subtotal es requerido', 400
    if 'total' not in datos_venta or datos_venta['total'] == '':
        return 'El total de la venta es requerida', 400
    if 'tipo_venta' not in datos_venta or datos_venta['tipo_venta'] == '':
        return 'Tipo de venta es requerida', 400
    if 'id_producto' not in datos_venta or datos_venta['id_producto'] == '':
        return 'id_producto es requerido', 400
    if 'id_cliente' not in datos_venta or datos_venta['id_cliente'] == '':
        return 'id_cliente es requerido', 400
    ventas.actualizar_venta(num_venta, datos_venta)
    return 'Datos de venta han sido modificados', 200


@app.route('/ventas', methods=['GET'])
def listar_ventas():
    return jsonify(ventas.listar_ventas())


@app.route('/ventas/<int:num_venta>/buscar', methods=['GET'])
def buscar_num_venta(num_venta):
    try:
        venta = ventas.obtener_venta(num_venta)
        return jsonify(venta), 200
    except Exception:
        return 'No se encuentra el número de venta', 404


@app.route('/ventas/<string:tipo_venta>/buscar', methods=['GET'])
def buscar_tipo_venta(tipo_venta):
    try:
        venta = ventas.buscar_venta_tipo(tipo_venta)
        return jsonify(venta), 200
    except Exception:
        return 'No existe el tipo de venta buscado', 404


@app.route('/ventas/<int:num_venta>', methods=['DELETE'])
def borrar_venta(num_venta):
    ventas.borrar_venta(num_venta)
    return "Venta eliminada exitosamente", 200


##########  Saldos ###############
# Saldos
@app.route('/saldos', methods=['GET'])
def mostrar_saldos():
    return jsonify(saldos_clientes.listar_saldos())


if __name__ == '__main__':
    app.debug = True
    app.run(port=5001)
