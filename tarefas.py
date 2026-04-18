import json, time
tempo = 3

lista_tarefas = []

def salvar_dados():
    with open("dados.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo)


def carregar_dados():
    global lista_tarefas
    try:
        with open("dados.json", "r") as arquivo:
           lista_tarefas = json.load(arquivo)
    except FileNotFoundError:
        print("Nenhum dado encontrado!")
        lista_tarefas = []


def adicionar_tarefa(descricao):
    tarefa = {
        "descricao": descricao, "concluida": False
    }
    if descricao == lista_tarefas:
        print("Está tarefa já existe")
    else:
        lista_tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!!")

    salvar_dados()


def listar_tarefas():
    for indice, tarefa in enumerate(lista_tarefas):

        if tarefa["concluida"] == True:
            print(f"{indice} - [X] {tarefa['descricao']} | concluída")
        else:
            print(f"{indice} - [] {tarefa['descricao']} | pendente")


def concluir_tarefa(indice):
    lista_tarefas[indice]["concluida"] = True


def excluir_tarefa(excluir):
    for indice in enumerate(lista_tarefas):
        try:
            if indice == excluir:
                print("Tarefa excluída!")
                lista_tarefas.pop(indice)
            else:
                print("Digite um número válido")
        except ValueError:
            print("Digite apenas a posição da tarefa!")