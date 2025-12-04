from Dominio.DTO.Proyecto import Proyecto

class ReglasProyecto:
    def validar(self, proyecto):
        if proyecto.presupuesto > 1000000000:
            raise ValueError("Presupuesto demasiado alto")
        return True
