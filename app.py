from flask import Flask

app = Flask(__name__)

    
menu = """
<a href="/">Página inicial</a> | <a href="/sobre">Sobre</a> | <a href="/contato">Contato</a>
<br>
"""
<style>
  button:active {
    background-color: red;
  }

@app.route("/")
def index():
  return menu + "Olá, mundo! Esse é meu site. (Gabriela Soares)"

@app.route("/sobre")
def sobre():
  return menu + "Aqui vai o conteúdo da página Sobre"

@app.route("/contato")
def contato():
  return menu + "Aqui vai o conteúdo da página Contato"



