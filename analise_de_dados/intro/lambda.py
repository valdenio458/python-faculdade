# Para criar essa função anônima, usamos a palavra reservada "lambda" passando como parâmetro "x". Os dois pontos é o que separa a definição da função anônima da sua ação. Veja que após os dois pontos, é feito o cálculo matemático x + 1. Na frente da função, já a invocamos passando como argumento o valor x = 3.
print((lambda x: x + 1)(x = 3))
print((lambda x, y: x + y)(x = 3, y = 2))

first_char = lambda s: s[0]
print(first_char('Valdênio'))

first_char = (lambda s: s[0])(s='Martinho')
print(first_char)