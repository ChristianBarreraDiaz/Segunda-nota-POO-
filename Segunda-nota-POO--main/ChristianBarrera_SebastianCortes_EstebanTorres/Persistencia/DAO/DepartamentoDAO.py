from Persistencia.DAO.Conexion import obtener_conexion
from Dominio.DTO.Departamento import Departamento

class DepartamentoDAO:

    def agregar(self, departamento):
        try:
            con = obtener_conexion()
            sql = "INSERT INTO departamentos (codigo, nombre, descripcion) VALUES (%s, %s, %s)"
            with con.cursor() as c:
                c.execute(sql, (departamento.codigo, departamento.nombre, departamento.descripcion))
            con.commit()
            return True
        except Exception as e:
            print("Error al agregar departamento:", e)
            return False

    def mostrar(self):
        con = obtener_conexion()
        sql = "SELECT * FROM departamentos"
        with con.cursor() as c:
            c.execute(sql)
            return c.fetchall()

    def buscar_codigo(self, codigo):
        con = obtener_conexion()
        sql = "SELECT * FROM departamentos WHERE codigo=%s"
        with con.cursor() as c:
            c.execute(sql, (codigo,))
            return c.fetchone()

    def buscar_nombre(self, nombre):
        con = obtener_conexion()
        sql = "SELECT * FROM departamentos WHERE nombre LIKE %s"
        with con.cursor() as c:
            c.execute(sql, ("%" + nombre + "%",))
            return c.fetchall()

    def modificar(self, departamento):
        try:
            con = obtener_conexion()
            sql = "UPDATE departamentos SET nombre=%s, descripcion=%s WHERE codigo=%s"
            with con.cursor() as c:
                c.execute(sql, (departamento.nombre, departamento.descripcion, departamento.codigo))
            con.commit()
            return True
        except Exception as e:
            print("Error al modificar departamento:", e)
            return False

    def eliminar(self, departamento):
        try:
            con = obtener_conexion()
            sql = "DELETE FROM departamentos WHERE codigo=%s"
            with con.cursor() as c:
                c.execute(sql, (departamento.codigo,))
            con.commit()
            return True
        except Exception as e:
            print("Error al eliminar departamento:", e)
            return False
