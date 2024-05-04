# Variáveis são elementos fundamentais não apenas em python mas em qualquer linguagem de programação.

# Tipos de variáveis:
# String: utilizada para textos, sentenças, siglas, abreviações;
# Int: utilizada para numerais inteiros positivos ou negativos;
# float: utilizada para numerais com casas decimais, positivos e negativos;
# boolean: True or False (Verdadeiro ou Falso);


# Exemplo:

titulo = 'O Senhor dos Anéis: A sociedade do Anel' # titulo é uma variável do tipo string que nos mostra o nome do livro
volume = 1 # volume é uma variável do tipo int que nos mostra qual é o volume do livro
preco = 34.99 # preco é uma variável do tipo float que nos mostra o preço do livro *utilizar . (ponto) para separar a casa decimal*
disponibilidade = False # disponibilidade é uma variável booleana que nos mostra se o livro está disponivel ou não.


# Concatenar strings

# a seguir temos duas variáveis:

var_x = '1'
var_y = '1'

# qual é o resultado da soma?

resultado = var_x + var_y

# com o comando print(resultado) conseguiremos ver este resultado:

print(f'Resultado = {resultado}')

# O resultado mostrado foi 11. Isso acontece pois as variaveis utilizadas na soma não são numerais, elas são do tipo STRING. o que
# significa que elas são textos. para fazer a soma devidamente, é necessário converter as variáveis o tipo desejado, no caso, para int.

var_x = int(var_x) # estou atribuindo um novo valor para a variável, para que deixe de ser texto e torne-se um numero inteiro.
var_y = int(var_y) # o mesmo está sendo feito para esta variável.

novo_resultado = var_x + var_y

print(f'Novo resultado = {novo_resultado}')

# Operações matemáticas.

# No exemplo a seguir teremos duas variáveis do tipo INT e a utilizaremos para fazer algumas operações matemáticas.
# Repare que na divisão (5/2), o valor do resultado foi arredondado para 2. Isso ocorre pois variáveis do tipo INT não utilizam casas decimais.

var_a = 2
var_b = 5

resultado_soma = var_a + var_b
print(f'Soma = {int(resultado_soma)}')

resultado_sub = var_a - var_b
print(f'Sub = {int(resultado_sub)}')

resultado_multi = var_a * var_b
print(f'Multi = {int(resultado_multi)}')

resultado_div = var_b / var_a
print(f'Div = {int(resultado_div)}')

# Para obter um valor preciso com casas decimais, é necessário fazer a conversão para o tipo FLOAT. 
# É tão simples converter como no exemplo acima. basta utilizar a sintaxe float(variavel_desejada)
# Exemplo:

resultado_float = var_b / var_a
float(resultado_float)
print(f'Resultado Float = {resultado_float}')