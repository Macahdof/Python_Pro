diccionario = {
    "SAPO": "chismoso, que cuenta todo a todos",
    "PLENA": "de verdad",
    "CALETA": "casa",
    "LATA": "dólar",
    "GUAGUA": "niño"
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in diccionario.keys():
    # ¿Qué debemos hacer si se encuentra la palabra?
    print(diccionario[word])
else:
    # ¿Qué hacer si no se encuentra la palabra?
    print("Esa palabra no se encuentra en el diccionario")
