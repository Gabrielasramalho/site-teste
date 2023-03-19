from flask import Flask

app = Flask(__name__)

menu = """
<a href="/">inicial</a> 
<a href="/sobre">Sobre</a>
<a href="/contato">Contato</a>
<br>
"""

@app.route("/")
def hell_world():
  return menu + "Olá, mundo! Esse é meu site. (Gabriela Soares)"
  
  @app.route("/sobre")
def sobre():
  return "sobre"
  
  @app.route("/contato")
def contato():
  return "contato"

