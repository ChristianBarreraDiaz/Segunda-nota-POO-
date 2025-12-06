from Dominio.DTO.Empleado import Empleado

class ReglasEmpleado:
    def __init__(self):
        self.empleados = []

    def crear_objeto(self, rut, nombre, apellido, email="", id_departamento=None):
        return Empleado(rut, nombre, apellido, email, id_departamento)

    def agregar(self, empleado):
        self.empleados.append(empleado)
        return True

    def mostrar_todos(self):
        return self.empleados

    def buscar_por_rut(self, rut):
        for e in self.empleados:
            if e.rut == rut:
                return e
        return None

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for e in self.empleados:
            if nombre.lower() in e.nombre.lower() or nombre.lower() in e.apellido.lower():
                encontrados.append(e)
        return encontrados

    def modificar(self, empleado_modificado):
        for i, e in enumerate(self.empleados):
            if e.rut == empleado_modificado.rut:
                self.empleados[i] = empleado_modificado
                return True
        return False

    def eliminar(self, empleado):
        for e in self.empleados:
            if e.rut == empleado.rut:
                self.empleados.remove(e)
                return True
        return False
