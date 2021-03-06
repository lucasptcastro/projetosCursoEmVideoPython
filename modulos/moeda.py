#Função para mostrar um cabeçalho personalizado
def cab(txt, cor = 37, fundo = 41):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[1;{cor};{fundo}m{txt.center(48)}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)


#Função para dar uma linah de espaço
def espace():
    print(' ')


#Função para mostrar o dobro de um valor
def dobro(n):
    return n*2


#Função para mostrar a metade de um valor
def metade(n):
    return n/2


#Função para aumentar com uma porcentagem um valor
def aumentar(n, n2=10):
    a = (n*n2) / 100
    return n + a


#Função para reduzir com uma porcentagem um valor
def diminuir(n, n2=13):
    d = (n*n2) / 100
    return n - d


#Função para formatar um valor em real
def moedabr(n, format=True):
    if format == False:
        return n
    else:
        return f'R${n:.2f}'.replace('.',',')


#Função para fazer um resumo sobre um valor
def resumo(n=0, aum=25, red=25):
    cab("INFORMAÇÕES FINANCEIRAS")
    espace()
    print(f'Preço analisado: {" "*15 }\t{moedabr(n)}')
    print(f'Dobro do preço: {" "*15} \t{moedabr(dobro(n))}')
    print(f'Metade do preço: {" "*15} \t{moedabr(metade(n))}')
    print(f'\033[1;32m{aum}%\033[m de aumento: {" "*15} \t{moedabr(aumentar(n, aum))}')
    print(f'\033[1;31m{red}%\033[m de redução: {" "*15} \t{moedabr(diminuir(n, red))}')
    espace()


#Função para ler valores monetários e transformá-los em float
def leiaDinheiro(txt):
    while True:    
        n = str(input(txt)).replace(',','.')
        if n.isalpha():
            print(f'\033[1;31m{n} é um valor inválido, tente novamente!\033[m')
            continue
        elif n.strip() == "":
            print('\033[1;31mNenhum valor identificado, tente novamente!\033[m')
            continue    
        else:
            return float(n)



