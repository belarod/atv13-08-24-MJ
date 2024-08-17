import re


def validacpf():
    pattern = re.compile('[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}')
    cpf = input('Digite o CPF:')
    CPFlimpo = re.sub(r'\D', '', cpf)  # r'\D' tudo que não é digito ---> substitui por '' (nadinha)
    numsCPF = list(CPFlimpo)

    def verif_primDIG(): #calcula 1o digito verificador
        numsCPF = list(CPFlimpo) #separa os numeros individualmente

        multiplier = 10
        i = 0
        res = []
        while multiplier >= 2: #começando pelo 10, multiplica cada num do cpf pelo seu respectivo multiplicador
            numsCPF = list(CPFlimpo[:9])
            multnumCPF = int(numsCPF[i])*multiplier
            res.insert(i, multnumCPF)
            multiplier -= 1
            i += 1

        res_primDIG = 11-(sum(res)%11) #calculo c/multiplier
        if res_primDIG >= 10:
            res_primDIG = 0
            return res_primDIG
        else:
            return res_primDIG

    def verif_segDIG(): #calcula segundo digito verificador
        numsCPF = list(CPFlimpo)

        multiplier = 11
        i = 0
        res = []
        while multiplier >= 2: #começando pelo 11, multiplica cada num do cpf pelo seu respectivo multiplicador
            numsCPF = list(CPFlimpo[:10])
            multnumCPF = int(numsCPF[i]) * multiplier
            res.insert(i, multnumCPF)
            multiplier -= 1
            i += 1

        res_segDIG = 11 - (sum(res) % 11) #calculo c/ módulo
        if res_segDIG >= 10:
            res_segDIG = 0
            return res_segDIG
        else:
            return res_segDIG

    resultado1 = int(verif_primDIG())
    resultado2 = int(verif_segDIG())

    if pattern.match(cpf) and len(cpf) == 14 and resultado1 == int(numsCPF[9]) and resultado2 == int(numsCPF[10]):
        print('Válido.')

    else:
        print('Inválido.')
        validacpf()


validacpf()