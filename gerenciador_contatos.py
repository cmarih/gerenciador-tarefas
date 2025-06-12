contatos = []

def menu():
    print("\n ###################### MINHA AGENDA ##########################")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar como favorito")
    print("5. Ver favoritos")
    print("6. Apagar contato")
    print("7. Sair")

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    }
    contatos.append(contato)
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    if not contatos:
        print("Nenhum contato cadastrado.")
        return
    for i, contato in enumerate(contatos):
        fav = "❤️ " if contato["favorito"] else ""
        print(f"{i+1}. {contato['nome']} {fav} - {contato['telefone']} - {contato['email']}")

def editar_contato():
    listar_contatos()
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato a editar: ")) - 1
        if 0 <= indice < len(contatos):
            print("Deixe em branco para manter o valor atual.")
            nome = input(f"Novo nome ({contatos[indice]['nome']}): ") or contatos[indice]['nome']
            telefone = input(f"Novo telefone ({contatos[indice]['telefone']}): ") or contatos[indice]['telefone']
            email = input(f"Novo email ({contatos[indice]['email']}): ") or contatos[indice]['email']
            contatos[indice].update({"nome": nome, "telefone": telefone, "email": email})
            print("Contato atualizado com sucesso!")
        else:
            print("Contato inválido.")
    except ValueError:
        print("Entrada inválida.")

def marcar_favorito():
    listar_contatos()
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato para marcar/desmarcar como favorito: ")) - 1
        if 0 <= indice < len(contatos):
            contatos[indice]["favorito"] = not contatos[indice]["favorito"]
            status = "favorito" if contatos[indice]["favorito"] else "não favorito"
            print(f"Contato {contatos[indice]['nome']} agora é {status}.")
        else:
            print("Contato inválido.")
    except ValueError:
        print("Entrada inválida.")

def ver_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito.")
        return
    for c in favoritos:
        print(f"{c['nome']} ❤️  -  {c['telefone']}  -  {c['email']}")

def apagar_contato():
    listar_contatos()
    if not contatos:
        return
    try:
        indice = int(input("Digite o número do contato para apagar: ")) - 1
        if 0 <= indice < len(contatos):
            removido = contatos.pop(indice)
            print(f"Contato {removido['nome']} removido com sucesso.")
        else:
            print("Contato inválido.")
    except ValueError:
        print("Entrada inválida.")

# Loop principal
while True:
    menu()
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        listar_contatos()
    elif escolha == "3":
        editar_contato()
    elif escolha == "4":
        marcar_favorito()
    elif escolha == "5":
        ver_favoritos()
    elif escolha == "6":
        apagar_contato()
    elif escolha == "7":
        print("Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
