from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados que você quer exibir no HTML
    informacoes = [
        {"nome": "Matheus", "idade": 25, "cidade": "São Paulo"},
        {"nome": "Ana", "idade": 22, "cidade": "Rio de Janeiro"},
        {"nome": "Carlos", "idade": 30, "cidade": "Belo Horizonte"}
    ]
    return render_template('index.html', informacoes=informacoes)

if __name__ == '__main__':
    app.run(debug=True)