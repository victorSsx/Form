from app import app
from flask import Flask, request, render_template

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome")
    return f"Olá, {nome}! Formulário enviado com sucesso."


# O Vercel precisa que exista essa variável global chamada "app"
app = app
