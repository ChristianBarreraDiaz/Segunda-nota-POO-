from Dominio.DTO.Departamento import Departamento

class ReglasDepartamento:
    def validar(self, departamento):
        if len(departamento.codigo) > 10:
            raise ValueError("El código del departamento es muy largo (máximo 10 caracteres)")
        if len(departamento.nombre) > 100:
            raise ValueError("El nombre del departamento es muy largo")
        # Si llega aquí, está OK
        return True

