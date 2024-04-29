from name_function import get_formatted_name
print("Enter 'q' at any time to quit")

while True:
    first = input("\n Dime el primer nombre: ")
    if first == 'q':
        break
    last = input("\n Dime el apellido: ")
    if last == 'q':
        break
    nombre_formateado = get_formatted_name(first,last)
    print(f"Nombre formateado correcto: {nombre_formateado}")