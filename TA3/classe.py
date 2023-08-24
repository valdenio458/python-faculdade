class FirstClass: 
    
    def print_msg(self, name): # criando um método
        print(f"Olá {name}, seja bem vindo!")

obj1 = FirstClass() # instanciando um objeto 
obj1.print_msg('João') # invocando o método