linguagens = ["Python", "JavaScript", "Ruby"]

print("Antes da list_comprehension = ", linguagens)

linguagens = [item.upper() for item in linguagens]

print("Após a list_comprehension = ", linguagens)



# Outro exemplo com números:

# list = [2, 4, 6, 8]
# list = [5 * item for item in list]
# print(list) # [10, 20, 30, 40]