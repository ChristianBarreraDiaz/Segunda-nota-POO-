class Menu():
    def __init__(self,titulo:str, opciones: list[str]):
        self.titulo=titulo
        self.opciones=opciones

    def agregar(self):
        pass
    def mostrarTodos(self):
        pass
    def buscarPorCodigo(self):
        pass
    def buscarPorNombre(self):
        pass
    def modificar(self):
        pass
    def eliminar(self):
        pass
    def volverMenuPrincipal(self):
        print("\nVolviendo al menú principal...")
    
    def mostrarMenu(self):
        print("\n===== {} =====".format(self.titulo))
        
        for idx, opcion in enumerate(self.opciones, start=1):
            print("{}. {}".format(idx,opcion))
        try:
            eleccion = input("\nSeleccione una opción: ")
        except Exception as e:
            print(f"Error: {e}")
        return eleccion
    