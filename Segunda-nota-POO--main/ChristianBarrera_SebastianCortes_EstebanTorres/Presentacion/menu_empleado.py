from Presentacion.menu_base import Menu

class MenuEmpleado(Menu):
    def __init__(self):
        super().__init__(
            titulo="Menú de Empleados",
            opciones=[
                "Agregar Empleado",
                "Mostrar Todos",
                "Buscar por Código",
                "Buscar por Nombre",
                "Modificar",
                "Eliminar",
                "Volver al Menú Principal"
            ]
        )

    def agregar(self):
        print("Agregar Empleado (presentación)")
        #Aqui y en los demas metodos falta 
        #agregar la conexion al metodo de la clase correspondiente

    def mostrarTodos(self):
        print("Mostrar todos los Empleados (presentación)")

    def buscarPorCodigo(self):
        print("Buscar Empleado por Código (presentación)")

    def buscarPorNombre(self):
        print("Buscar Empleado por Nombre (presentación)")

    def modificar(self):
        print("Modificar Empleado (presentación)")

    def eliminar(self):
        print("Eliminar Empleado (presentación)")
