from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///donations.db'
db = SQLAlchemy(app)

class Solicitacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instituicao = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solicitacao', methods=['POST'])
def adicionar_solicitacao():
    data = request.get_json()
    nova_solicitacao = Solicitacao(instituicao=data['instituicao'], descricao=data['descricao'])
    db.session.add(nova_solicitacao)
    db.session.commit()
    return jsonify({'message': 'Solicitação adicionada com sucesso!'})

@app.route('/solicitacoes', methods=['GET'])
def listar_solicitacoes():
    solicitacoes = Solicitacao.query.all()
    resultado = []
    for solicitacao in solicitacoes:
        resultado.append({
            'id': solicitacao.id,
            'instituicao': solicitacao.instituicao,
            'descricao': solicitacao.descricao
        })
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
