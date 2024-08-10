# Funções:

def coletar_dados():
    '''
    Função criada com a finalidade de coletar os dados do usuário.
    '''

    nome = input('Digite seu nome: ')
    idade = int(input('Insira sua idade: '))
    rua = input('Insira a rua onde mora: ')
    bairro = input('Insira o bairro em que você mora: ')
    cidade = input('Insira a cidade em que você mora: ')

    dados = [nome, idade, rua, bairro, cidade]

    return dados


def confirmar_dados(nome, idade, rua, bairro, cidade):
    '''
    Função elaborada com a finalidade de confirmar os dados inseridos 
    pelo usuário ANTES de prosseguir com o procedimento.

    Argumentos:
    - nome: str
    - idade: int
    - rua: str
    - bairro: str
    - cidade: str
    '''

    print('Aqui estão os dados que você nos enviou:\n')
    print(f'Nome: {nome};')
    print(f'Idade: {idade} anos;')
    print(f'Endereço completo: {rua}, {bairro}, {cidade}')

    resposta = bool(input('Confirme os dados acima. Digite "True" se estiver correto ou "False" se algo estiver errado. Resposta: '))

    return resposta


def mensagem_confirmacao(nome):
    '''
    Função auxiliar apenas para confirmar ao usuário que está tudo certo com
    o cadastro dele e que em breve entraremos em contato por correio.

    Argumentos:
    - nome: str
    '''

    print(f'Obrigado pela confirmação, {nome}. Em breve você receberá uma carta com as informações para seguir seu procedimento...')


# --------------------------------------------------------------------------------------

# Código com funções:

cadastro_completo = False

while not cadastro_completo:
    dados = coletar_dados()
    resposta = confirmar_dados(dados[0], dados[1], dados[2], dados[3], dados[4])

    if resposta:
        mensagem_confirmacao(dados[0])
        cadastro_completo = True

    else:
        print(f'Que pena, {dados[0]}, vamos corrigir seus dados: \n')

