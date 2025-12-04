import os
from Presentacion.menu_departamento import MenuDepartamento
from Presentacion.menu_proyecto import MenuProyecto
from Presentacion.menu_empleado import MenuEmpleado

class MenuPrincipal:
    def __init__(self):
        self.opciones = [
            "Menú de Departamentos",
            "Menú de Proyectos",
            "Menú de Empleados",
            "Salir"
        ]

    def mostrar(self):
        while True:
            os.system('clear')
            print("\n===== MENÚ PRINCIPAL =====")
            for i, opcion in enumerate(self.opciones, 1): #para mostrar el numero y la opcion
                print("{}. {}".format(i,opcion))
            
            opcion = input("\nSeleccione una opción: ")
            

            if opcion == "1":
                self.ejecutar(MenuDepartamento())
            elif opcion == "2":
                self.ejecutar(MenuProyecto())
            elif opcion == "3":
                self.ejecutar(MenuEmpleado())
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")

    def ejecutar(self, menu):
        while True:
            opcion = menu.mostrarMenu()

            acciones = {
                "1": menu.agregar,
                "2": menu.mostrarTodos,
                "3": menu.buscarPorCodigo,
                "4": menu.buscarPorNombre,
                "5": menu.modificar,
                "6": menu.eliminar,
                "7": menu.volverMenuPrincipal
            }

            accion = acciones.get(opcion)

            if accion:
                accion()
                if opcion == "7":
                    break
            else:
                print("Opción inválida.")
