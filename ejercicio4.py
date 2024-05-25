def contador_frecuencia(cadena):
    palabras = cadena.split()

    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(diccionario):
    palabra_mas_repetida = max(diccionario, key=diccionario.get)
    frecuencia_palabra_mas_repetida = diccionario[palabra_mas_repetida]
    return palabra_mas_repetida, frecuencia_palabra_mas_repetida

cadena = " Me dijeron que en el Reino del Revés Nada el pájaro y vuela el pez Que los gatos no hacen miau y dicen yes Porque estudian mucho inglés Vamos a ver cómo es El Reino del Revés Vamos a ver cómo es El Reino del Revés Me dijeron que en el Reino del Revés Nadie baila con los pies Que un ladrón es vigilante y otro es juez Y que dos y dos son tres"
diccionario = contador_frecuencia(cadena)

palabra, frecuencia = palabra_mas_repetida(diccionario)

print("La palabra más frecuente es'",palabra,"'y se repite",frecuencia,"veces.")