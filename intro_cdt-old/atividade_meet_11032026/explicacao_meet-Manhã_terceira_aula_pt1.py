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

>Nessa aula, a calculadora deixa de ser apenas um exemplo de aplicação de operações matemáticas, 
e passa a ser um exemplo de aplicação de estruturas de controle de fluxo (condicionais) 
e estruturas de dados (listas).

E temos na sequencia uma pergunta para vocês, onde devem pensar em quais as possiveis formas 
de criar ou usar uma calculadora em python.


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



'''
 
###Calculadora Média Dificuldade

historico = []

while True:
    print("\n--- Calculadora simples - Python ---")
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
