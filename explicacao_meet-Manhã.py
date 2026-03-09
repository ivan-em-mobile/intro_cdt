'''
25-03

print('Sistema de Agendamento de Aulas - Meet')

# O código acima é um exemplo de um sistema de agendamento # para um salão de beleza. Ele apresenta um menu com opções 
# para agendar clientes, ver a agenda, mudar serviços, # cancelar agendamentos e gerar relatórios de serviços. 
# O usuário pode escolher uma opção e o sistema irá executar #  a ação correspondente. O código é escrito em Python 3 e 
# não utiliza bibliotecas externas, apenas recursos # básicos da linguagem.

nome_usuario = input('Digite seu nome para continuar: ')

#Uma variavel chamada 'nome_usuario' armazena o nome do usuário que foi digitado pelo input. 
# O input é uma função que permite ao usuário inserir dados no programa.


aluno_turma = input('Digite sua turma: ("a", "b", "c", "d"): ')




email_usuario = input('Digite seu e-mail ("nome.sobrenome@gmail.com"): ' )




print(f'Bem-vindo, {nome_usuario}!')
print('\n === Sistema de Agendamento de Aulas - Meet === \n')

print("1. Agendar Aula")
print("2. Ver Agenda")
print("3. Mudar Aula")
print("4. Cancelar Agendamento")
print("5. Relatório de Aulas")
print("0. Sair")


while True:

    acesso_menu = input("\n O que precisa fazer?: ")

    if acesso_menu == '1':
        print("Agendando aula...")

        nome_aluno = input("Digite o nome do aluno: ")

        turma_aluno = input("Digite a turma do aluno: ")

        email_aluno = input("Digite o e-mail do aluno: ")

        telefone_aluno = input("Digite o telefone do aluno: ")

        inicio_aula = input("Digite o horário de início da aula (HH:MM): ")

        tema_aula = input("Digite o tema da aula: ")

        print('Confirmando agendamento...')

        print('Aula agendada com sucesso!')
        # Código para agendar aula


    elif acesso_menu == '2':
        print("Exibindo agenda...")
        # Código para exibir agenda
        # 
        # 
        # 
        # 
        # 
        #         
    
    elif acesso_menu == '0':
        print("Saindo do sistema. Até logo!")
        break

#exemplo de indentação correta para o código acima:

    else:
        print("Opção inválida. Por favor, tente novamente.")

    if escolha_menu == '1':

        print("Agendando aula...")

        nome_aluno = input("Digite o nome do aluno: ")

        turma_aluno = input("Digite a turma do aluno: ")

        email_aluno = input("Digite o e-mail do aluno: ")
        # Código para agendar aula


    elif escolha_menu == '0':
    
        print("Saindo do sistema. Até logo!")
        break
        
            
        else:
        print("Opção inválida. Por favor, tente novamente.")

print('\n::Programação Python::\n')
# print('')
print('Turma A - Segunda e Quarta')
print('Turma A 08:00 - 12:00')
print('')
print('Turma A 10:00 - 12:00')

'''
 
##PERGUNTA
#Caso precise criar uma sistemas com nome e sobrenome dos jovens; turma; e-mail (nome.sobrenome@gmail.com)
#Quais as variaveis que preciso criar?


print('\nCalculadora simples - Python')

# num_um = float(input('Digite o primeiro número:'))
num_um = input('Digite o primeiro número: ')

# num_dois = float(input('Digite o segundo número:'))
num_dois = input('Digite o segundo número: ')

operacao = input('Escolha a operação: 1-> +, 2-> -, 3-> *, 4-> /')

# result = int(num_um) + int(num_dois)  
#tratamento de resultado, convertendo as entradas para 
##inteiros antes de realizar a operação de soma.

if operacao == '1':
    result = int(num_um) + int(num_dois) 
    print(f'O resultado da soma é: {result}')

elif operacao == '2':
    result = int(num_um) - int(num_dois)  # Subtração
    print(f'O resultado da subtração é: {result}')

elif operacao == '3':
    result = int(num_um) * int(num_dois) # Multiplicação
    print(f'O resultado da multiplicação é: {result}')
else:
    print("Número não é válido, tente novamente!")


# result = int(num_um) / int(num_dois)  #1 divisão
# result = int(num_um) * int(num_dois)  #2 multiplicação
# result = int(num_um) + int(num_dois)  #3 soma
# result = int(num_um) - int(num_dois)  #4 subtração


print(f'O resultado é: {result}')





