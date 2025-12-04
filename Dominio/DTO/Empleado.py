from .Departamento  import Departamento       

class Empleado:
    def __init__ (self,id, nombre, direccion, correo,salario,departamento,fecha_contrato):
        self.__nombre = nombre
        self.__id = id
        self.__direccion = direccion
        self.__correo = correo
        self.__salario = salario
        self.__departamento = departamento
        self.__fecha_contrato = fecha_contrato
    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nuevo_valor):
        if not nuevo_valor:
            raise ValueError("Nombre vacio")
        self.__nombre = nuevo_valor

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self,nuevo_valor):
        if not nuevo_valor:
            raise ValueError("Dirección Vacia")
        self.__direccion = nuevo_valor 

    @property 
    def correo(self):
        return self.__correo
    @correo.setter #falta añadir el validador de @ 
    def correo(self,nuevo_valor):
        if not nuevo_valor:
            raise ValueError("Correo Vacio")
        self.__correo = nuevo_valor   
    
    @property
    def salario(self):
        return self.__salario
    @salario.setter
    def salario(self,nuevo_valor):
        try:
            monto_salario = float(nuevo_valor)
        except ( TypeError, ValueError): #para validar si se puede convertir en numeros
            raise ValueError("El monto debe ser un valor válido")
        if monto_salario <= 0:
            raise ValueError("El monto debe ser mayor a cero")
        self.__salario = monto_salario #se modifica el salario si para el try y el if
    
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, nuevo_valor):
        if nuevo_valor is None:
            raise ValueError("El departamento no puede ser nulo.")
        if not isinstance(nuevo_valor, Departamento):
            raise TypeError("El departamento debe venir de la clase Departamento.")
    
        self.__departamento = nuevo_valor
    
    @property
    def fecha_contrato(self):
        return self.__fecha_contrato
    @fecha_contrato.setter
    def fecha_contrato(self,nuevo_valor):
        if not nuevo_valor:
            raise ValueError("Fecha de contrato no especificada")
        self.__fecha_contrato = nuevo_valor
    
    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.__nombre, self.__direccion, \
                                                    self.__correo, self.__salario, self.__departamento,\
                                                     self.__fecha_contrato) #esto hay que corregir 