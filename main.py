from tarefas import adicionar_tarefa, listar_tarefas
while True:
    print("1- Adicionar")
    print("2- Listar")
    print("3- Sair")
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1: 
            descricao_tarefa = input("Dgite a descrição da tarefa: ")
            adicionar_tarefa(descricao_tarefa)
        case 2:
            pass
        case 3:
            print("Finalizando aplicação")
            break
