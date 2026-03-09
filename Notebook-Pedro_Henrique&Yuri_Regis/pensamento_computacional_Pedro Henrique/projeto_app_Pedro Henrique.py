''''
CRUD

Barbearia

Atender o cliente com responsabildade, e cortar o cabelo do cliente ser atencioso e respeitar.


'''

print("\n=== GESAô Da BArBeARIA  ===")
print("1. Agendar Corte")
print("2. Ver Agenda do Dia")
print("3. Alterar Horário")
print("4. Cancelar Agendamento")
print("5. Cadastrar Cliente")
print("6. Listar Clientes")
print("7. Remover Cliente")
print("8. Serviços Disponíveis")
print("9. Relatório Financeiro")
print("0. Sair")



while True:

    escolha = input("\nEscolha uma opção:")

    if escolha == "1":if escolha == '1':
     print("Agendar Corte...")
    #Código para agendar cliente 

elif escolha == '2':
    print("Ver agenda do dia")
elif escolha == '3':
    print("Alterar horario")
elif escolha == '4':
    print("Cancelar agendamento")
elif escolha == '5':
    print("Cadastrar cliente")
elif escolha == '6':
    print("Listar clientes")
elif escolha == '7':
    print("Remover cliente")
elif escolha == '8':
    print("Serviços disponiveis")
elif escolha == '9':
    print("Relatorio financeiro")

elif escolha == '0':
    print("Sair")
    break



else:
    print("opção inválida. Por favor, tente novamente")