from flask import Flask, render_template
from dicionario.carro import carro

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/carro')
def mostra_carro():
    return render_template('carro.html',**carro)


app.run(debug=True)

