print('\n== Bem-vindo ao sistema de gerenciamento do Salão de Beleza! ===\n')

# Inicializamos as variáveis com valores vazios (o nosso "espaço" na memória)
nome_cliente = "Ninguém"
telefone_cliente = "0000-0000"
servico_cliente = "Nenhum"

while True:
    print("\n1. Agendar Cliente")
    print("2. Ver Agenda")
    print("3. Mudar Serviço")
    print("4. Cancelar Agendamento")
    print("5. Relatório de Serviços")
    print("0. Sair")

    escolha_menu = input("\nEscolha uma opção: ")

    if escolha_menu == '1':
        print("\n--- Agendando cliente ---")
        nome_cliente = input("Digite o nome do cliente: ")
        telefone_cliente = input("Digite o telefone do cliente: ")
        servico_cliente = input("Digite o serviço (Corte/Barba): ")
        print(">> Cliente agendado com sucesso!")

    elif escolha_menu == '2':
        print("\n--- Agenda Atual ---")
        # Exibimos o que está guardado nas variáveis
        print(f"Cliente: {nome_cliente}")
        print(f"Telefone: {telefone_cliente}")
        print(f"Serviço: {servico_cliente}")

    elif escolha_menu == '3':
        print("\n--- Mudar Serviço ---")
        # Atualizamos apenas a variável do serviço
        novo_servico = input(f"O serviço atual de {nome_cliente} é {servico_cliente}. Digite o novo: ")
        servico_cliente = novo_servico
        print(">> Serviço atualizado!")

    elif escolha_menu == '4':
        print("\n--- Cancelar Agendamento ---")
        # "Apagamos" os dados voltando ao estado inicial
        nome_cliente = "Ninguém"
        telefone_cliente = "0000-0000"
        servico_cliente = "Nenhum"
        print(">> Agendamento cancelado e sistema limpo.")

    elif escolha_menu == '5':
        print("\n--- Relatório de Serviços ---")
        # Uma exibição simples apenas do serviço atual
        print(f"O serviço agendado no momento é: {servico_cliente}")

    elif escolha_menu == '0':
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")