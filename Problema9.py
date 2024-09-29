def omitir_vocales(texto):
    vocales = "aeiouAEIOU"
    texto_sin_vocales = ''.join(caracter for caracter in texto if caracter not in vocales)
    return texto_sin_vocales
texto_usuario = input("Ingresa una cadena de texto: ")
resultado = omitir_vocales(texto_usuario)
print(f"Texto sin vocales: {resultado}")
