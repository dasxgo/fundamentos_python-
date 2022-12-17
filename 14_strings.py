text = 'Ella sabe programar en Python'

'''
print('JavaScript' in text)
print('Python' in text)

if 'JS' in text:
  print('Elegiste bien!!')
else:
  print('Tambien elegiste bien')

'''
# len contamos cuantas letras tiene 

size = len(text)
print(size)

print(text)

# upper pasa a mayusculas
# lower pasa a minusculas
# count cantidad de letras dento del texto
# swapcase cualquier caracter mayuscula lo pasa a minuscula y visceversa
# Srastswith me indica si el texto inicia con algo que le indique
# endeswith me indica si el texto finaliza con algo que le indique
# remplace (remplaza)

print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Rust'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2)
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
print("398".isdigit())
