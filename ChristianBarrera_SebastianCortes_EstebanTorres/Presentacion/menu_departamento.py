from Presentacion.menu_base import Menu
from Persistencia.DAO.EmpleadoDAO import mostrar_todos

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
        
        #1. Se piden los datos
        nombre=input("Ingrese el Nombre del Departamento: ")
        
        #2. Mostrar datos de Empleados 
        datos=Persistencia.DAO.EmpleadoDAO.mostrar_todos()
        print("************* Mostrar Empleados ***********")
        print("ID\t\tNombre Empleado")
        for dato in datos:
            print("{}\t\t{}".format(dato[0],dato[1])) #ID    Nombre Empleado
        print("***********************************************")
        empleados=[]
        n=1
        while n:
            empleado=input("Ingrese nombre del empleado: ")
            empleados.append(empleado)#Aqui se agrega con un append a empleados
            op=input("Desea agregar otro empleado? ") #tener cuidado con los valores a ingresar
            if op == "si"or"Si"or"SI" : #preguntar si queremos salir del ciclo
                continue
            else:
                break
            
        #2. Mostrar datos de Empleados 
        datos=Persistencia.DAO.EmpleadoDAO.mostrar_todos()
        print("************* Mostrar Empleados ***********")
        print("ID\t\tNombre Empleado")
        for dato in datos:
            print("{}\t\t{}".format(dato[0],dato[1])) #ID    Nombre Empleado
        print("***********************************************")
        gerente=input("Ingrese el nombre del gerente a cargo: ")
        
        #3. Mandar los datos a la aplicacion para crear objeto
        


        #4. Mandar el objeto para insertar en BD
    
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
