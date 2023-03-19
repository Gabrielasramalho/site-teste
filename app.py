from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "Olá, mundo! Esse é meu site. (Gabriela Soares)"
  
  @app.route("/sobre")
def sobre():
  return "sobre"
  
  @app.route("/contato")
def contato():
  return "contato"

