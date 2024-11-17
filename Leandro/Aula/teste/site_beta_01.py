from flask import Flask, render_template, request, jsonify

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    resultado = data['numero'] * 2  # Exemplo de cálculo
    return jsonify({"resultado": resultado})

if _name_ == '_main_':
    app.run(debug=True)