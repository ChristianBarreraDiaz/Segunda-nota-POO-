#dominio
class Departamento:
    def __init__(self,codigo, nombre, descripcion=""):
        self.__codigo = codigo #doble guión bajo para encapsulamiento
        self.__nombre = nombre
        self.__descripcion = descripcion

    #devolver codigo privado
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,value):
        if not value: 
            raise ValueError("no puede estar vacío")#para validar conjuntos vacios 
        self.__codigo = value
    
    #devlver nombre privado
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
     if not value:
        raise ValueError("Nombre vacío")#validar que no este vacio
        self.__nombre = value

    #devolver descripcion privada
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value if value else ""#sino ingresa un valor se guarda vacio

    def __str__(self):
        return "{} - {}".format(self.__codigo, self.__nombre)#el primer {} para codigo y el segundo {} para nombre
    
