from time import sleep

#Cores
def vermelho(txt, fundo=40):
    return f'\033[1;31;{fundo}m{txt}\033[m'

def verde(txt, fundo=40):
    return f'\033[1;32;{fundo}m{txt}\033[m'

def branco(txt, fundo=40):
    return f'\033[1;{fundo}m{txt}\033[m'

def amarelo(txt, fundo=40):
    return f'\033[1;33;{fundo}m{txt}\033[m'

def azul(txt, fundo=40):
    return f'\033[1;36;{fundo}m{txt}\033[m'

#Cabeçalho
def cab(txt, cor=37, fundo=41):
    print('\033[1;37m=\033[m'*50)
    print(f'\033[1;37m|\033[m\033[1;{cor};{fundo}m{txt.center(48)}\033[m\033[1;37m|\033[m')
    print('\033[1;37m=\033[m'*50)

#Dar um espaço
def espace():
    print(' ')

#Mostrar uma linha
def linha(i=50):
    print('='*i)

#Interface
def menu(lista):
    cab("INTERFACE PYTHON", cor=37, fundo=41)
    c = 1
    for item in lista:
        print(f'{amarelo(c)} - {verde(item)}')
        c+=1
    linha()
    question = leiaInt(azul("▶ Informe sua opção: "))
    return question

def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print(vermelho("ERRO! Por favor, informe um número inteiro válido!"))
            continue
        except (KeyboardInterrupt):
            print(vermelho("\nERRO! Nenhuma entrada de dados informada!"))
            return 0
        else:
            return n

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        sleep(1)
        print(vermelho('Houve um erro na criação do arquivo!'), flush=True)
    else:
        sleep(1)
        print(f'▶ Arquivo {azul(nome)} não existe! Criado com sucesso!', flush=True)

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(vermelho('Houve um erro na leitura do arquivo!'))
    else:
        cab('PESSOAS CADASTRADAS:', 31, 47)
        print(a.read())
    finally:
        a.close()

def cadastro(arq, nome='Nulo', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(vermelho('Houve um erro ao abrir o arquivo!'))
    else:
        try:
            a.write(f'{nome:<30}{idade:>3} anos\n')
        except:
            print(vermelho('Houve um erro ao adicionar as informações no arquivo!'))
        else:
            print(verde(f'Novo registro adicionado ao arquivo!'))
            a.close()