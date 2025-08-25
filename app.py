# imports
from flask import Flask, request, redirect, url_for, render_template
from datetime import datetime
from pathlib import Path
import csv

# ------------------------------
# 1 Configuração básica
# ------------------------------
app = Flask(__name__)

# Arquivo CSV onde salvaremos as respostas
CSV_FILE = Path("respostas.csv")

# Ordem das colunas do CSV
FIELDNAMES = [
    "timestamp",  # preenchido automaticamente
    "nome",
    "idade",
    "cidade",
    "genero",
    "sono",
    "atividade",
    "bebida",
    "app",
]

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    return f"Olá, {nome}! Formulário enviado com sucesso."


# ------------------------------
# 2 Rotas HTTP
# ------------------------------

@app.get("/")
def index():
    """Rota inicial que mostra o formulário"""
    return render_template("form.html")

@app.post("/enviar")
def enviar():
    """Recebe os dados do formulário e salva no CSV"""

    # 2.1 Coleta os campos do formulário
    payload = {
        "nome": request.form.get("nome", "").strip(),
        "idade": request.form.get("idade", "").strip(),
        "cidade": request.form.get("cidade", "").strip(),
        "genero": request.form.get("genero", "").strip(),
        "sono": request.form.get("sono", "").strip(),
        "atividade": request.form.get("atividade", "").strip(),
        "bebida": request.form.get("bebida", "").strip(),
        "app": request.form.get("app", "").strip(),
    }

    # 2.2 Validação básica da idade
    idade_str = payload.get("idade", "")
    if idade_str:
        try:
            idade_num = int(idade_str)
            if not (0 <= idade_num <= 120):
                idade_num = max(0, min(idade_num, 120))
            payload["idade"] = str(idade_num)
        except ValueError:
            payload["idade"] = ""

    # 2.3 Monta registro com timestamp
    registro = {"timestamp": datetime.now().isoformat(timespec="seconds"), **payload}

    # 2.4 Salva no CSV
    arquivo_existe = CSV_FILE.exists()
    with CSV_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        if not arquivo_existe:
            writer.writeheader()
        writer.writerow(registro)

    # redireciona para página de obrigado
    return redirect(url_for("obrigado"))

@app.get("/obrigado")
def obrigado():
    """Página de confirmação"""
    return render_template("obrigado.html")

# ------------------------------
# 3 Inicialização
# ------------------------------
if __name__ == "__main__":
    app.run(debug=True)

# ------------------------------
from flask import Flask, render_template, request

app = Flask(__name__)

