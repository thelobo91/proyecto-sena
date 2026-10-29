class Coche:
    def __init__(self):
        self.__velocidad = 0
    
    
    @property
    def velocidad(self):
        return self.__velocidad 
            
    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        if 0 <= nueva_velocidad <= 200:
            self.__velocidad = nueva_velocidad
        else:
            print("Error: la velocidad debe estar entre 0 y 200 Km/H")
            
v = Coche()
    
v.velocidad = 210
print(v.velocidad)

v.velocidad = -10
print(v.velocidad)

v.velocidad = 120
print("velocidad actual:", v.velocidad, "km/h")

        