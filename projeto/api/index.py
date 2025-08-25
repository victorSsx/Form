import sys # Para manipulação do sistema
import os # Para manipulação de caminhos

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app # Importa a aplicação Flask do arquivo app.py

# handler que a Vercel precisa
def handler(environ, start_response):
    return app(environ, start_response) # Chama a aplicação Flask