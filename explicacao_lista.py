"""

As listas são coleções ordenadas de elementos. A sua principal característica é serem mutáveis,
o que significa que podemos adicionar, remover ou alterar os seus itens depois de a lista ter sido criada.
Sintaxe: Utiliza colchetes []


As tuplas são muito parecidas com as listas, mas com uma diferença crucial: elas são imutáveis.
Uma vez criada uma tupla, o seu conteúdo não pode ser modificado, garantindo a segurança dos dados.
Sintaxe: Utiliza parênteses ()


Os dicionários são coleções mutáveis que armazenam dados no formato de pares: chave-valor.
m vez de aceder aos dados por uma posição numérica (índice),
acedemos através de uma chave única (como uma palavra e o seu significado num dicionário real).
Sintaxe: Utiliza chaves {} e dois pontos : para separar a chave do valor.


"""

print("\nmodulo04 - Estruturas de dados - Listas \n")
print("🍒" * 40)
print("Bem-vindo ao sistema de Lista de Frutas Favoritas \n")
print("🍒" * 40)

# 1. LISTA (Coleção ordenada e mutável)
frutas_favoritas = [
    "banana",
    "morango",
    "abacaxi",
    "maça",
    "abacate",
    "uva",
    "mango",
    "kiwi",
    "pessego",
    "cereja",
    "pitaya",
]

# Entrada de dados do utilizador
fruta_escolhida = input("Digite o nome da fruta que deseja colocar: ").lower().strip()

# ESTRUTURA CONDICIONAL: Verificando se a fruta já existe na lista
if fruta_escolhida in frutas_favoritas:
    # Se a fruta JÁ ESTIVER na lista, executa este bloco
    print(f'\nAviso: A fruta "{fruta_escolhida}" já está na sua lista de favoritas!')
else:
    # Se a fruta NÃO ESTIVER na lista, executa este bloco e adiciona
    frutas_favoritas.append(fruta_escolhida)
    print(f'\nFruta "{fruta_escolhida}" adicionada com sucesso!')

# Exibindo a lista final
print(f"A lista atualizada de frutas favoritas é: {frutas_favoritas}")
