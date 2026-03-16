'''
DESCRIÇÃO DO PROJETO:
Este sistema é uma ferramenta de gestão para Salões de Beleza que permite realizar 
o ciclo completo de um agendamento (CRUD): cadastrar clientes, consultar a agenda, 
alterar serviços, cancelar registros e gerar relatórios financeiros simples.

Criação de um aplicativo para um salão de beleza, 
onde os clientes podem agendar serviços, 
escolher profissionais e 
visualizar seus agendamentos futuros. Baseado em CRUD (Create, Read, Update, Delete) 
para gerenciar os agendamentos e os profissionais disponíveis.

adicionalmente, o sistema inclui um controle de preços para cada serviço, permitindo que o administrador 
do salão possa atualizar os valores conforme necessário. Os clientes podem visualizar os 
preços antes de agendar um serviço, e o sistema calcula automaticamente 
o valor total a pagar com base nos serviços selecionados.

'''

# === SISTEMA DE GESTÃO DO SALÃO COM CONTROLE DE PREÇOS ===

# 1. Tabela de Preços Inicial
tabela_precos = {
    "Corte": 25.00,
    "Tintura": 15.00,
    "Completo": 35.00,
    "Sobrancelha": 10.00
}

# 2. Listas para armazenar os dados
nomes_clientes = []
servicos_clientes = []
valores_pagar = []

print('== Bem-vindo ao Sistema de Gestão Profissional ==')

while True:
    print("\n---------- MENU PRINCIPAL ----------")
    print("1. Agendar Cliente")
    print("2. Ver Agenda e Total do Dia")
    print("3. Ver Tabela de Preços")
    print("4. [ADM] Alterar Preço de Serviço")
    print("0. Sair")
    
    escolha = input("\nEscolha uma opção: ")

    if escolha == '1':
        nome = input("Nome do cliente: ")
        print(f"Serviços: {', '.join(tabela_precos.keys())}")
        servico = input("Qual o serviço? ").capitalize()

        if servico in tabela_precos:
            preco = tabela_precos[servico]
            print(f">> Valor tabelado: R$ {preco:.2f}")
        else:
            preco = float(input("Serviço não listado. Digite o valor manualmente: "))

        nomes_clientes.append(nome)
        servicos_clientes.append(servico)
        valores_pagar.append(preco)
        print(f">> Sucesso: {nome} agendado!")

    elif escolha == '2':
        print("\n--- Relatório do Dia ---")
        if not nomes_clientes:
            print("Nenhum agendamento para hoje.")
        else:
            total = 0
            for i in range(len(nomes_clientes)):
                print(f"{nomes_clientes[i]} - {servicos_clientes[i]}: R$ {valores_pagar[i]:.2f}")
                total += valores_pagar[i]
            print(f"\n>> TOTAL ACUMULADO: R$ {total:.2f}")

    elif escolha == '3':
        print("\n--- Tabela de Preços Atual ---")
        for s, p in tabela_precos.items():
            print(f"{s}: R$ {p:.2f}")

    elif escolha == '4':
        print("\n--- Área Administrativa: Alterar Preços ---")
        servico_alvo = input("Qual serviço deseja alterar o preço? ").capitalize()
        
        if servico_alvo in tabela_precos:
            novo_valor = float(input(f"O valor atual de {servico_alvo} é R$ {tabela_precos[servico_alvo]:.2f}. Digite o novo valor: "))
            # Atualizando o valor dentro do dicionário
            tabela_precos[servico_alvo] = novo_valor
            print(f">> Sucesso: Preço do serviço '{servico_alvo}' atualizado para R$ {novo_valor:.2f}!")
        else:
            print(">> Erro: Este serviço não existe na tabela.")

    elif escolha == '0':
        print("Encerrando sistema...")
        break
    else:
        print(">> Opção inválida!")