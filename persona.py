class Persona:
    def __init__(self):
        
        self.__edad = 0
    
        
    def obtener_edad(self):
        return f"su edad es: {self.__edad} años"
    
        
    def establecer_edad(self, nueva_edad):
        if 0 <= nueva_edad <= 120:
            self.__edad = nueva_edad
        else:
            print("Error: la edad no es valida, debe estar entre 0 y 120")
        
mi_edad = Persona()

mi_edad.establecer_edad(60) 
print(mi_edad.obtener_edad())  

mi_edad.establecer_edad(150)  
print(mi_edad.obtener_edad())     