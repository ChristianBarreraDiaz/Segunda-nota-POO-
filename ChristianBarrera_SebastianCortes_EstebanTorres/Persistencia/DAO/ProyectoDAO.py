from Persistencia.DAO.Conexion import obtener_conexion
from Dominio.DTO.Proyecto import Proyecto

class ProyectoDAO:
    def agregar(self, proyecto):
        conn = obtener_conexion()
        sql = "INSERT INTO proyectos (codigo, nombre, presupuesto, id_departamento) VALUES (%s, %s, %s, %s)"
        with conn.cursor() as cursor:
            cursor.execute(sql, (proyecto.codigo, proyecto.nombre, proyecto.presupuesto, proyecto.id_departamento))
        conn.commit()
        conn.close()

    def modificar(self, proyecto):
        conn = obtener_conexion()
        sql = "UPDATE proyectos SET nombre=%s, presupuesto=%s, id_departamento=%s WHERE codigo=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (proyecto.nombre, proyecto.presupuesto, proyecto.id_departamento, proyecto.codigo))
        conn.commit()
        conn.close()

    def eliminar(self, codigo):
        conn = obtener_conexion()
        sql = "DELETE FROM proyectos WHERE codigo=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (codigo,))
        conn.commit()
        conn.close()

    def mostrar_todos(self):
        conn = obtener_conexion()
        sql = "SELECT * FROM proyectos"
        with conn.cursor() as cursor:
            cursor.execute(sql)
            datos = cursor.fetchall()
        conn.close()
        return datos

    def mostrar_parcial(self, nombre_parcial):
        conn = obtener_conexion()
        sql = "SELECT * FROM proyectos WHERE nombre LIKE %s"
        with conn.cursor() as cursor:
            cursor.execute(sql, ("%" + nombre_parcial + "%",))
            datos = cursor.fetchall()
        conn.close()
        return datos

    def mostrar_uno(self, codigo):
        conn = obtener_conexion()
        sql = "SELECT * FROM proyectos WHERE codigo=%s"
        with conn.cursor() as cursor:
            cursor.execute(sql, (codigo,))
            dato = cursor.fetchone()
        conn.close()
        return dato
