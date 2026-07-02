'''

>>Data de entrega de atividade, criando o APP: 25-03-2026, Ao final da aula.
A atividade deve estar no repositório do Lider com os devidos FORKS e PULL REQUESTS,
para que seja possível a correção e avaliação.

>Em aulas anteriores, vimos como criar um sistema de agendamento de aulas utilizando o Google Meet.
Agora, vamos criar um sistema de agendamento de aulas utilizando o Google Meet, 
mas com uma interface de texto simples, onde o usuário pode escolher opções 
para agendar aulas, ver a agenda, mudar aulas, cancelar agendamentos e gerar relatórios de aulas.

>Nesta aula vamos focar na estrutura básica do código, utilizando condicionais 
(if, elif, else) para criar um menu de opções para o usuário.

>E na sequencia temos uma pergunta para vocês, onde devem pensar em quais variáveis seriam 
necessárias para criar um sistema de agendamento de aulas,

##PERGUNTA
#Caso precise criar uma sistemas com nome e sobrenome dos jovens; turma; e-mail (nome.sobrenome@gmail.com)
#Quais as variaveis que preciso criar?

>>Essa Aula será dividida em duas partes para as calculadoras, onde a primeira será uma calculadora simples, 
utilizando apenas as operações básicas de soma, subtração, multiplicação e divisão. 
E a segunda parte será uma calculadora mais complexa, onde o usuário poderá escolher entre operações básicas 
e porcentagem, além de ter um histórico de cálculos realizados.

>Vimos a diferença entre listas e tuplas, onde as listas são mutáveis e as tuplas são imutáveis.
As listas permitem adicionar, remover e modificar elementos, enquanto as tuplas não permitem essas
operações após a criação. As tuplas são mais eficientes em termos de memória e desempenho, 
enquanto as listas são mais flexíveis para manipulação de dados.



'''
 
print('\nCalculadora - Python')
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
