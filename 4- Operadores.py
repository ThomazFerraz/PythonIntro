# Para montarmos condicionais e laços de repetição é necessário conhecermos os Operadores Lógicos.
# Podemos criar comparações, verificar conteúdo, etc.
# Usaremos alguns casos de IF como exemplo para breves explicações dos operadores lógicos:


nome = 'Thomaz'
idade = 34
vacinado = True
astronauta = False


if nome: #Caso a variável nome não esteja vazia
    print('Sim, a variável nome está preenchida.')

if nome == 'Márcio': # Caso a variável nome seja IDENTICA á string 'Márcio'
    print('O nome é Márcio!')

if nome != 'Thiago': # Caso a variável nome SEJA DIFERENTE de 'Thiago'
    print('O nome não é Thiago!')

if 'a' in nome: # Caso a variável nome contenha a string 'a' 
    print('Existe a letra "a" no nome')

if 'ho' in nome: # Caso a variável nome contenha a string 'ho'
    print('Existe a string "ho" no nome')

if not vacinado: # Caso variavel vacinado seja False
    print('Não pode viajar sem as vacinas!')

if astronauta: # Caso variavel astronauta seja True
    print('Temos um astronauta por aqui!')




if idade >= 18: # Caso a idade seja maior ou igual a 18
    print('Maior de idade')

elif idade < 18: # Caso a idade seja menor do que 18
    print('Menor de idade')

else:
    print('Idade inválida!')




# também é possivel criar uma condicional IF com mais de uma condição, utilizando AND ou OR.
# AND é utilizado quando as duas condições PRECISAM SER ATENDIDAS. 
# OR é utilizado quando apenas uma das duas condições precisa ser atendida.

if nome == 'Thomaz' and idade == 35: # Este IF só será "ativado" caso a variável nome seja 'Thomaz' e a variável idade seja 35. 
    print('Thomaz tem 35 anos de idade!')

if nome == 'Thomaz' or nome == 'Chavinho': # Este IF será "ativado" caso a variável nome seja 'Thomaz' OU 'Chavinho'.
    print('Seja Thomaz ou Chavinho, ambos gostam de sanduíche de mortadela!')
