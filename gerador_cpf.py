
import random


validade = []

# verifica cpf


def soma(inicio, final, *args):
    l = 0
    multiplicador = 10
    cpf = args[0]

    for numero in range(inicio, final):

        l = l +(multiplicador * cpf[numero])
        multiplicador -= 1

    return l


def gera_ou_verificad(l, posicao, *args):
    cpf = args[0]

    r = l % 11
    k = l / 11

    if r == 0 or r == 1:
        if cpf[posicao] == 0:
            validade.append(1)
        else:
            validade.append(0)
    else:
        if cpf[posicao] == (11 - r):
            validade.append(1)
        else:
            validade.append(0)

    return validade


def verifica_cpf(*args):
    cpf = args[0]
    (gera_ou_verificad(soma(0, 9, cpf), 9, cpf))
    (gera_ou_verificad(soma(1, 10, cpf), 10, cpf))
    if all(validade):
        print("cpf valido")
    else:
        print("cpf invalido")


# gera cpf

def gerad10(l, *args):
    cpf = args[0]
    cpf = list(cpf)

    r = l % 11
    k = l / 11

    if r == 0 or r == 1:
        cpf.append(0)
    else:
        cpf.append(11-r)

    return cpf

def gera_9d():
    cpf = []

    while len(cpf) < 9:
        digito = random.randrange(0,9)
        cpf.append(digito)
    return cpf

def gerad11(l, *args):
    cpf = args[0]
    cpf = list(cpf)

    r = l % 11
    k = l / 11

    if r == 0 or r == 1:
        cpf.append(0)
    else:
        cpf.append(11 - r)

    return cpf


def gera_cpf():
    gerador = gera_9d()

    quase = gerad10(soma(0, 9, gerador), gerador)

    cpf_gerado = gerad11(soma(1, 10, quase), quase)

    cpf = ''

    for x in cpf_gerado:
        cpf += str(x)

    print(cpf)


while True:
    cpf = []
    escolha = False
    while not escolha:
        op = input("Digite: \n 1 | Validar cpf\n 2 | Gerar cpf \n \n")
        try:
            op = int(op)
            if op > 2:
                pass
            elif op < 0:
                pass
            else:
                escolha = True
        except:
            pass


    if op == 0:
        break
    elif op == 1:
        cp = str(input("Digite o cpf: \n"))
        for x in cp:
            cpf.append(int(x))

        verifica_cpf(cpf)

    elif op == 2:
        gera_cpf()