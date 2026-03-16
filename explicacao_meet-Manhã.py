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


##PERGUNTA
#Caso precise criar uma sistemas com nome e sobrenome dos jovens; turma; e-mail (nome.sobrenome@gmail.com)
#Quais as variaveis que preciso criar?


print('\nCalculadora simples - Python')
num_um = input('Digite o primeiro número: ')
num_dois = input('Digite o segundo número (Lembrando que não pode ser zero para divisão): ')
operacao = input('Escolha a operação: 1-> +, 2-> -, 3-> *, 4-> /')


if operacao == '1':
    result = int(num_um) + int(num_dois)  #Soma
    print(f'O resultado da soma é: {result}')

elif operacao == '2':
    result = int(num_um) - int(num_dois)  # Subtração
    print(f'O resultado da subtração é: {result}')

elif operacao == '3':
    result = int(num_um) * int(num_dois) # Multiplicação
    print(f'O resultado da multiplicação é: {result}')
#Crie o código para realizar a divisão, 
elif operacao == '4':
    # if int(num_dois) != 0:
        result = int(num_um) / int(num_dois) # Divisão
        print(f'O resultado da divisão é: {result}')
    # else:
    #     print("Erro: Divisão por zero não é permitida.") ##lembrando de tratar o caso de divisão por zero.
else:
    print("Número não é válido, tente novamente!")



'''
 
##PERGUNTA
#Quais as possiveis formas de criar ou usar uma calculadora em python?

###LISTAS

frutas = ['Maçã', 'Banana', 'Laranja', 'Abacaxi']
print(frutas[0])  # Acessa o primeiro elemento da lista (Maçã)

frutas.append('Manga')  # Adiciona 'Manga' ao final da lista
frutas.append('Romã') # Adiciona 'Romã' ao final da lista
frutas.append('Melão') # Adiciona 'Melão' ao final da lista

print(frutas)  # Exibe a lista atualizada



###TUPLAS

cores = ('Azul', 'Vermelho', 'Amarelo', 'Verde', 'Preto')

#Criarndo um exemplo

##Carro eletrico, não modificar o contador de tempo, Velocidade.

##Cemtimetros, Metros, Milimitros.

##Escala de Medidas - 1:100, 1:50, 1:25, 1:10, 1:5, 1:2, 1:1, 2:1, 5:1, 10:1, 25:1, 50:1, 100:1



###Calculadora Média Dificuldade

historico = []

while True:
    print("\n--- Calculadora Média ---")
    print("1. Operações Básicas (+, -, *, /)")
    print("2. Calcular Porcentagem (X% de Y)")
    print("3. Ver Histórico")
    print("0. Sair")
    
    opcao = input("Escolha: ")

    if opcao == '1':
        n1 = float(input("Número 1: "))
        n2 = float(input("Número 2: "))
        op = input("Operação (+, -, *, /): ")
        
        if op == '+': res = n1 + n2
        elif op == '-': res = n1 - n2
        elif op == '*': res = n1 * n2
        elif op == '/': res = n1 / n2 if n2 != 0 else "Erro"
        
        calc = f"{n1} {op} {n2} = {res}"
        print(calc)
        historico.append(calc)

    elif opcao == '2':
        porcentagem = float(input("Porcentagem (%): "))
        valor = float(input("Sobre o valor: "))
        res = (porcentagem / 100) * valor
        calc = f"{porcentagem}% de {valor} = {res}"
        print(calc)
        historico.append(calc)

    elif opcao == '3':
        print("\n-- Histórico --")
        for item in historico:
            print(item)
            
    elif opcao == '0': break


###Calculadora Alta Dificuldade

historico_detalhado = []

while True:
    print("\n==============================")
    print("    CALCULADORA COMPLEXA")
    print("==============================")
    print("1. Calcular (Inteiro/Decimal)")
    print("2. Porcentagem")
    print("3. Ver Histórico Detalhado")
    print("0. Sair")
    
    escolha = input("\nOpção: ")

    if escolha == '1':
        # Entrada de dados
        v1 = input("Primeiro número: ")
        v2 = input("Segundo número: ")
        
        # Lógica para converter (verifica se há ponto para ser float ou int)
        n1 = float(v1) if '.' in v1 else int(v1)
        n2 = float(v2) if '.' in v2 else int(v2)
        
        print("Operações: [1]+ [2]- [3]* [4]/")
        op_mat = input("Operação: ")
        
        if op_mat == '1': simbola, res = "+", n1 + n2
        elif op_mat == '2': simbola, res = "-", n1 - n2
        elif op_mat == '3': simbola, res = "*", n1 * n2
        elif op_mat == '4': 
            simbola = "/"
            res = n1 / n2 if n2 != 0 else "Indeterminado"
        
        registro = f"Cálculo: {n1} {simbola} {n2} | Resultado: {res} | Tipo: {type(res).__name__}"
        print(f"\n>> {registro}")
        historico_detalhado.append(registro)

    elif escolha == '2':
        # Ex: 10% de aumento em 100 reais
        v_porcent = float(input("Valor da porcentagem: "))
        v_total = float(input("Valor base: "))
        
        print("1. Calcular apenas a parte (X% de Y)")
        print("2. Acréscimo (Y + X%)")
        print("3. Desconto (Y - X%)")
        tipo_p = input("Opção: ")
        
        parte = (v_porcent / 100) * v_total
        
        if tipo_p == '1':
            res_p = parte
            msg = f"{v_porcent}% de {v_total} é {res_p}"
        elif tipo_p == '2':
            res_p = v_total + parte
            msg = f"{v_total} com acréscimo de {v_porcent}% = {res_p}"
        elif tipo_p == '3':
            res_p = v_total - parte
            msg = f"{v_total} com desconto de {v_porcent}% = {res_p}"
            
        print(f"\n>> {msg}")
        historico_detalhado.append(msg)

    elif escolha == '3':
        print("\n--- HISTÓRICO DE OPERAÇÕES ---")
        if not historico_detalhado:
            print("Nenhum cálculo realizado.")
        else:
            for i, item in enumerate(historico_detalhado, 1):
                print(f"{i}. {item}")

    elif escolha == '0':
        print("Encerrando... Até à próxima!")
        break