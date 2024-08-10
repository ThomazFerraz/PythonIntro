# Uma função é um bloco de código designada a executar uma tarefa específica.

# COMO CRIAR UMA FUNÇÃO:

# Usando o demarcador 'def' voce vai nomear sua função(funcao_exemplo) e entre parentesis colocará os 
# parametros necessśarios para realizar a tarefa da função, feche o parentesis e coloque dois pontos (:).
# Indente todo seu código para dentro da função (TAB).

# Sempre utilize nomes muito claros em suas funcoes, nao use letras maiusculas e nem espacos, separe as
# palavras usando underline (_).

def funcao_exemplo(variavel, variavel_x, variavel_y):
    '''Primeira coisa a se fazer é colocar entre ASPAS TRIPLAS a descrição da função.
    Insira o máximo de detalhes possíveis, para que serve e quais os tipos de variavels
    usados nela.

    Parametros:
    - variavel: string
    - variavel_x: int
    - variavel_y: bool
    '''

    # Agora monte o código da função utilizando os parametros estabelecidos.

    resposta = ''

    if variavel_y == True and variavel_x > 2:
        resposta = f'Muito bem, {variavel}!'

    else:
        resposta = f'Que pena, {variavel}'


    # return identifica o que será extraído da função, e será armazenado em
    # uma variável no código. Neste exemplo, a variável 'resposta' será
    # armazenada e devolvida ao fim da execução da função.
    return resposta



# Como usar uma função no código:

nome = 'Jonas'
idade = 4
esta_vivo = True

resultado = funcao_exemplo(nome, idade, esta_vivo)

print(f'Retorno da função: {resultado}')



