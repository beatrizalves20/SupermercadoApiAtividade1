from flask import Flask, request

api = Flask(__name__)

produtos = []
usuarios = []
setores = []
categorias = []


def getID(data):
    if data:
        return max(item['id'] for item in data) + 1
    return 1

@api.route("/")
def index():
    return ({'version': '1.0.0'}, 200)


@api.route('/categorias/<int:id>', methods=['GET'])
def getCategoriaByID(id:int):
    categoria = next((c for c in categorias if c['id'] == id), None)
    if categoria:
        return (categoria)
    
    return ({'message': 'Categoria não encontrada'}), 404
    
@api.route('/categorias', methods=['GET', 'POST'])
def categoriasHandle():
    if request.method == 'POST':
        json = request.get_json()
    
        jsonCategoria ={
           'id': getID(categorias),
           'nome': json['nome']                
        }
               
        return (jsonCategoria), 201
    
    elif request.method == 'GET':
        
        return (categorias, 200)

@api.route('/produtos', methods=['GET', 'POST'])
def produtosHandle():
    if request.method == 'POST':
        json = request.get_json()
        
        jsonProduto ={
            'id': getID(produtos),
           'nome': json['nome']                
        }
               
        return ( jsonProduto), 201
    
    elif request.method == 'GET':
        
        return (produtos, 200)
 
def getProdutoByID(id:int):
    produto = next((i for i in produtos if i['id'] == id), None)
    if produto:
        return (produto)
    return ({'error': 'não encontrado'}, 404)

@api.route('/usuarios', methods=['GET', 'POST'])
def usuariosHandle():
    if request.method == 'POST':
        json = request.get_json()
        
        jsonUsuarios ={
            'id': getID(usuarios),
           'nome': json['nome']                
        }
               
        return ( jsonUsuarios), 201
    
    elif request.method == 'GET':
        
        return (usuarios, 200)

def getUsuarioByID(id:int):
    usuario = next((i for i in usuarios if i['id'] == id), None)
    if usuario:
        return (usuario)
    return ({'error': 'Usuario não encontrado'}, 404)

@api.route('/setores', methods=['GET', 'POST'])
def setoresHandle():
    if request.method == 'POST':
        json = request.get_json()
        
        jsonSetores ={
            'id': getID(setores),
           'nome': json['nome']                
        }
               
        return (jsonSetores), 201
    
    elif request.method == 'GET':
        
        return (setores, 200)
    
def getsetorByID(id:int):
    setor = next((i for i in setores if i['id'] == id), None)
    if setor:
        return (setor)
    return ({'error': 'Setor não encontrado'}, 404) 
   
if __name__ == '__main__':
    api.run(debug=True)
