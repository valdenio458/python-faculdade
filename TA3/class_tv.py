class Televisao: 
    def __init__(self): # self é variável de instância
        self.volume = 10
    
    def aumentar_volume(self):
        self.volume += 2

    def diminuir_volume(self):
        self.volume -= 2

# instanciando um objeto da classe Televisão
tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentar_volume()
print("Volume atual = ", tv.volume)
