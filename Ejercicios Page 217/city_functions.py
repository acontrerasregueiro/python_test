#Ejercicios test pagina 217

def formatea_ciudad_pais(ciudad,pais,population =''):

    if population:
        datos_formateados = f"{ciudad},{pais} - population {population}"        
    else:
        datos_formateados = f"{ciudad},{pais}"
        
    return datos_formateados.title()    
    