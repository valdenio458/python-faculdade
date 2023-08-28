import matplotlib.pyplot as plt 
import random

lista1 = random.sample(range(100), k = 20)
lista2 = random.sample(range(100), k = 20)

plt.plot(lista1, lista2)