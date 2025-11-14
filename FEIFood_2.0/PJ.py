MENU = {
    '1': 'Cadastrar usuário',
    '2': 'Login',
    '3': 'Adicionar pedido',
    '4': 'Buscar pedido',
    '5': 'Listar pedidos',
    '6': 'Atualizar pedido',
    '7': 'Remover pedido',
    '8': 'Sair'
}

def mostrar_menu():
    print("\nMenu principal:")
    for opcao, valor in MENU.items():
        print(opcao + " - " + valor)
    print()

def cadastrar_usuario():
    nome = input("Nome do usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{email},{senha}\n")
    print("Usuário cadastrado com sucesso no Banco de Dados FEIFood.\n")

def login():
    email = input("Email: ")
    senha = input("Senha: ")
    usuario_logado = None

    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            nome, e, s = linha.strip().split(",")
            if email == e and senha == s:
                usuario_logado = nome
                break

    if usuario_logado:
        print(f"Bem-vindo(a), {usuario_logado}!\n")
        menu_pedidos(usuario_logado)
    else:
        print("Email ou senha incorretos.\n")

def adicionar_pedido(usuario):
    alimento = input("Nome do alimento: ")
    quantidade = input("Quantidade: ")
    avaliacao = "Sem avaliação"

    with open("pedidos.txt", "a") as arquivo:
        arquivo.write(f"{usuario},{alimento},{quantidade},{avaliacao}\n")

    print("Pedido adicionado com sucesso.\n")

def buscar_pedido(usuario):
    nome_busca = input("Digite o nome do alimento: ")
    encontrado = False

    with open("pedidos.txt", "r") as arquivo:
        for linha in arquivo:
            nome_user, alimento, qtd, avaliacao = linha.strip().split(",")
            if nome_user == usuario and alimento.lower() == nome_busca.lower():
                print(f"\nPedido encontrado:")
                print(f"Alimento: {alimento}")
                print(f"Quantidade: {qtd}")
                print(f"Avaliação: {avaliacao}\n")
                encontrado = True
                break

    if not encontrado:
        print("Nenhum pedido encontrado.\n")

def listar_pedidos(usuario):
    print("\nSeus pedidos no FEIFood:")
    with open("pedidos.txt", "r") as arquivo:
        for linha in arquivo:
            nome_user, alimento, qtd, avaliacao = linha.strip().split(",")
            if nome_user == usuario:
                print(f"{alimento} - {qtd} unidade(s) - {avaliacao}")
    print()

def atualizar_pedido(usuario):
    nome_busca = input("Digite o nome do alimento que deseja atualizar: ")
    novo_conteudo = ""
    encontrado = False

    with open("pedidos.txt", "r") as arquivo:
        for linha in arquivo:
            nome_user, alimento, qtd, avaliacao = linha.strip().split(",")
            if nome_user == usuario and alimento.lower() == nome_busca.lower():
                print("Pedido encontrado. Insira as novas informações:")
                novo_alimento = input("Novo alimento: ")
                nova_qtd = input("Nova quantidade: ")
                nova_avaliacao = input("Nova avaliação: ")
                novo_conteudo += f"{usuario},{novo_alimento},{nova_qtd},{nova_avaliacao}\n"
                encontrado = True
            else:
                novo_conteudo += linha

    with open("pedidos.txt", "w") as arquivo:
        arquivo.write(novo_conteudo)

    if encontrado:
        print("Pedido atualizado com sucesso.\n")
    else:
        print("Pedido não encontrado.\n")

def remover_pedido(usuario):
    nome_busca = input("Digite o nome do alimento a ser removido: ")
    novo_conteudo = ""
    encontrado = False

    with open("pedidos.txt", "r") as arquivo:
        for linha in arquivo:
            nome_user, alimento, qtd, avaliacao = linha.strip().split(",")
            if nome_user == usuario and alimento.lower() == nome_busca.lower():
                encontrado = True
            else:
                novo_conteudo += linha

    with open("pedidos.txt", "w") as arquivo:
        arquivo.write(novo_conteudo)

    if encontrado:
        print("Pedido removido com sucesso.\n")
    else:
        print("Pedido não encontrado.\n")

def menu_pedidos(usuario):
    while True:
        print(f"\nUsuário: {usuario}")
        print("=== Menu de Pedidos FEIFood===")
        print("3 - Adicionar pedido")
        print("4 - Buscar pedido")
        print("5 - Listar pedidos")
        print("6 - Atualizar pedido")
        print("7 - Remover pedido")
        print("8 - Sair")
        print()

        escolha = input("Escolha uma opção: ")

        if escolha == '3':
            adicionar_pedido(usuario)
        elif escolha == '4':
            buscar_pedido(usuario)
        elif escolha == '5':
            listar_pedidos(usuario)
        elif escolha == '6':
            atualizar_pedido(usuario)
        elif escolha == '7':
            remover_pedido(usuario)
        elif escolha == '8':
            print("Saindo do menu de pedidos.\n")
            break
        else:
            print("Opção inválida.\n")

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        cadastrar_usuario()
    elif escolha == '2':
        login()
    elif escolha == '8':
        print("Encerrando o sistema FEIFood. Até logo!")
        break
    else:
        print("Opção inválida.\n")
