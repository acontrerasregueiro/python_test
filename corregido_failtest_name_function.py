#Modificado para producir un error
#Python crash course page 211

def get_formatted_name_with_middle_corregido(first,last,middle=''):
    #Al poner middle como último es optativo y le damos un valor por defecto
    """ Genera un nombre formateado correctamente"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()