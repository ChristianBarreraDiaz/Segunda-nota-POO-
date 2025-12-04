from Persistencia.DAO.Conexion import obtener_conexion
from Dominio.DTO.Departamento import Departamento

class DepartamentoDAO:
    def agregar(self, departamento):
        conn = obtener_conexion()
        sql = "INSERT INTO departamentos (codigo, nombre, descripcion) VALUES (%s, %s, %s)"
        with conn.cursor() as cursor:
            cursor.execute(sql, (departamento.codigo, departamento.nombre, departamento.descripcion))
        conn.commit()
        conn.close()

    def modificar(self, departamento):
        conn = obtener_conexion()
        sql = "UPDATE departamentos SET nombre=%s, descripcion=%s WHERE codigo=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (departamento.nombre, departamento.descripcion, departamento.codigo))
        conn.commit()
        conn.close()

    def eliminar(self, codigo):
        conn = obtener_conexion()
        sql = "DELETE FROM departamentos WHERE codigo=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (codigo,))
        conn.commit()
        conn.close()

    def mostrar_todos(self):
        conn = obtener_conexion()
        sql = "SELECT * FROM departamentos"
        with conn.cursor() as cursor:
            cursor.execute(sql)
            datos = cursor.fetchall()
        conn.close()
        return datos

    def mostrar_parcial(self, nombre_parcial):
        conn = obtener_conexion()
        sql = "SELECT * FROM departamentos WHERE nombre LIKE %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, ("%" + nombre_parcial + "%",))
            datos = cursor.fetchall()
        conn.close()
        return datos

    def mostrar_uno(self, codigo):
        conn = obtener_conexion()
        sql = "SELECT * FROM departamentos WHERE codigo=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (codigo,))
            dato = cursor.fetchone()
        conn.close()
        return dato
