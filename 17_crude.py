# Crud - create, read, update, delete
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0,"hola")
print(numbers)
numbers.insert(3, "change")
print(numbers)


task = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + task
print(new_list)

# index cambia algo del array
index = new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

#pop elimina el ultimo de la lista

new_list.pop()
print(new_list)