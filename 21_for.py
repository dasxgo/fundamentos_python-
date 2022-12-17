
    # Ciclos for

'''
for element in range(1, 21):
  print(element)


my_list = [23, 45, 67, 89, 43]
for element in my_list:
  print(element)


my_tuple = ("nico", "juli", "santi")
for element in my_tuple:
  print(element)
'''
product = {
  "name" : "Camisa",
  "price" : 100,
  "stock" : 89

}

for key in product: 
  print(key, "=>", product[key])

for key, value in product.items():
  print(key,"=>", value)

'''
people = [
  {
  "name" : "nico",
  "age" : 32
},
{
  "name" : "andrea",
  "age" : 22
},
{
  "name" : "santi",
  "age" : 18
}
]

for person in people:
  print("name =>", person["name"])

for person in people: 
  print("age =>", person["age"])

print(list(people))

print(type(people))

'''