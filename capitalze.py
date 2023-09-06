# Función para capitalizar un string. Es decir, en mayúsculas la primera 
# letra de cada palabra del array

words = ['hola', 'estoy', 'es', 'tu', 'curso', 'de', 'pitón', 'en', 'español! :D']

def capitlize (words):
    for word in words:
        print(word.capitalize(), end= ' ')

capitlize(words)
print(' ')
