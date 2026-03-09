# --- CÓDIGO DA CÁPSULA DO TEMPO DIGITAL ---

# 1. Coletando informações do usuário
# Usamos input() para perguntar e armazenamos a resposta em variáveis
print("Olá! Vamos criar sua Cápsula do Tempo Digital! 🚀")





estilo = input("O que você gosta de vestir?") # Variável para guarda o estilo
musica = input("Qual seu gosto musical?") # Variável para guarda a musica
pet = input("Tem animal de estimação?") # Variável para guarda on pet


# Coletando informações numéricas e convertendo para inteiro com int()
# Isso é importante para podermos fazer cálculos com a idade 
ano_atual_str = input("Em que ano estamos? (Ex: 2025) ")
data_atual_str =input("Qual e a data de hoje? (Ex: 01/01")

ano_atual = int(ano_atual_str) # Converte o texto (string) para número inteiro (int) 
data_atual =int(data_atual_str) # Converte o texto (string) para número inteiro (int) 


anos_no_futuro_str = input("Daqui a quantos anos você quer 'abrir' sua cápsula? (Ex: 10)")
anos_no_futuro = int(anos_no_futuro_str) # Converte para número inteiro

# 2. Processando as informações
# Calculando o ano em que a cápsula será "aberta" 
ano_da_abertura = ano_atual + anos_no_futuro

# 3. Exibindo a mensagem da cápsula do tempo
# Usamos f-strings para formatar a saída de forma clara e personalizada 
print("\n--- ABRINDO SUA CÁPSULA DO TEMPO DIGITAL ---")
print(f"Olá do passado! Esta mensagem foi criada por {nome} no ano de {ano_atual}.")
print(f"Naquela época, seu estillo de {nome} era: {estilo}.")
print(f"Seu gosto musical de {nome} era: {musica}.")
Print(f"tem animal de estimação {nome} era: {pet} .")
print(f"\nEspero que você, em {ano_da_abertura}, esteja realizando seus sonhos!")
print("--- FIM DA CÁPSULA ---")
