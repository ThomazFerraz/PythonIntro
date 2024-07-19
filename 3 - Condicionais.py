# Este documento aprenderemos sobre as condições IF, ELIF e ELSE (SE, SENÃO-SE, SENÃO)
# Durante o dia a dia do programador, ele se depara com muitas situações onde se faz necessário aplicar condicionais e tratativas
# Para que seu aplicativo/código funcione de forma eficiente e sem erros. E para tais tratativas, usa-se muito os laços condicionais.

# Exemplo:

var_x = 90
var_y = 16

if var_x > var_y:

    print('Variável X é maior que variável Y')

elif var_y > var_x:

    print ('Variável Y é maior que Variável X')

else:

    print('As variáveis tem o mesmo valor')


# Repare que ao rodar o código, a única frase que aparece é a "Variável X é maior que a variável Y".
# Isso se dá pois apenas a condição dentro do IF é cumprida. as condições do ELIF não são atendidas
# e o ELSE só é acionado caso nenhuma das demais condições seja atendida.

# Experimente mudar o valor das variáveis com o intuito de mudar a frase a ser mostrada.