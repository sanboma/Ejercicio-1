mensaje = "fundamentos de programacion"
vocales = 'aeiouAEIOU'  


conteo_vocales = 0


for caracter in mensaje:
   
    if caracter in vocales:
        conteo_vocales += 1
        print(f"Se encontró la vocal '{caracter}' en el mensaje.")


print(f"El mensaje tiene {conteo_vocales} vocal(es).")