from Persistencia.DAO.Conexion import obtener_conexion
from Dominio.DTO.Empleado import Empleado

class EmpleadoDAO:

    def agregar(self, empleado):
        try:
            con = obtener_conexion()
            sql = "INSERT INTO empleados (rut, nombre, apellido, email, id_departamento) VALUES (%s, %s, %s, %s, %s)"
            with con.cursor() as c:
                c.execute(sql, (empleado.rut, empleado.nombre, empleado.apellido, empleado.email, empleado.id_departamento))
            con.commit()
            return True
        except Exception as e:
            print("Error al agregar empleado:", e)
            return False

    def mostrar(self):
        con = obtener_conexion()
        sql = "SELECT * FROM empleados"
        with con.cursor() as c:
            c.execute(sql)
            return c.fetchall()

    def buscar_codigo(self, rut):
        con = obtener_conexion()
        sql = "SELECT * FROM empleados WHERE rut=%s"
        with con.cursor() as c:
            c.execute(sql, (rut,))
            return c.fetchone()

    def buscar_nombre(self, nombre):
        con = obtener_conexion()
        sql = "SELECT * FROM empleados WHERE nombre LIKE %s OR apellido LIKE %s"
        like = "%" + nombre + "%"
        with con.cursor() as c:
            c.execute(sql, (like, like))
            return c.fetchall()

    def modificar(self, empleado):
        try:
            con = obtener_conexion()
            sql = "UPDATE empleados SET nombre=%s, apellido=%s, email=%s, id_departamento=%s WHERE rut=%s"
            with con.cursor() as c:
                c.execute(sql, (empleado.nombre, empleado.apellido, empleado.email, empleado.id_departamento, empleado.rut))
            con.commit()
            return True
        except Exception as e:
            print("Error al modificar empleado:", e)
            return False

    def eliminar(self, empleado):
        try:
            con = obtener_conexion()
            sql = "DELETE FROM empleados WHERE rut=%s"
            with con.cursor() as c:
                c.execute(sql, (empleado.rut,))
            con.commit()
            return True
        except Exception as e:
            print("Error al eliminar empleado:", e)
            return False
