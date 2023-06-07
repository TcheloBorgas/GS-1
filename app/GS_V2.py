#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
from datetime import datetime
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

class Produto:
    def __init__(self, nome, data_validade):
        self.nome = nome
        self.data_validade = data_validade

class Organizacao:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.produtos_recebidos = []

    def receber_produto(self, produto):
        self.produtos_recebidos.append(produto)

class Logistica:
    def __init__(self):
        self.produtos = []
        self.organizacoes = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def cadastrar_organizacao(self, organizacao):
        self.organizacoes.append(organizacao)

    def verificar_vencimentos(self):
        for produto in self.produtos:
            data_validade = datetime.strptime(produto.data_validade, '%d/%m/%Y')
            if data_validade.date() <= datetime.now().date():
                self.agendar_coleta(produto)
                print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
                print(f'O produto {produto.nome} está vencendo ou já venceu.')
                print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
                print('')

    def agendar_coleta(self, produto):
        print("Organizações disponíveis para coleta:")
        for i, organizacao in enumerate(self.organizacoes):
            print(f"{i+1}. {organizacao.nome}")

        escolha = int(input("Escolha o número correspondente à organização desejada: ")) - 1

        if escolha < 0 or escolha >= len(self.organizacoes):
            print("Escolha inválida.")
            return

        organizacao = self.organizacoes[escolha]
        organizacao.receber_produto(produto)

        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print(f"Coleta agendada: {produto.nome} para {organizacao.nome}")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

class InterfaceUsuario:
    def __init__(self, logistica):
        self.logistica = logistica

    def iniciar(self):
        while True:
            print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
            print("\n1 - Cadastrar produto")
            print("2 - Cadastrar organização")
            print("3 - Verificar vencimentos")
            print("4 - Mostrar empresas cadastradas")
            print("5 - Mostrar produtos da empresa")
            print("6 - Mostrar ONGs cadastradas e produtos recebidos")
            print("7 - Realizar entrega")
            print("8 - Gerar recibo")
            print("9 - Sair")
            print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
            print('')

            opcao = input("\nEscolha uma opção: ")

            if opcao == '1':
                self.cadastrar_produto()
            elif opcao == '2':
                self.cadastrar_organizacao()
            elif opcao == '3':
                self.logistica.verificar_vencimentos()
            elif opcao == '4':
                self.mostrar_empresas_cadastradas()
            elif opcao == '5':
                self.mostrar_produtos_empresa()
            elif opcao == '6':
                self.mostrar_ongs_cadastradas()
            elif opcao == '7':
                self.realizar_entrega()
            elif opcao == '8':
                self.gerar_recibo()
            elif opcao == '9':
                break
            else:
                print("Opção inválida!")
                print('')

    def cadastrar_produto(self):
        nome_produto = input("Nome do produto: ")
        data_validade = input("Data de validade (formato dd/mm/aaaa): ")
        produto = Produto(nome_produto, data_validade)
        self.logistica.adicionar_produto(produto)
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print(f"Produto {nome_produto} cadastrado com sucesso!")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

    def cadastrar_organizacao(self):
        nome = input("Nome da organização: ")
        endereco = input("Endereço da organização: ")
        organizacao = Organizacao(nome, endereco)
        self.logistica.cadastrar_organizacao(organizacao)
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print(f"Organização {nome} cadastrada com sucesso!")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

    def mostrar_empresas_cadastradas(self):
        if len(self.logistica.organizacoes) == 0:
            print("Nenhuma empresa cadastrada.")
        else:
            print("Empresas cadastradas:")
            for organizacao in self.logistica.organizacoes:
                print(f"Empresa: {organizacao.nome}")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

    def mostrar_produtos_empresa(self):
        nome_empresa = input("Digite o nome da empresa: ")
        empresa_encontrada = False

        for organizacao in self.logistica.organizacoes:
            if organizacao.nome == nome_empresa:
                empresa_encontrada = True
                if len(organizacao.produtos_recebidos) == 0:
                    print(f"A empresa {organizacao.nome} não cadastrou nenhum produto.")
                else:
                    print(f"Produtos cadastrados pela empresa {organizacao.nome}:")
                    for produto in organizacao.produtos_recebidos:
                        print(f"Produto: {produto.nome} (Data de Validade: {produto.data_validade})")
                break

        if not empresa_encontrada:
            print(f"Empresa {nome_empresa} não encontrada.")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

    def mostrar_ongs_cadastradas(self):
        if len(self.logistica.organizacoes) == 0:
            print("Nenhuma ONG cadastrada.")
        else:
            print("ONGs cadastradas e produtos recebidos:")
            for organizacao in self.logistica.organizacoes:
                if len(organizacao.produtos_recebidos) > 0:
                    print(f"ONG: {organizacao.nome}")
                    print("Produtos recebidos:")
                    for produto in organizacao.produtos_recebidos:
                        print(f"Produto: {produto.nome} (Data de Validade: {produto.data_validade})")
                    print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
            if all(len(ong.produtos_recebidos) == 0 for ong in self.logistica.organizacoes):
                print("Nenhuma ONG recebeu produtos.")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

    def realizar_entrega(self):
        nome_empresa = input("Digite o nome da empresa: ")
        taxa_entrega = input("A empresa deseja pagar a taxa de entrega? (S/N): ")
        empresa_encontrada = False

        for organizacao in self.logistica.organizacoes:
            if organizacao.nome == nome_empresa:
                empresa_encontrada = True
                if len(organizacao.produtos_recebidos) == 0:
                    print(f"A empresa {organizacao.nome} não cadastrou nenhum produto.")
                else:
                    produto_entrega = organizacao.produtos_recebidos[0]
                    organizacao.produtos_recebidos.remove(produto_entrega)

                    if taxa_entrega.upper() == "N":
                        print(f"A ONG {organizacao.nome} pagou a taxa de entrega.")
                    else:
                        print(f"A empresa {organizacao.nome} pagou a taxa de entrega.")

                    print(f"A empresa {organizacao.nome} realizou a entrega do produto {produto_entrega.nome} para a ONG.")
                break

        if not empresa_encontrada:
            print(f"Empresa {nome_empresa} não encontrada.")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

    def gerar_recibo(self):
        nome_empresa = input("Digite o nome da empresa: ")
        nome_ong = input("Digite o nome da ONG: ")
        produto_doado = input("Digite o nome do produto doado: ")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print(f"A empresa {nome_empresa} doou {produto_doado} para a ONG {nome_ong}.")
        print('━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━')
        print('')

#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━

#━━━━━━━━━❮Teste❯━━━━━━━━━
logistica = Logistica()
interface_usuario = InterfaceUsuario(logistica)
interface_usuario.iniciar()
#━━━━━━━━━━━❮◆❯━━━━━━━━━━━
