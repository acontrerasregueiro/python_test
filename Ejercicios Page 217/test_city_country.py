from city_functions import formatea_ciudad_pais

def test_city_country():
    """Funcionan los nombres como Santiago y Chile"""
    ciudad_formateada = formatea_ciudad_pais('santiago','chile')
    assert(ciudad_formateada == 'Santiago,Chile')
    
    ciudad_formateada = formatea_ciudad_pais('santiago','chile',5000000)
    assert(ciudad_formateada == 'Santiago,Chile - Population 5000000')
    
    