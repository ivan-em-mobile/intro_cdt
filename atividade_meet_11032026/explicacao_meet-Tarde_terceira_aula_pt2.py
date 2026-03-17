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
e estruturas de dados (listas e tuplas).



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
 
###Calculadora Alta Dificuldade

historico_detalhado = []

while True:
    print("\n==============================")
    print("    \nCalculadora - Python")
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
