from collections import ChainMap

user = {"first_name" : "Bas", "last name" : "Steins"}
details = {"twitter" : "bascodes", "mobile" : "123-4567"}

chain = ChainMap(user, details)

print(chain["first_name"])

print(chain["twitter"])


if ...:

  print("Python is weird")
else:
  print("Pyton Python Python")

fruits = ["apple", "banana", "pineapple", "mango, strawberry"]

fruits[0] = "lemon"
print(list(fruits))

fruits.append("orange")
print(list(fruits))


fruits.remove("pineapple")
print(list(fruits))

fruits.insert(3, "melons")
print(list(fruits))

print(fruits.count("banana"))

fruits.remove("melons")
print(list(fruits))

