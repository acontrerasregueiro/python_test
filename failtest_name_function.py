#Modificado para producir un error
#Python crash course page 211

def get_formatted_name_with_middle(first,middle,last):
    """ Genera un nombre formateado correctamente"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()