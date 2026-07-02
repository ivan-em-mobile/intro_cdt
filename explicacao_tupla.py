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
print("-" * 40)

# 1. TUPLA (Mantemos para validação, pois os dias são fixos)
dias_semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")

# 2. LISTA (Criada vazia. É mutável, logo vai receber dados novos)
historico_pesquisas = []

print("Bem-vindo ao programa de verificação de dias da semana! \n")
nome_usuario = input("Digite seu nome para começar: ")

# Loop simples de 2 tentativas para ver a lista a crescer
for i in range(2):
    dia_escolhido = input('\nDigite um dia da semana: \n').lower().strip()

    if dia_escolhido in dias_semana:
        # Adicionando o elemento à LISTA (Demonstração de mutabilidade)
        historico_pesquisas.append(dia_escolhido)

        if dia_escolhido == "domingo":
            print(f"Olá, {nome_usuario}! O dia {dia_escolhido} é dia de macarronada.")
        else:
            print(f"Olá, {nome_usuario}! O dia {dia_escolhido} é um dia de lasanha.")
    else:
        print(f'Olá, {nome_usuario}! "{dia_escolhido}" não é um dia válido.')

# Exibindo a nossa lista preenchida no final
print("\n" + "=" * 40)
print(f"Histórico de dias pesquisados (Sua Lista): {historico_pesquisas}")
print("=" * 40)
