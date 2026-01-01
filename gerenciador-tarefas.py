import os

arquivo = 'tarefas.txt'

def carregar_tarefas():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w'):
            pass
        return []
    
    with open(arquivo, 'r', encoding='utf-8') as arq:
        return [linha.strip() for linha in arq.readlines()]

def salvar_tarefas():
    with open(arquivo, 'w', encoding='utf-8') as arq:
        for tarefa in tarefas:
            arq.write(tarefa + '\n')

tarefas = carregar_tarefas()

def titulo(msg):
    """
    Adiciona um título configurado para cada opção.

    Args:
        msg (string): Define o título que vai aparecer
    """
    
    os.system('cls')
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)

def adicionar_tarefa():
    """
    Possibilita adicionar novas tarefas à lista
    """

    titulo('Adicionar Tarefas')
    nome = input('Digite a tarefa: ')
    tarefas.append(nome)
    salvar_tarefas()
    print(f'A tarefa {nome} foi adicionada com sucesso!')
    voltar()

def visualizar_tarefas():
    """
    Visualiza todas as tarefas existentes na lista
    """

    titulo('Suas Tarefas')
    c = 1
    for i in tarefas:
        print(f'{c}. {i}')
        c += 1
    print()
    voltar()

def remover_tarefa():
    """
    Possibilita remover alguma tarefa existente digitando seu índice
    """

    titulo('Remover uma Tarefa')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'{i}. {tarefa}')

    esc = int(input('Escolha uma tarefa para remover [0 para não remover]: '))

    if esc == 0:
        voltar()
        return
    
    if 1 <= esc <= len(tarefas):
        confirmacao = input(f'Deseja realmente remover "{tarefas[esc-1]}"? [S/N]').upper().strip()

        if confirmacao == 'S':
            del tarefas[esc-1]
            salvar_tarefas()
            print('Tarefa removida com sucesso!')
    voltar()

def voltar():
    """
    Comando rápido para voltar ao menu principal
    """

    volt = input('Pressione alguma tecla para voltar: ')
    menu()

def menu():
    """
    Mostra as opções disponíveis no programa
    """

    titulo('Menu Principal')
    print("""1. Adicionar tarefa
2. Visualizar tarefas
3. Remover tarefas
4. Sair""")
    try:
        esc = int(input('Escolha uma opção: '))
        if esc == 1:
            adicionar_tarefa()
        elif esc == 2:
            visualizar_tarefas()
        elif esc == 3:
            remover_tarefa()
        elif esc == 4:
            os.system('cls')
        else:
            raise ValueError
    except ValueError:
        print('ERRO! Digite apenas números de 1 a 4!')
        voltar()

menu()