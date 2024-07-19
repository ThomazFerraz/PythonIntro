# O laço de repetição WHILE (ENQUANTO), é usado para criar uma repetição até que certa condição seja atendida. 
# Usaremos uma variável numérica começando em ZERO, e a cada vez que ela passar pelo laço de repetição WHILE,
# seu valor aumentará. E o laço só vai parar quando a variável possuir um valor acima de 20.


variavel = 0

while variavel < 20: # ENQUANTO a variavel for MENOR DO QUE 20, o código dentro do laço while vai se repetir

    print('A variável ainda não tem o valor de 20!')

    print(f'Seu valor atual é de {variavel}')

    variavel += 1

print('Finalmente a variável chegou a 20!')