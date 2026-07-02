'''

Data de entrega de atividade, criando o APP: 25-03-2026, Ao final da aula.
A atividade deve estar no repositório do Lider com os devidos FORKS e PULL REQUESTS,
para que seja possível a correção e avaliação.

Em aulas anteriores, vimos como criar um sistema de agendamento de aulas utilizando o Google Meet.
Agora, vamos criar um sistema de agendamento de aulas utilizando o Google Meet, 
mas com uma interface de texto simples, onde o usuário pode escolher opções 
para agendar aulas, ver a agenda, mudar aulas, cancelar agendamentos e gerar relatórios de aulas.

Nesta aula vamos focar na estrutura básica do código, utilizando condicionais 
(if, elif, else) para criar um menu de opções para o usuário.

E na sequencia temos uma pergunta para vocês, onde devem pensar em quais variáveis seriam 
necessárias para criar um sistema de agendamento de aulas,

##PERGUNTA
#Caso precise criar uma sistemas com nome e sobrenome dos jovens; turma; e-mail (nome.sobrenome@gmail.com)
#Quais as variaveis que preciso criar?



'''
 
print('Sistema de Agendamento de Aulas - Meet')

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
        # Aqui temos nossa primeira entrega de atividade, onde o aluno deve 
        # criar o código para exibir a agenda de aulas agendadas,

        print('\n::Programação Python::\n')
# print('')
        print('Turma A - Segunda e Quarta')
        print('Turma A 08:00 - 12:00')
        print('')
        print('Turma A 10:00 - 12:00')      
    
    elif acesso_menu == '0':
        print("Saindo do sistema. Até logo!")
        break