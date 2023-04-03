from flask import Flask, request
from swagger_ui import api_doc
import yaml

app = Flask(__name__)

api_doc(app, config_path='./swagger.json', url_prefix='/swagger')

USUARIOS = []

@app.get('/usuarios')
def get_usuarios(id=None):
    return USUARIOS

@app.get('/usuarios/<id>')
def get_usuario_especifico(id=None):
    try:
        return USUARIOS[int(id)]
    except:
        return {'message': 'Não existe usuário com esse id'}, 404


@app.post('/usuarios')
def post_usuario():
    usuario = request.json
    for usuario_cadastrado in USUARIOS:
        if usuario['cpf'] == usuario_cadastrado['cpf']:
            return {'message': 'Um usuário com esse cpf já foi cadastrado'}, 401
    else:
        id = len(USUARIOS)
        usuario_cadastrado = {**usuario, 'id': id}
        USUARIOS.append(usuario_cadastrado)
        return usuario_cadastrado


if __name__ == '__main__':
    app.run()
