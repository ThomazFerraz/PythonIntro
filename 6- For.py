# O laço de repetição FOR (PARA CADA) é utilizado em diversas situações. Principalmente para lidar com listas, matrizes e afins. 
# Ainda não vimos o que são listas ou matrizes, mas não se preocupe com isto agora.
# Abaixo temos duas listas (Uma variável com um conjunto de valores).

lista_impar = [1, 3, 5, 7, 9]
lista_par = [2, 4, 6, 8, 0]

# O laço FOR a seguir vai imprimir cada número da lista impar:

for numero in lista_impar: # A interpretação da sintaxe fica: PARA CADA número dentro da lista_impar, imprima o numero.
    print(numero)


# O mesmo pode ser feito para a lista de numeros pares:

for numero in lista_par: # Para cada numero dentro da da lista_par, imprima o numero. 
    print(numero)


# Podemos também utilizar o laço for para outras coisas, como por exemplo:

nome = 'Asdrubal Gumercindo Junior'

for letra in nome: # Para cade letra no nome, imprima a letra.
    print(letra)


# note que no console foi impresso letra por letra do nome.