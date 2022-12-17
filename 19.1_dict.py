# call Diccionary

person = {
  "name" : "David",
  "last_name" : "Sarmiento",
  "langs" : ["python", "JavaSript"],
  "age" : 38
  
}

print(person)


person["name"] = "santi" 
person["last_name"] = "Araujo"
person["age"] -= 10 
person["langs"].append("rust")
print(person)

# Remove del or pop

del person["last_name"]
person.pop("age")

print(person)

# Call items

print("items")
print(person.items())


# Call keys

print("keys")
print(person.keys())

# Call values

print("values")
print(person.values())