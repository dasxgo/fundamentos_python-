# Operadores logicos 

# and

print("and")
print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

print(10 >= 5 and 5 < 10)

stock = input("ingrese el numero de stock => ")
stock = int(stock)
print(stock >= 100 and stock <=1000)

# or (si alguno de los dos es True el resl12_utado es True)

print("or")
print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

role = input("Digital el rol => ")
print(role == "admin" or role == "seller")

# NOT

print(not True)
print(not False)

print("not and")
print("not True and True =>", not (True and True))
print("not True and False =>", not (True and False))
print("not False and True =>", not (False and True))
print("not False and False =>", not (False and False))


stock = input("ingrese el numero de stock => ")
stock = int(stock)
print(not stock >= 100 and stock <=1000)