"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10
Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""


while True:
    # cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
    import re
    import sys

    # cpf_enviado_usuario = '746.824.890-70' \
    #     .replace('.', '') \
    #     .replace(' ', '') \
    #     .replace('-', '')
    entrada = input('CPF [746.824.890-70]: ')
    cpf_enviado_usuario = re.sub(
        r'[^0-9]',
        '',
        entrada
    )

    entrada_e_sequencial = entrada == entrada[0] * len(entrada)

    if entrada_e_sequencial:
        print('Você enviou dados sequenciais.')
        sys.exit()

    #cpf_enviado_usuario = "74682489070"


    cpf_nove_dgt = cpf_enviado_usuario[:9]

    regressivo1 = 10
    total_dig1 = 0

    for i in cpf_nove_dgt:
        mult = int(i) * regressivo1
        total_dig1 = total_dig1 + mult
        
        regressivo1 -= 1

    resutado_dig1 = (total_dig1*10) % 11

    digito1 = resutado_dig1 if resutado_dig1 <= 9 else 0


    cpf_dez_dgt = cpf_nove_dgt + str(digito1)

    #print(cpf_dez_dgt)

    regressivo2 = 11

    total_dig2 = 0
    for i in cpf_dez_dgt:
        total_dig2 += int(i) * regressivo2
        
        regressivo2 -= 1

    digito2 =  (total_dig2 * 10) % 11

    digito2 =  digito2 if digito2 <= 9 else 0

    cpf_gerado = cpf_dez_dgt + str(digito2)

    if cpf_enviado_usuario == cpf_gerado:
        print(f'O CPF: {cpf_gerado} é válido')
    else:
        print("Cpf Invalido")
