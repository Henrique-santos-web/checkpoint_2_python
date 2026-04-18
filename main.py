from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, carregar_dados, salvar_dados

import time
import os
TEMPO_FINALIZACAO = 3

carregar_dados()
while True:
    print("1- Adicionar")
    print("2- Listar")
    print("3- Atualizar Tarefa")
    print("4- Remover Tarefa")
    print("5- Sair")
    opcao = int(input("Escolha uma opção: "))
    os.system('cls' if os.name == 'nt' else 'clear')

    match opcao:
        case 1: 
            descricao_tarefa = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(descricao_tarefa)
            salvar_dados()
            time.sleep(TEMPO_FINALIZACAO)
            os.system('cls' if os.name == 'nt' else 'clear')
        case 2:
            listar_tarefas()
            time.sleep(TEMPO_FINALIZACAO)
            os.system('cls' if os.name == 'nt' else 'clear')
        case 3:
            while True:
                try:
                    listar_tarefas()
                    tarefa_concluida = int(input("Digite em números qual tarefa você concluiu: "))
                    print("Bom trabalho!")
                    concluir_tarefa(tarefa_concluida)
                    salvar_dados()
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                except IndexError:
                    print("Digite apenas números")
                    time.sleep(TEMPO_FINALIZACAO)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue
            os.system('cls' if os.name == 'nt' else 'clear')  
        case 4:
            exclusao = int(input("Digite a tarefa a ser excluída"))
        case 5:
            print("Finalizando aplicação")
            time.sleep(TEMPO_FINALIZACAO)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        case _:
            print("Opção inválida")
            time.sleep(TEMPO_FINALIZACAO)