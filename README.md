# Documentação do Código: Sistema de Logística para Produtos e Organizações


 Este programa implementa um sistema de logística básico para lidar com produtos e organizações. O sistema mantém uma lista de produtos, cada um com um nome e uma data de validade, e uma lista de organizações, cada uma com um nome e um endereço. O sistema é capaz de agendar a coleta de produtos que estão vencendo ou já venceram.

# Classes
## O programa contém as seguintes classes:


Produto: Representa um produto, que possui um nome e uma data de validade.
Organizacao: Representa uma organização, que tem um nome, um endereço e uma lista de produtos recebidos.
Logistica: Gerencia a logística, mantendo listas de produtos e organizações e proporcionando funcionalidades como adicionar produtos, registrar organizações e verificar a validade dos produtos.
InterfaceUsuario: Fornece uma interface de usuário simples para interagir com o sistema de logística.
# Funcionamento
## Aqui está um breve resumo de como o programa funciona:

A InterfaceUsuario pede ao usuário que escolha uma opção: adicionar um produto, registrar uma organização, verificar os vencimentos dos produtos, ou sair do programa.
Se o usuário optar por adicionar um produto, ele deverá fornecer o nome e a data de validade do produto. O produto é então adicionado à lista de produtos na classe Logistica.
Se o usuário optar por registrar uma organização, ele deverá fornecer o nome e o endereço da organização. A organização é então adicionada à lista de organizações na classe Logistica.
Se o usuário optar por verificar os vencimentos dos produtos, o sistema verifica a data de validade de cada produto na lista de produtos. Se um produto está vencendo ou já venceu, ele é enviado para a primeira organização na lista de organizações e uma mensagem é impressa indicando que a coleta do produto foi agendada.
O usuário pode continuar escolhendo opções até que ele opte por sair do programa.


# Como executar
Para executar este programa, você só precisa executá-lo em um ambiente que suporte Python. Quando o programa começa a ser executado, ele exibe um menu de opções e você pode interagir com o programa selecionando as opções e fornecendo as informações solicitadas.