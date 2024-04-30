import pytest
from employee import Employee

#Testear la clase Employee usando el decorador @pytest.fixture

@pytest.fixture
def test_empleado():
    nombre = 'javier'
    apellido = 'lopez'
    salario = 10000    
    test_empleado = Employee(nombre,apellido, salario)
    return(test_empleado)

def test_empleado_defecto(test_empleado):
    test_empleado.dar_aumento()
    mostrar_aumento = test_empleado.mostrar_salario_aumento()
    assert mostrar_aumento == "El salario actual es 15000"
    
def test_empleado_variable(test_empleado):
    test_empleado.dar_aumento(15000)
    mostrar_aumento = test_empleado.mostrar_salario_aumento()
    assert mostrar_aumento == "El salario actual es 25000"