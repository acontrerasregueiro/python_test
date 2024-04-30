from employee import Employee

def test_employee_default():
    """Comprobamos que funciona la clase con incremento por defecto"""
    
    javier =Employee("javier","lopez",10000)
    javier.dar_aumento()
    mostrar_datos = javier.mostrar_salario_aumento()
    assert mostrar_datos == "El salario actual es 15000" 

def test_employee_variable():
    """Comprobamos que funciona la clase para un incremento variable"""
    javier =Employee("javier","lopez",10000)
    javier.dar_aumento(15000)
    mostrar_datos = javier.mostrar_salario_aumento()
    assert mostrar_datos == "El salario actual es 25000" 
        