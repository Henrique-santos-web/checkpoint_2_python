from tarefas import adicionar_tarefa, listar_tarefas, concluir_tarefa, carregar_dados, salvar_dados, excluir_tarefa

import time
import os
TEMPO_FINALIZACAO = 3

carregar_dados()
while True:
    try:   
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
                        concluir_tarefa(tarefa_concluida)
                        print("Bom Trabalho!")
                        salvar_dados()
                        time.sleep(1.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    except ValueError:
                        print("Digite apenas números")
                        time.sleep(TEMPO_FINALIZACAO)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
                    except IndexError:
                        print("Digite uma tarefa existe")
                        time.sleep(TEMPO_FINALIZACAO)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
            case 4:
                while True:
                    try:
                        listar_tarefas()
                        exclusao = int(input("Digite a tarefa a ser excluída: "))
                        excluir_tarefa(exclusao)
                        salvar_dados()
                        time.sleep(TEMPO_FINALIZACAO)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
                    except IndexError:
                        print("Digite apenas o número da tarefa")
                        time.sleep(1.5)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        continue
            case 5:
                print("Finalizando aplicação")
                time.sleep(TEMPO_FINALIZACAO)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            case _:
                try:
                    print("Opção inválida")
                    time.sleep(TEMPO_FINALIZACAO)
                except ValueError:
                    print("Digte uma opção válida!")
    except ValueError:
            print("BURRO!")
            time.sleep(TEMPO_FINALIZACAO)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue