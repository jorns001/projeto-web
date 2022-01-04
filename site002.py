#---------------------------------------
# site002.py
# criação de site com Python->flask
# Jorns - Jan/2022
# --------------------------------------

from flask import Flask, render_template, request

app = Flask(__name__)

# criar a 1ª pagina do site
# route > caminho
# function > o que vai ser exibido
# templates

@app.route("/")
def homepage():
    return render_template("homepage.html");

@app.route("/contato/")
def contato():
    return render_template("contato.html");

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario);

# colocar o site no ar
if __name__ =="__main__":
    app.run(debug=True)