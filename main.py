class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    
    def cambiarColor(self,x):
        lista=["rojo","verde","amarillo","negro","blanco"]
        for i in lista:
            if i==x:
                self.color=x

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
        
    def cambiarRegistro(self, y):
        if type(y)==int:
            self.registro=y
            
    def asignarTipo(self,z):
        modelos=["electrico","gasolina"]
        for i in modelos:
            if i==z:
                self.tipo=z

class Auto:
    cantidadCreados=None
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        
    def cantidadAsientos(self):
        conteo=0
        for i in self.asientos:
            if i!=None:
                conteo+=1
        return conteo
    
    def verificarIntegridad(self):
        resultado=""
        if self.motor.registro==self.registro:
            resultado="Auto original"
            for i in self.asientos:
                if i!=None:
                    if i.registro!=self.registro:
                        resultado="Las piezas no son originales"
        else:
            resultado="Las piezas no son originales"
        return resultado
