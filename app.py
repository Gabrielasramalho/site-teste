from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
  return "Olá, mundo! Esse é meu site. (Gabriela Soares)"
  
  @app.route("/")
def sobre():
  return "sobre"
  
  @app.route("/")
def contato():
  return "contato"

