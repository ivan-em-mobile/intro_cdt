'''
CRUD

print('Sistema de Agendamento de Aulas - Meet')


print("\n" + "__"*14)


# id_usuario = input('Seja bem-vindo! Digite seu nome para continuar: ')
nome_jovem=input('Seja bem-vindo! Digite seu nome para continuar: ')

# aluno_turma = input('Digite sua turma: ("a", "b", "c", "d"): ')
turma_jovem = input('Digite sua turma: ("a", "b", "c", "d"): ')

# email_usuario = input('Digite seu e-mail ("nome.sobrenome@gmail.com"): ')
email_jovem = input('Digite seu e-mail ("nome.sobrenome@gmail.com"): ')


print(f"Bem-vindo, {nome_jovem}!")
print("\n" + "__"*4 + " Sistema de Agendamento de Aulas - Meet" + "\n" + "__"*7)
      

print("1. Agendar Aula")
print("2. Ver Agenda")
print("3. Mudar Aula")
print("4. Cancelar Agendamento")
print("5. Relatório de Aulas")
print("0. Sair")

while True:

    acesso_menu = input("\n O você quer precisa fazer?: ")

    if acesso_menu == "1":
        nome_aluno = input("Digite o nome do aluno: ")

        turma_aluno = input("Digite a turma do aluno: ")

        email_aluno = input("Digite o e-mail do aluno: ")

        telefone_aluno = input("Digite o telefone do aluno: ")

        inicio_aula = input("Digite o horário de início da aula (HH:MM): ")

        tema_aula = input("Digite o tema da aula: ")

        print("Confirmando agendamento...")

        print("Aula agendada com sucesso!")
        # Código para agendar aula

    elif acesso_menu == "2":
        print("Exibindo agenda...")

       
    # Código para exibir agenda

    elif acesso_menu == "0":
        print("Saindo do sistema. Até logo!")
        break
    # exemplo de indentação correta para o código acima:

print('\nSistema de Agendamento de Aulas - Meet\n')
# print('')
print(':: Programação Python::\n')
# print('')
print('Turma A Segunda e Quarta')
print('Turma A 08:00 - 12:00\n')
# print('')
print('Turma A 10:00 - 12:00')

'''

print('\n Calculadora simples - Python Vocação\n')

numb_hum = input('Digite o primeiro número:')
numb_dois = input('Digite o segundo número:')

operar_numb = input('Escolha a operação: 1 -> +, 2 -> -, 3 -> *, 4 -> /')

if operar_numb =='4':
    result = int(numb_hum) / int(numb_dois)
    print(f'O resultado é: {result}')

elif operar_numb == '3':
    result = int(numb_hum) * int(numb_dois)
    print(f'O resultado é: {result}')

# Lição de Casa: Faça as operações de soma e subtração, utilizando o mesmo modelo acima.




else:
    print('Numero não divido por zero.')

# result = numb_hum + numb_dois #Jeito errado de fazer a conta, 
## pois o input retorna uma string e não um número. 
## O resultado seria a concatenação dos números, e não a soma.

# result = int(numb_hum) + int(numb_dois) #Jeito certo de fazer a conta, 
## convertendo as strings para inteiros antes de somar.

# print(f'O resultado é: {result}')





























































'''
print("Sistema de Agendamento de Aulas - Meet")

# O código acima é um exemplo de um sistema de agendamento # para um salão de beleza. Ele apresenta um menu com opções
# para agendar clientes, ver a agenda, mudar serviços, # cancelar agendamentos e gerar relatórios de serviços.
# O usuário pode escolher uma opção e o sistema irá executar #  a ação correspondente. O código é escrito em Python 3 e
# não utiliza bibliotecas externas, apenas recursos # básicos da linguagem.

nome_usuario = input("Digite seu nome para continuar: ")

# Uma variavel chamada 'nome_usuario' armazena o nome do usuário que foi digitado pelo input.
# O input é uma função que permite ao usuário inserir dados no programa.


aluno_turma = input('Digite sua turma: ("a", "b", "c", "d"): ')


email_usuario = input('Digite seu e-mail ("nome.sobrenome@gmail.com"): ')


print(f"Bem-vindo, {nome_usuario}!")
print("\n === Sistema de Agendamento de Aulas - Meet === \n")

print("1. Agendar Aula")
print("2. Ver Agenda")
print("3. Mudar Aula")
print("4. Cancelar Agendamento")
print("5. Relatório de Aulas")
print("0. Sair")


while True:

    acesso_menu = input("\n O que precisa fazer?: ")

    if acesso_menu == "1":
        print("Agendando aula...")

        nome_aluno = input("Digite o nome do aluno: ")

        turma_aluno = input("Digite a turma do aluno: ")

        email_aluno = input("Digite o e-mail do aluno: ")

        telefone_aluno = input("Digite o telefone do aluno: ")

        inicio_aula = input("Digite o horário de início da aula (HH:MM): ")

        tema_aula = input("Digite o tema da aula: ")

        print("Confirmando agendamento...")

        print("Aula agendada com sucesso!")
        # Código para agendar aula

    elif acesso_menu == "2":
        print("Exibindo agenda...")
    # Código para exibir agenda

    elif acesso_menu == "0":
        print("Saindo do sistema. Até logo!")
        break

    # exemplo de indentação correta para o código acima:

    else:
        print("Opção inválida. Por favor, tente novamente.")


'''











##PERGUNTA
# Caso precise criar uma sistemas com nome e 
# sobrenome dos jovens; turma; e-mail (nome.sobrenome@gmail.com)

# Quais as variaveis que preciso criar?