from Dominio.DTO.Departamento import Departamento

class ReglasDepartamento:
    def __init__(self):
        self.departamentos = []

    def crear_objeto(self, codigo, nombre, descripcion=""):
        depto = Departamento(codigo, nombre, descripcion)
        return depto
    
    def agregar(self, departamento):
        self.departamentos.append(departamento)
        return True

    def mostrar_todos(self):
        return self.departamentos

    def buscar_por_codigo(self, codigo):
        for d in self.departamentos:
            if d.codigo == codigo:
                return d
        return None

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for d in self.departamentos:
            if nombre.lower() in d.nombre.lower():
                encontrados.append(d)
        return encontrados

    def modificar(self, departamento_modificado):
        for i, d in enumerate(self.departamentos):
            if d.codigo == departamento_modificado.codigo:
                self.departamentos[i] = departamento_modificado
                return True
        return False

    def eliminar(self, departamento):
        for d in self.departamentos:
            if d.codigo == departamento.codigo:
                self.departamentos.remove(d)
                return True
        return False
