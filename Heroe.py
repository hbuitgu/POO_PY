##una clase es un molde, el nombre del archivo debe ser en mayuscula la primera letra por convencion.
Class Heroe:

    ##contructor de la clase 
    ##constructor es igual a una funcion ESPECIAL, es decir el contructor es una funcion que permite inicializar los atributos, siempre lleva la palabra "self", como referencia a la misma clase y despues de self coloco los parametros que quiero inicializar
    

    def__init__(self, name,heiht,poder):
        self.poder=poder
        self.nombre=name
        self.estatura=heiht
        self.tipoHeroe=None
        self.cantidad_Vida=None
##atributos = propiedades =datos 
##variables del lenguaje que yo elija 
#metodos =acciones ¿que hace mi molde
##todos los metodos en pyton debe tener el self dentro de los parametro de la funcion  
    def saludar():
        print("hola....")

##funciones del lenguaje que yo elija 


##utilizando la clase, es lo mismo que decir crear una instancia, sacar fotocopiia, crear el objeto. 

##un objeto sin importar el lenguaje siempre es una variable especial. 

batman = Heroe('bruce wayne',1.90,500)
jocker= Heroe('nn',170,1200)

#con el objeto accedo al atributo 
print(batman)
print(jocker.poder)


#con el objeto acceso a un metodo (Fuction)
batman.saludar()