# Como de costume, utilizamos a frase "Hello World!" para iniciarmos nossos estudos.
# o comando print() irá imprimir algo no console do programa. No caso, a frase "Hello World!"

print('Hello World!')


#-------------------------------------------------------------------------------------------------#

# Agora vamos replicar o mesmo resultado, porém utilizando variáveis...


# Variáveis:
primeira_palavra = 'Hello'
segunda_palavra = 'World'

# Concatenar as variáveis string em uma nova variavel:
frase = primeira_palavra + ' ' + segunda_palavra +  '!'

# 'Printar' a variáveal frase

print(frase)

#-------------------------------------------------------------------------------------------------#

# Agora vamos melhorar a utilização de variáveis em uma só string...

# Variáveis
palavra_um = 'Hello'
palavra_dois = 'World'

# ao colocar a letra f antes de abrir aspas para elaborar uma string, você estará utilizando uma
# "f-string" que é uma string que permite formatar a frase juntamente a variáveis dentro dela.
# Para utilizar uma variável, basta inseri-la onde deseja, posicionando-a entre chaves {}

print(f'{palavra_um} {palavra_dois}!')


