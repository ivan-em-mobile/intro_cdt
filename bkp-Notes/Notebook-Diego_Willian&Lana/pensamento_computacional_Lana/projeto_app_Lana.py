'''

CRUD

Padaria

O sistema da padaria deve permitir o acesso ao menu de produtos e promoções, onde o cliente pode selecionar 
os itens desejados e adiciona-los ao pedido. O sistema deve calcular o valor do pedido de acordo com o valor
do produto selecionado. O sistema deve permitir que o cliente possa finalizar o pedido, e escolher entre a
retirada no estabelecimento, e a entrega, escolher o metodo de pagamento, onde o cliente possa escolher entre 
dinheiro, pix, ou cartão de crédito ou débito. O sistema deve confirmar se o pedido chegou ao estabelecimento.

'''
print('Padaria Peter Pão - O melhor pão da cidade!🍞🍰')
 
nome_cliente = input('Digite seu nome: ')

print(f'Olá {nome_cliente}! Seja bem-vindo à Padaria Peter Pão!🍞🍰')

print('1 - fazer cadastro')
print('2 - Ver o cardápio')
print('3 - Meus Pedidos')
print('4 - Informações')
print('0 - Sair')


acesso_menu = input("\n O que você quer fazer?: ")

while True:
 if acesso_menu == "1":
   print("Fazer cadastro")
   
   email_cliente = input("Digite o email:")
   endereco_cliente = input("Digite o endereço:")
   telefone_cliente = input("Digite o telefone:")

   print("Cadastro realizado com sucesso!")
   #Código para fazer cadastro
   break

 elif acesso_menu == "2":
    print("Exibir cardápio")
    print("1 - Salgados")
    print("2 - Doces")
    print("3 - Bebidas")
    print("4 - Promoções")
    #Código para exibir cardápio
    break

 elif acesso_menu == "3":
    print("Meus Pedidos")
    #Código para exibir pedidos

 elif acesso_menu == "4":
    print("Informações")
    print("Endereço: Rua dos Pães, 123 - Centro")
    print("Telefone: (11) 1234-5678")
    print("Horário de funcionamento: Segunda a sábado, das 6h às 20h")
    #Código para exibir informações
    break

 elif acesso_menu == "0":
    print("Saindo do sistema. Até logo!")
    break