import re

def validacpf():
    pattern = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}-[0-9]{2}')
    cpf = input('Digite o CPF:')
    if pattern.match(cpf) and len(cpf) == 14:
        print('Válido.')

    else:
        print('Inválido.')
        validacpf()


validacpf()