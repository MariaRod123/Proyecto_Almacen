from flask import Flask, request, redirect, url_for
from flask import render_template
from web.servicios import autenticacion_serweb
from web.servicios import clientes_serweb
from web.servicios import compras_serweb
from web.servicios import productos_serweb
from web.servicios import proveedores_serweb
from web.servicios import ventas_serweb
from web.servicios import saldos_serweb

app = Flask(__name__)


# Cargar página principal
@app.route('/')
def index():
    return redirect(url_for('login'))


# Formulario login
@app.route('/index', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print(request.form)
        if not autenticacion_serweb.validar_credenciales(request.form['nomb_usuario'], request.form['rol'],
                                                         request.form['contrasenia']):
            error = 'Los datos ingresados no son correctos'
        else:
            return redirect(url_for('inicio'))
    return render_template('index.html', error=error)


# Página de inicio para usuario logueado
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


############################### USUARIOS ##############################################################

# Ver todos los usuarios
@app.route('/usuarios', methods=['GET'])
def ver_usuarios():
    usuarios = autenticacion_serweb.obtener_usuarios()
    return render_template('usuarios.html', usuarios=usuarios)


# Ingresar un nuevo usuario desde el formulario de registro
@app.route('/usuarios', methods=['POST'])
def registro_usuario():
    error = None
    if request.method == 'POST':
        if not autenticacion_serweb.crear_usuario(request.form['nomb_usuario'], request.form['email'],
                                                  request.form['rol'],
                                                  request.form['contrasenia']):
            error = 'No se puede crear usuario'
        else:
            return redirect(url_for('ver_usuarios'))  # va el nombre de la funcion que lista todos los usuarios
    return render_template('usuarios.html', error=error)


# Modificar datos de usuario
@app.route('/usuarios/<int:id_usuario>/modificar', methods=['POST'])
def actualizacion_datos_usuario(id_usuario):
    error = None
    if request.method == 'POST':
        if not autenticacion_serweb.modifica_usuario(id_usuario, request.form['nomb_usuario'],
                                                     request.form['email'],
                                                     request.form['rol'], request.form['contrasenia']):
            error = 'Usuario no se ha podido modificar'
        else:
            return redirect(url_for('ver_usuarios'))
    return render_template('usuarios.html', error=error)


# Eliminar usuario
@app.route('/usuarios/<int:id_usuario>', methods=['GET', 'POST'])
def eliminacion_usuario(id_usuario):
    borrar_usuario = autenticacion_serweb.eliminar_usuario(id_usuario)
    if borrar_usuario is True:
        return redirect(url_for('ver_usuarios'))
    return render_template('usuarios.html')


# Salir de la aplicación
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


###################################### CLIENTES #################################################

# Clientes - lista de todos los clientes

@app.route('/clientes', methods=['GET'])
def ver_todos_clientes():
    clientes = clientes_serweb.obtener_todos_clientes()
    return render_template('clientes.html', clientes=clientes)


# Ingresar nuevo cliente
@app.route('/clientes', methods=['POST'])
def ingresar_nuevo_cliente():
    error = None
    if request.method == 'POST':
        if not clientes_serweb.crear_cliente(request.form['nomb_cliente'], request.form['apellido_cliente'],
                                             request.form['dire_cliente'], request.form['tel_cliente'],
                                             request.form['tope_credito']):
            error = 'No se puede ingresar el cliente'
        else:
            return redirect(url_for('ver_todos_clientes'))
    return render_template('clientes.html', error=error)


# Modificar cliente
@app.route('/clientes/<int:id_cliente>/modificar', methods=['POST'])
def modifica_datos_clientes(id_cliente):
    error = None
    if request.method == 'POST':
        if not clientes_serweb.modificar_cliente(id_cliente, request.form['nomb_cliente'],
                                                 request.form['apellido_cliente'],
                                                 request.form['dire_cliente'], request.form['tel_cliente'],
                                                 request.form['tope_credito']):
            error = 'Los datos del cliente no se han podido modificar'
        else:
            return redirect(url_for('ver_todos_clientes'))
    return render_template('clientes.html', error=error)


# Eliminar cliente
@app.route('/clientes/<int:id_cliente>', methods=['GET', 'POST'])
def eliminacion_cliente(id_cliente):
    borrar_cliente = clientes_serweb.eliminar_cliente(id_cliente)
    if borrar_cliente is True:
        return redirect(url_for('ver_todos_clientes'))
    return render_template('clientes.html')


################################# PRODUCTOS #############################################################

# Productos - ingresar un nuevo producto
@app.route('/productos', methods=['POST'])
def ingresar_producto_nuevo():
    error = None
    if request.method == 'POST':
        if not productos_serweb.crear_producto(request.form['nomb_producto'], request.form['precio_costo'],
                                               request.form['utilidad'], request.form['medida'],
                                               request.form['precio_venta'], request.form['cantidad_stock'],
                                               request.form['vencim_prod'], request.form['categoria']):
            error = 'No se puede ingresar el producto'
        else:
            return redirect(url_for('listar_productos'))
    return render_template('productos.html', error=error)


# Productos- Mostrar el listado de todos los productos que hay en tabla producto de la bd
@app.route('/productos', methods=['GET'])
def listar_productos():
    productos = productos_serweb.obtener_todos_productos()
    return render_template('productos.html', productos=productos)


# Productos - Borrar un producto específico

@app.route('/productos/<int:id_producto>', methods=['GET', 'POST'])
def elimina_producto(id_producto):
    borrar_producto = productos_serweb.eliminar_producto(id_producto)
    if borrar_producto is True:
        return redirect(url_for('listar_productos'))
    return render_template('productos.html')


# Actualizar datos del producto
@app.route('/productos/<int:id_producto>/modificar', methods=['POST'])
def modificar_datos_producto(id_producto):
    error = None
    if request.method == 'POST':
        if not productos_serweb.modifica_producto(id_producto, request.form['nomb_producto'],
                                                  request.form['precio_costo'],
                                                  request.form['utilidad'], request.form['medida'],
                                                  request.form['precio_venta'], request.form['cantidad_stock'],
                                                  request.form['vencim_prod'], request.form['categoria']):
            error = 'No se puede modificar el producto'
        else:
            return redirect(url_for('listar_productos'))
    return render_template('productos.html', error=error)


# Buscar producto general
@app.route('/productos/buscar', methods=['POST'])
def busqueda_producto():
    productos = productos_serweb.buscar_producto_general(request.form['buscar'])
    return render_template('productos.html', productos=productos)


################################# PROVEEDORES ##############################################

# Proveedores - listado de todos los proveedores

@app.route('/proveedores', methods=['GET'])
def ver_proveedores():
    proveedores = proveedores_serweb.obtener_todos_proveedores()
    return render_template('proveedores.html', proveedores=proveedores)


# Ingresar nuevo proveedor
@app.route('/proveedores', methods=['POST'])
def ingresar_nuevo_proveedor():
    error = None
    if request.method == 'POST':
        if not proveedores_serweb.crear_proveedor(request.form['nomb_prov'], request.form['dire_prov'],
                                                  request.form['tel_prov']):
            error = 'No se puede ingresar el proveedor'
        else:
            return redirect(url_for('ver_proveedores'))
    return render_template('proveedores.html', error=error)


# Modificar proveedor
@app.route('/proveedores/<int:id_prov>/modificar', methods=['POST'])
def modifica_datos_proveedor(id_prov):
    error = None
    if request.method == 'POST':
        if not proveedores_serweb.modifica_proveedor(id_prov, request.form['nomb_prov'], request.form['dire_prov'],
                                                     request.form['tel_prov']):
            error = 'Los datos del proveedor no se han podido modificar'
        else:
            return redirect(url_for('ver_proveedores'))
    return render_template('proveedores.html', error=error)


# Eliminar proveedor
@app.route('/proveedores/<int:id_prov>', methods=['GET', 'POST'])
def eliminar_prov(id_prov):
    borrar_proveedor = proveedores_serweb.eliminar_proveedor(id_prov)
    if borrar_proveedor is True:
        return redirect(url_for('ver_proveedores'))
    return render_template('proveedores.html')


################################# COMPRAS #################################################

# Compras - Ver todas las compras
@app.route('/compras', methods=['GET'])
def ver_todas_compras():
    compras = compras_serweb.obtener_todas_compras()
    return render_template('compras.html', compras=compras)


# Compras - Ingresar compra
@app.route('/compras', methods=['POST'])
def ingresar_nueva_compra():
    error = None
    if request.method == 'POST':
        if not compras_serweb.crear_compra(request.form['num_fact'], request.form['fecha_compra'],
                                           request.form['nomb_prov'], request.form['nomb_producto'],
                                           request.form['cant_prod'], request.form['precio_costo'],
                                           request.form['subtotal_compra'], request.form['total_compra'],
                                           request.form['tipo_compra']):
            error = 'No se puede ingresar compra'
        else:
            return redirect(url_for('ver_todas_compras'))
    return render_template('compras.html', error=error)


# Modificar compra
@app.route('/compras/<int:id_compra>/modificar', methods=['POST'])
def modificacion_datos_compra(id_compra):
    error = None
    if request.method == 'POST':
        if not compras_serweb.modificar_compra(id_compra, request.form['num_fact'], request.form['fecha_compra'],
                                               request.form['nomb_prov'], request.form['nomb_producto'],
                                               request.form['cant_prod'], request.form['precio_costo'],
                                               request.form['subtotal_compra'], request.form['total_compra'],
                                               request.form['tipo_compra']):
            error = 'No se ha podido modificar datos de compra'
        else:
            return redirect(url_for('ver_todas_compras'))
    return render_template('compras.html', error=error)


# Eliminar compra
@app.route('/compras/<int:id_compra>', methods=['GET', 'POST'])
def eliminacion_compra(id_compra):
    borrar_compra = compras_serweb.eliminar_compra(id_compra)
    if borrar_compra is True:
        return redirect(url_for('ver_todas_compras'))
    return render_template('compras.html')


################################# VENTAS ##################################

# Ventas - Mostrar todas las ventas
@app.route('/ventas', methods=['GET'])
def ver_ventas_todas():
    ventas = ventas_serweb.obtener_todas_ventas()
    return render_template('ventas.html', ventas=ventas)


# Ventas - Ingresar venta
@app.route('/ventas', methods=['POST'])
def ingresar_nueva_venta():
    error = None
    mensaje = 'Venta ingresada correctamente'
    if request.method == 'POST':
        if not ventas_serweb.ingresar_nueva_venta(request.form['fecha_venta'], request.form['cantidad'],
                                                  request.form['subtotal'], request.form['total'],
                                                  request.form['tipo_venta'], request.form['id_producto'],
                                                  request.form['id_cliente']):
            error = 'No se puede ingresar venta'
        else:
            return redirect(url_for('ver_ventas_todas'))
    return render_template('ventas.html', error=error, mensaje=mensaje)


# Eliminar venta
@app.route('/ventas/<int:num_venta>', methods=['GET', 'POST'])
def eliminacion_venta(num_venta):
    borrar_venta = ventas_serweb.eliminar_venta(num_venta)
    mensaje = 'Venta eliminada correctamente'
    if borrar_venta is True:
        return redirect(url_for('ver_ventas_todas'))
    return render_template('ventas.html', mensaje=mensaje)


# Modificar ventas

@app.route('/ventas/<int:num_venta>/modificar', methods=['POST'])
def actualizacion_venta(num_venta):
    error = None
    if request.method == 'POST':
        if not ventas_serweb.modificacion_venta(num_venta, request.form['fecha_venta'], request.form['cantidad'],
                                                request.form['subtotal'], request.form['total'],
                                                request.form['tipo_venta'], request.form['id_producto'],
                                                request.form['id_cliente']):
            error = 'No se puede modificar venta'
        else:
            return redirect(url_for('ver_ventas_todas'))
    return render_template('ventas.html', error=error)


################################## SALDOS ################################################

# Saldos - Mostrar saldos clientes
@app.route('/saldos', methods=['GET'])
def ver_saldos_clientes():
    saldos = saldos_serweb.obtener_saldos_clientes()
    return render_template('saldos.html', saldos=saldos)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5002)
