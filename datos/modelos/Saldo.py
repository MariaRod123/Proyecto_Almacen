from datos.base_datos import BaseDatos

# Listar saldos de clientes

def listar_saldos():
    listar_saldos_sql = f"""
        SELECT NOMB_CLIENTE, 
               APELLIDO_CLIENTE, 
               TOPE_CREDITO, 
               SALDO_CLIENTE 
               FROM CLIENTE 
               INNER JOIN SALDO ON CLIENTE.ID_CLIENTE = SALDO.ID_CLIENTE
    """
    bd = BaseDatos()
    return [{"nomb_cliente": registro[0],
             "apellido_cliente": registro[1],
             "tope_credito": registro[2],
             "saldo_cliente": registro[3]
             } for registro in bd.ejecutar_sql(listar_saldos_sql)]
