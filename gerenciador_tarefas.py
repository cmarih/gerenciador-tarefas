## Funções
def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada.")
    return

def ver_tarefas(tarefas):
    print("\n Lista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✅" if tarefa["completada"] else "❌"
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return
    
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if  indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa '{nome_tarefa}' atualizada para '{novo_nome_tarefa}'")
    else:
        print("Terefa não encontrada!!!!")
    return
def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    tarefas[ indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {nome_tarefa} Concluída!")
    return

def deletar_tarefas_completadas (tarefas):
    tarefas_deletadas = [tarefa["tarefa"] for tarefa in tarefas if tarefa["completada"]]
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    if tarefas_deletadas:
        print("Tarefas deletadas:")
        for nome in tarefas_deletadas:
            print(f"- {nome}")
    else:
        print("Nenhuma tarefa completada para deletar.")
    return

tarefas = []

##Condição de opções de entrada
while True: ##Sempre inicia o codigo com essa condição
    print("\nMenu do gerenciador de Lista de tarefas: ")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

## Para que o usuário escolha a opção do menu
    escolha = input("Digite a opção desejada: ")

## Condições
    if escolha == "1":
        nome_tarefa = input("Informe o nome da tarefa a ser adicionada: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefas = input ("Qual tarefa deseja atualizar? ")
        novo_nome = input ("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefas, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input ("Qual tarefa deseja completar? ")
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break ##programa finaliza ao digitar opção 6

print("Programa finalizado!")

