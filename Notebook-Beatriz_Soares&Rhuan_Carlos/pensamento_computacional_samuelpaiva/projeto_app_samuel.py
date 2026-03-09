'''


CRUD

Hamburgueria 

fazer um sistema de cardapio, onde o usuário possa cadastrar, visualizar, atualizar e deletar itens do cardapio e fazer um sistema de
cadastrar a conta do google, e fazer um sistema de login, onde o usuário possa acessar a conta do google e visualizar e fazer um sistema de
delivery, onde o cliente rastreia o pedido
'''
print('\n=== HAMBURGUERIA MSD ===')
print('1.cadastrar conta do google')
print('2. selecionar itens do cardápio')
print('3. finalizar pedido')
print('4. rastrear pedido')
print('5. seu pedido foi aceito e está sendo preparado')
print('6. seu pedido saiu para entrega')
print('7. seu pedido foi entregue')
print('0. sair')



while True:# loop principal do sistema, verdadeiro para   escolha = input('\nEscolha uma opção: ') 
#manter o programa rodando até o usuário escolher sair

 escolha = input('\nEscolha uma opção: ')#variavel para armazenar a escolha do usuário

if escolha == '1':
    print('cadastro de conta do google...')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    print('Conta cadastrada com sucesso!')

elif escolha == '2':
    print('selecionar itens do cardápio')
    print('1. hambúrguer')
    print('2. batata frita')
    print('3. refrigerante')
    item = input('Digite o número do item que deseja: ')
    print('Item selecionado com sucesso!')

elif escolha == '3':
    print('Pedido finalizado com sucesso!')

elif escolha == '4':
    print('seu pedido está sendo preparado...')
 
elif escolha == '5':
    print('Seu pedido saiu para entrega!')

elif escolha == '6':
        print('Seu pedido foi entregue!')

elif escolha == '0':
    print('Saindo do sistema até logo...')
    
    
else:
    print("Opção inválida. Por favor, tente novamente.")
   
       
















































