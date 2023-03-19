from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "Olá, mundo! Esse é meu site. (Gabriela Soares)"
