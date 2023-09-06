# Función para capitalizar un string. Es decir, en mayúsculas la primera 
# letra de cada palabra del array

words = 'hola estoy es tu curso de pitón en español! :D'

def capitlize (words):
    arr = words.split(' ')
    for word in arr:
        print(word.capitalize(), end= ' ')

capitlize(words)
print(' ')
