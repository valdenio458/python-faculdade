linguagens = ["Python", "JavaScript", "Ruby"]

print("Antes da list_comprehension = ", linguagens)

linguagens = [item.upper() for item in linguagens]

print("Após a list_comprehension = ", linguagens)