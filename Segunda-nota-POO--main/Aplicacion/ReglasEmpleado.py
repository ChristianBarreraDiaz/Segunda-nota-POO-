from Dominio.DTO.Empleado import Empleado

class ReglasEmpleado:
    def validar(self, empleado):
        if empleado.email != "" and "@" not in empleado.email:
            raise ValueError("El correo electrónico no es válido")
        return True
