# --------------------------------------------------------------------------------------

# Código sem funções:

cadastro_completo = False

while not cadastro_completo:
    nome = input('Digite seu nome: ')
    idade = int(input('Insira sua idade: '))
    rua = input('Insira a rua onde mora: ')
    bairro = input('Insira o bairro em que você mora: ')
    cidade = input('Insira a cidade em que você mora: ')

    print('Aqui estão os dados que você nos enviou:\n')
    print(f'Nome: {nome};')
    print(f'Idade: {idade} anos;')
    print(f'Endereço completo: {rua}, {bairro}, {cidade}')

    resposta = (input('Confirme os dados acima. Digite "True" se estiver correto ou "False" se algo estiver errado. Resposta: '))
    confirmacao = False

    if resposta.lower() == 'true':
        confirmacao = True
    else:
        confirmacao = False

    if confirmacao:
        print(f'Obrigado pela confirmação, {nome}. Em breve você receberá uma carta com as informações para seguir seu procedimento...')
        cadastro_completo = True
    else:
        print(f'Que pena, {nome}, vamos corrigir seus dados: \n')