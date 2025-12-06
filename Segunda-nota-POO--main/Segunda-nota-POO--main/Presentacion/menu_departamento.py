from Presentacion.menu_base import Menu

class MenuDepartamento(Menu):
    def __init__(self):
        super().__init__(
            titulo="Menú de Departamentos",
            opciones=[
                "Agregar Departamento",
                "Mostrar Todos",
                "Buscar por Código",
                "Buscar por Nombre",
                "Modificar",
                "Eliminar",
                "Volver al Menú Principal"
            ]
        )

    def agregar(self):
        print("Agregar Departamento (presentación)")
        #Aqui y en los demas metodos falta 
        #agregar la conexion al metodo de la clase correspondiente
    
    def mostrarTodos(self):
        print("Mostrar todos los Departamentos (presentación)")
        #Aqui y en los demas metodos falta 
        #agregar la conexion al metodo de la clase correspondiente
    def buscarPorCodigo(self):
        print("Buscar Departamento por Código (presentación)")
    
    def buscarPorNombre(self):
        print("Buscar Departamento por Nombre (presentación)")
    
    def modificar(self):
        print("Modificar Departamento (presentación)")
    
    def eliminar(self):
        print("Eliminar Departamento (presentación)")
