from Presentacion.menu_base import Menu

class MenuProyecto(Menu):
    def __init__(self):
        super().__init__(
            titulo="Menú de Proyectos",
            opciones=[
                "Agregar Proyecto",
                "Mostrar Todos",
                "Buscar por Código",
                "Buscar por Nombre",
                "Modificar",
                "Eliminar",
                "Volver al Menú Principal"
            ]
        )

    def agregar(self):
        print("Agregar Proyecto (presentación)")
        #Aqui y en los demas metodos falta 
        #agregar la conexion al metodo de la clase correspondiente

    def mostrarTodos(self):
        print("Mostrar todos los Proyectos (presentación)")

    def buscarPorCodigo(self):
        print("Buscar Proyecto por Código (presentación)")

    def buscarPorNombre(self):
        print("Buscar Proyecto por Nombre (presentación)")

    def modificar(self):
        print("Modificar Proyecto (presentación)")

    def eliminar(self):
        print("Eliminar Proyecto (presentación)")
