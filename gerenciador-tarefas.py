import os

tarefas = ['Regar as plantas', 'Jogar o lixo fora', 'Pagar as contas']

def titulo(msg):
    os.system('cls')
    print('-' * 40)
    print(msg.center(40))
    print('-' * 40)

def adicionar_tarefa():
    titulo('Adicionar Tarefas')
    nome = input('Digite a tarefa: ')
    tarefas.append(nome)
    print(f'A tarefa {nome} foi adicionada com sucesso!')
    voltar()

def visualizar_tarefas():
    titulo('Suas Tarefas')
    c = 1
    for i in tarefas:
        print(f'{c}. {i}')
        c += 1
    print()
    voltar()

def remover_tarefa():
    titulo('Remover uma Tarefa')
    c = 1
    for i in tarefas:
        print(f'{c}. {i}')
        c += 1
    esc = int(input('Escolha uma tarefa para remover [0 para não remover]: '))
    if esc != 0:
        esc2 = str(input(f'Deseja realmente remover a tarefa {tarefas[esc-1]} da sua lista? [S/N]: ')).upper().strip()
        if esc2 == 'S':
            del tarefas[esc-1]
            print('Tarefa removida com sucesso!')
            voltar()
        else:
            voltar()
    elif esc == 0:
        voltar()

def voltar():
    volt = input('Pressione alguma tecla para voltar: ')
    menu()

def menu():
    titulo('Menu Principal')
    print("""1. Adicionar tarefa
2. Visualizar tarefas
3. Remover tarefas
4. Sair""")
    esc = int(input('Escolha uma opção: '))
    if esc == 1:
        adicionar_tarefa()
    elif esc == 2:
        visualizar_tarefas()
    elif esc == 3:
        remover_tarefa()
    elif esc == 4:
        print('Saindo do programa...')
        os.system('cls')

menu()