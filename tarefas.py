lista_tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }

    lista_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!!") 
    #esté print aq é pra quando uma opcao no main ser selecionada
    # ele mostrar o print pra saber se deu certo

def listar_tarefas():
    for tarefa in lista_tarefas:
        print(tarefa["descricao"])