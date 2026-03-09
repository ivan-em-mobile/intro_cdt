print("Olá bem vindo ao meu sistema de coleta de dados!")
# print sempre será usado para exibir mensagens na tela
# input sempre será usado para coletar informações do usuário



input("Qual é o seu nome? ")
# input espera que aconteça algo na tela. 
# Espera o usuário pressionar Enter antes de fechar
# input() é usado para coletar informações do usuário, como nome, hobby, etc.



username = input("Qual é o seu @username? ")  
# variavel, recebe um input para fazer alguma coisa. (Coleta o nome do usuário)

## Faça a substituição das variaveis acima por outras que você quiser
#Exemplo:pessoal_nome; o_que_gosta; o_que_quer_fazer
## snake_case é uma convenção de nomenclatura onde as palavras são separadas por underscores (_)
#Exemplo Errado: pessoalNome; oQueGosta; oQueQuerFazer
#ou pn; oqgosta; oqqfazer

pessoal_nome = input("Como devo te chamar? ")

altura_pessoa = input("Qual é sua Altura? ")

gosto_pessoa = input("O que gosta de Fazer? ")

print("\n***O seu resultado foi salvo com sucesso!***\n")
print(f"Olá {pessoal_nome}, seu @username é {username} e sua altura é {altura_pessoa}m. Você gosta de {gosto_pessoa}.")
print("\n---Fim do sistema com sucesso!---\n")

# Variável para guardar o nome

# Variaveis elas tem tipos, ou seja, elas podem ser de texto, números, booleanos.
##string = texto
##int = número inteiro
##float = número decimal
##bool = verdadeiro ou falso
