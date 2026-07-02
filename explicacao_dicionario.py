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

print("\nmodulo04 - Estruturas de dados - Dicionários \n")
print("-" * 40)

# 1. DICIONÁRIO (Coleção de itens em pares de chave-valor)
cardapio_da_semana = {
    "segunda-feira": "Arroz com feijão",
    "terça-feira": "Panquecas",
    "quarta-feira": "Feijoada",
    "quinta-feira": "Sopa de legumes",
    "sexta-feira": "Peixe grelhado",
    "sábado": "Pizza",
    "domingo": "Macarrão",
}

# Demonstrando a MUTABILIDADE: Vamos alterar o prato de quarta-feira!
cardapio_da_semana["quarta-feira"] = "Feijoada Especial com Couve"

print("Bem-vindo ao programa de verificação de cardápio! \n")

# .strip() remove espaços acidentais que o usuário possa digitar
dia_escolhido = input("Digite um dia da semana para saber o menu: ").lower().strip()

# Verificando se a CHAVE existe dentro do dicionário
if dia_escolhido in cardapio_da_semana:
    # Acedendo ao VALOR através da CHAVE
    comida = cardapio_da_semana[dia_escolhido]
    print(f"No {dia_escolhido}, o prato do dia é: {comida}!")
else:
    print(
        f'Desculpe, "{dia_escolhido}" não é um dia válido no nosso cardápio. Tente usar o hífen (ex: segunda-feira).'
    )
