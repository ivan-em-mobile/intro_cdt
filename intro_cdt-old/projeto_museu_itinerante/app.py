from flask import Flask, render_template# Importa o Flask e a função para renderizar templates

import datetime # Importa o módulo datetime para trabalhar com datas e horas

app = Flask(__name__) # Cria uma instância do aplicativo Flask

# Define uma rota para a página inicial (/)
@app.route('/')
def pagina_inicial():
    nome_usuario = "Usuario" # Você pode pegar isso de um banco de dados ou input
    agora = datetime.datetime.now() # Pega a data e hora atual
    data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S") # Formata a data e hora

    # Renderiza o template 'index.html' e passa as variáveis para ele
    return render_template('teste_python.html', usuario=nome_usuario, data_hora=data_hora_formatada)

# Executa o aplicativo Flask
if __name__ == '__main__':
    app.run(debug=True) # debug=True é ótimo para desenvolvimento, mostra erros no navegador
    
    # --- CÓDIGO DA CÁPSULA DO TEMPO DIGITAL ---

# 1. Coletando informações do usuário
# Usamos input() para perguntar e armazenamos a resposta em variáveis

# app.py