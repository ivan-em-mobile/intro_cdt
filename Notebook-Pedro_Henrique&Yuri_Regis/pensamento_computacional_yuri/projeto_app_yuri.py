'''

CRUD

Barbearia

Organizar e gerenciar clientes, agendamentos e serviços por meio das
 operações de cadastro, consulta, atualização e exclusão de dados.

'''


print('Bem-vindo!')

# input('Pressione Enter para continuar... ')
nome_cliente = input('Qual é o seu nome:')
print (f"bem vindo {nome_cliente}!")

nome_cliente = input ('Qual a sua turma:')

nome_conta = input ('Digite sua conta:')
print(f'{nome_conta} Correto agora entre com sua senha ')
input  ('Digite sua senha:')

acesso_menu = print ('Acesso Permitido')

nome_cliente = input ('O que deseja fazer?') ('1 - Acessar Agenda, 2 - consulta')
if nome_cliente == '1':
    print ('Acessar Agenda')       
elif nome_cliente == '2':
    print ('Consulta')

    while True:
        nome_cliente = input('Deseja acessar a agenda? (s/n): ')
        if nome_cliente.lower() == 's':
            print('Acessando a agenda...')
            break
        elif nome_cliente.lower() == 'n':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Por favor, digite "s" para sim ou "n" para não.')