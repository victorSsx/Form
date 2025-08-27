from flask import Flask, render_template, request

app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    return f"Obrigado, {nome}! Recebemos seu email: {email}"
