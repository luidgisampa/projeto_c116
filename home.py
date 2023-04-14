from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")

def fist_page():

    nome = 'Luidgi Sampaio'
    idade = '16'
    jogo1 = 'Terraria'
    jogo2 = 'Hollow Knight'

    return render_template('index.html', nome_estudante = nome, idade_estudante = idade, jogo_favorito1 = jogo1, jogo_favorito2 = jogo2)


app.run(debug=True)