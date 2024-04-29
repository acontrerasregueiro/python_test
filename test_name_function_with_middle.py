from name_function import get_formatted_name #Test ok
from failtest_name_function import get_formatted_name_with_middle   # Fail test
from corregido_failtest_name_function import get_formatted_name_with_middle_corregido

def test_first_last_name():
    """Funcionan los nombres como 'Janis Joplin' ????"""
    ##formated_name = get_formatted_name("janis","joplin")
    #assert formated_name == 'Janis Joplin'
    
    #El siguiente ejemplo dará error al ser 3 argumentos y pasar solo 2
    #formated_name = get_formatted_name_with_middle("janis", "joplin")
    #assert formated_name == 'Janis Joplin'

    #Corrigiendo la funcion para que funcione con middle name
    formated_name = get_formatted_name_with_middle_corregido("janis", "joplin")
    assert formated_name == 'Janis Joplin'

    