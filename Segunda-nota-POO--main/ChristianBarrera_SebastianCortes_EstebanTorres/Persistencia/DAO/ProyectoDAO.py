from Persistencia.DAO.Conexion import obtener_conexion
from Dominio.DTO.Proyecto import Proyecto

class ProyectoDAO:

    def agregar(self, proyecto):
        try:
            con = obtener_conexion()
            sql = "INSERT INTO proyectos (codigo, nombre, presupuesto, id_departamento) VALUES (%s, %s, %s, %s)"
            with con.cursor() as c:
                c.execute(sql, (proyecto.codigo, proyecto.nombre, proyecto.presupuesto, proyecto.id_departamento))
            con.commit()
            return True
        except Exception as e:
            print("Error al agregar proyecto:", e)
            return False

    def mostrar(self):
        con = obtener_conexion()
        sql = "SELECT * FROM proyectos"
        with con.cursor() as c:
            c.execute(sql)
            return c.fetchall()

    def buscar_codigo(self, codigo):
        con = obtener_conexion()
        sql = "SELECT * FROM proyectos WHERE codigo=%s"
        with con.cursor() as c:
            c.execute(sql, (codigo,))
            return c.fetchone()

    def buscar_nombre(self, nombre):
        con = obtener_conexion()
        sql = "SELECT * FROM proyectos WHERE nombre LIKE %s"
        with con.cursor() as c:
            c.execute(sql, ("%" + nombre + "%",))
            return c.fetchall()

    def modificar(self, proyecto):
        try:
            con = obtener_conexion()
            sql = "UPDATE proyectos SET nombre=%s, presupuesto=%s, id_departamento=%s WHERE codigo=%s"
            with con.cursor() as c:
                c.execute(sql, (proyecto.nombre, proyecto.presupuesto, proyecto.id_departamento, proyecto.codigo))
            con.commit()
            return True
        except Exception as e:
            print("Error al modificar proyecto:", e)
            return False

    def eliminar(self, proyecto):
        try:
            con = obtener_conexion()
            sql = "DELETE FROM proyectos WHERE codigo=%s"
            with con.cursor() as c:
                c.execute(sql, (proyecto.codigo,))
            con.commit()
            return True
        except Exception as e:
            print("Error al eliminar proyecto:", e)
            return False
