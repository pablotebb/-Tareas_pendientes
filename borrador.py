def solo_letras(cadena):
    palabras = cadena.split()  # Dividir la cadena en palabras
    for palabra in palabras:
        if not palabra.isalpha():
            raise ValueError("La cadena solo debe contener letras")
    return True

try:
    entrada = input("Introduce una cadena de letras: ")
    if solo_letras(entrada):
        print("La cadena introducida contiene solo letras.")
except ValueError as error:
    print("Error:", error)
