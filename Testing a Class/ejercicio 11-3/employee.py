#Ejercicio Pag 223. 11-3

class Employee:
    def __init__(self,nombre,apellido,salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        
    def dar_aumento(self,incremento = 5000):
        self.salario += incremento
        
    def mostrar_salario_aumento(self):
        return(f"El salario actual es {self.salario}")
        

empleado = Employee('adrian','contreras',22000)
empleado.dar_aumento()
empleado.mostrar_salario_aumento()

empleado = Employee('javier','lopez',22000)
empleado.dar_aumento(8000)
empleado.mostrar_salario_aumento()
