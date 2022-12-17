# Dictionary 

my_dict = {}
print(type(my_dict))

my_dict = {
  "avion" : "bla bla bla",
  "name" : "Nicolas", 
  "age" : 40,
  "country" : "Colombia"
  
}

print(my_dict)
print(type(my_dict))

# len (Cuantas categorias existen en el dicionario)

print(len(my_dict))
print(my_dict["age"])

# Get

print(my_dict["name"])
print(my_dict.get("name"))

print(my_dict.get("age"))

# Search 
print("avion" in my_dict)
print("otro que no" in my_dict)
