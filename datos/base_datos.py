import sqlite3


# Configuraciones de conexion a la BD

class BaseDatos:
    url_bd = 'almacen.db'

    def _crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(BaseDatos.url_bd)
        except Exception as e:
            print(e)

    def _cerrar_conexion(self):
        self.conexion.close()
        self.conexion = None

    def ejecutar_sql(self, sql, retornar_id_sesion=False):
        self._crear_conexion()
        cur = self.conexion.cursor()
        cur.execute(sql)

        filas = cur.fetchall()

        if retornar_id_sesion:
            filas = cur.lastrowid

        self.conexion.commit()
        self._cerrar_conexion()

        return filas
