from Persistencia.DAO.Conexion import obtener_conexion
from Dominio.DTO.Empleado import Empleado

class EmpleadoDAO:
    def agregar(self, empleado):
        conn = obtener_conexion()
        sql = "INSERT INTO empleados (rut, nombre, apellido, email, id_departamento) VALUES (%s, %s, %s, %s, %s)"
        with conn.cursor() as cursor:
            cursor.execute(sql, (empleado.rut, empleado.nombre, empleado.apellido, empleado.email, empleado.id_departamento))
        conn.commit()
        conn.close()

    def modificar(self, empleado):
        conn = obtener_conexion()
        sql = "UPDATE empleados SET nombre=%s, apellido=%s, email=%s, id_departamento=%s WHERE rut=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (empleado.nombre, empleado.apellido, empleado.email, empleado.id_departamento, empleado.rut))
        conn.commit()
        conn.close()

    def eliminar(self, rut):
        conn = obtener_conexion()
        sql = "DELETE FROM empleados WHERE rut=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (rut,))
        conn.commit()
        conn.close()

    def mostrar_todos(self):
        conn = obtener_conexion()
        sql = "SELECT * FROM empleados"
        with conn.cursor() as cursor:
            cursor.execute(sql)
            datos = cursor.fetchall()
        conn.close()
        return datos

    def mostrar_parcial(self, nombre_parcial):
        conn = obtener_conexion()
        sql = "SELECT * FROM empleados WHERE nombre LIKE %s OR apellido LIKE %s"
        like = "%" + nombre_parcial + "%"
        with conn.cursor() as cursor:
            cursor.execute(sql, (like, like))
            datos = cursor.fetchall()
        conn.close()
        return datos

    def mostrar_uno(self, rut):
        conn = obtener_conexion()
        sql = "SELECT * FROM empleados WHERE rut=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (rut,))
            dato = cursor.fetchone()
        conn.close()
        return dato
