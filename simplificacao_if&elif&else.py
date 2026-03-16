'''
Exemplo de simplificação de código usando if, elif e else


===usando função para simplificar o código===
preco_frutas = {
    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0
}

def get_preco(frutas, preco_frutas):
    return f"O preço da {frutas} é R${preco_frutas.get(frutas, 'Fruta não encontrada')}"

print(get_preco(frutas='maçã', preco_frutas=preco_frutas))
===usando função para simplificar o código===

# fruta = input("Digite o nome da fruta (maçã, banana, laranja): ").lower()

# if fruta in preco_frutas:
#     print(f"O preço da {fruta} é R${preco_frutas[fruta]:.2f}")

# print(f"O preço da {fruta} é R${preco_frutas[fruta]:.2f}" if fruta in preco_frutas else "Fruta não encontrada.")
    
    ===usando função para simplificar o código===

====exemplo de simplificação usando dicionário e método get() para evitar if, elif e else====
tabela_precos = {
    'Corte': 30.0,
    'Barba': 15.0,
    'Completo': 40.0
}

servico = input("Qual serviço deseja consultar? ")
valor = tabela_precos.get(servico, "Serviço não tabelado")

print(f"O valor para {servico} é: {valor}")
====exemplo de simplificação usando dicionário e método get() para evitar if, elif e else====

'''

# Definimos o dicionário (Base de dados)
preco_frutas = {
    'maçã': 2.5,
    'banana': 1.8,
    'laranja': 3.0
}

# Definimos qual fruta queremos procurar

# fruta_desejada = 'maçã' # Podemos pedir para o usuário digitar a fruta desejada

fruta_desejada = input("Digite o nome da fruta (maçã, banana, laranja): ").lower()

# Fazemos a busca direta usando o método .get()
# O .get() tenta encontrar a fruta; se não achar, mostra 'Fruta não encontrada'

resultado = preco_frutas.get(fruta_desejada, 'Fruta não encontrada')

# Exibimos o resultado
print(f"O preço da {fruta_desejada} é R${resultado}")