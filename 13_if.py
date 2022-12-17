if True:
  print("deberia ejecutarse")

if False:
  print("nunca deberia ejecutarse")


pet = input("¿Cual es tu mascota favorita? ")

if pet == "perro" :
 print("genial tienes buen gusto")
elif pet == "gato" :
  print("espero que tengas suerte")
elif pet == "pez" :
  print("eres lo maximo")
else:
  print("no tienes ninguna mascota interesante")

# else (lo contrario de if si esa accion no sucede)

'''
stock = int(input("Digita el stock => "))

# else se usa si no cumple con la condicion 

if stock >= 100 and stock <= 1000 :
  print("el stock es correcto")
else:
  print("el stock es incorrecto")
'''
