'''

CRUD

AÇAÍTERIA

descricao

'''

print("\n=== 🍷 Açaíataria 🍷 ===\n")

print("1. Cadastro 📝 ")
print("2. Cardápio 📋")
print("3. Pedidos 🛒")
print("4. Feedback 🗣️")
print("5. Ajuda ❓")
print("0. Sair 🚪")

while True:

    escolha_menu = input("\nEscolha uma opção: ")
    if escolha_menu == "1":

        print("Agendando cadastro...")
        nome_cliente = input("Digite o nome do cliente: ")
        telefone_cliente = input("Digite o telefone do cliente: ")
    
    elif escolha_menu == "0":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")

'''

CRUD
    
sistema de agendamento de aulas - meet

'''
print("sistema de agendamento de aulas - meet")

id_usuario = input(" Seja bem-vindo! Por favor, insira seu nome para continuar: ")

print("\n" + "_" * 15)

aluno_turma = input ('digite sua turma: (ex: A, B, C, D ): ')

email_usuario = input('Digite seu email: (nome.sobrenome@gmail.com) ')