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
print("modulo04 - Estruturas de dados - Tuplas \n")
print("modulo04 - Estruturas de dados - Dicionários \n")
print("modulo04 - Estruturas de dados - Conjuntos \n")
print("-" * 40)

# 1. TUPLA (Dados fixos e ordenados)
dias_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

# 2. CONJUNTO / SET (Excelente para buscas rápidas com o operador 'in')
dias_uteis = {"segunda", "terça", "quarta", "quinta", "sexta"}

# 3. DICIONÁRIO (Par Chave-Valor para associar o dia ao cardápio)
cardapio = {"domingo": "macarronada", "sábado": "feijoada", "dia_util": "lasanha"}

print("Bem-vindo ao programa de verificação de dias da semana! \n")
nome_usuario = input("Digite seu nome para começar: ")

# Tratamento do texto digitado pelo usuário
dia_escolhido = input("Digite um dia da semana: ").lower().strip()

# Validação usando a Tupla
if dia_escolhido in dias_semana:
    # Verifica se o dia está no Conjunto de dias úteis
    if dia_escolhido in dias_uteis:
        prato = cardapio["dia_util"]
    else:
        prato = cardapio[
            dia_escolhido
        ]  # Busca direto no Dicionário (domingo ou sábado)

    print(f"Olá, {nome_usuario}! O dia {dia_escolhido} é dia de {prato}.")

else:
    print(
        f'Olá, {nome_usuario}! "{dia_escolhido}" não é um dia da semana válido. Tente novamente!'
    )
