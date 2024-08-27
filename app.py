from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados em memória (variáveis voláteis)
data = {
    "produtos": [],
    "usuarios": [],
    "setores": [],
    "categorias": []
}

# Função para gerar novos IDs
def get_new_id(endpoint):
    if data[endpoint]:
        return max(item['id'] for item in data[endpoint]) + 1
    return 1

# Função para listar ou adicionar itens
def handle_endpoint(endpoint):
    if request.method == 'POST':
        new_item = request.json
        new_item['id'] = get_new_id(endpoint)
        data[endpoint].append(new_item)
        return jsonify(new_item), 201
    
    return jsonify(data[endpoint])

# Função para obter item específico por ID
def get_item(endpoint, item_id):
    item = next((i for i in data[endpoint] if i['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': f'{endpoint[:-1].capitalize()} não encontrado'}), 404

# Rotas para os endpoints
@app.route('/<endpoint>', methods=['GET', 'POST'])
def handle_items(endpoint):
    if endpoint not in data:
        return jsonify({'message': 'Endpoint inválido'}), 404
    return handle_endpoint(endpoint)

@app.route('/<endpoint>/<int:item_id>', methods=['GET'])
def handle_item(endpoint, item_id):
    if endpoint not in data:
        return jsonify({'message': 'Endpoint inválido'}), 404
    return get_item(endpoint, item_id)

if __name__ == '__main__':
    app.run(debug=True)
