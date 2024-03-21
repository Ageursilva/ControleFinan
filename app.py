from flask import Flask, render_template, request, redirect, url_for
from models import db, Conta 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/Ageu4/Área de Trabalho/FinControl/database.db'
##db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route('/add_conta', methods=['POST'])
def add_conta():
    tipo = request.form['tipo']
    valor = request.form['valor']
    data_vencimento = request.form['data_vencimento']
    descricao = request.form['descricao']
    
    if tipo == 'pagar':
        nova_conta = Conta(valor=valor, data_vencimento=data_vencimento, descricao=descricao, tipo=tipo)
    else:
        nova_conta = Conta(valor=valor, data_vencimento=data_vencimento, descricao=descricao, tipo=tipo, paga=True)
    
    db.session.add(nova_conta)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/')
def index():
    # Buscar todas as contas
    contas = Conta.query.all() 

    contas_pagar = [conta for conta in contas if conta.tipo == 'pagar']
    contas_receber = [conta for conta in contas if conta.tipo == 'receber']
    # Calcular o total de contas a pagar e receber
    total_pagar = sum(conta.valor for conta in contas if conta.tipo == 'pagar')
    total_receber = sum(conta.valor for conta in contas if conta.tipo == 'receber')

    # Renderizar o template HTML com os totais calculados
    return render_template('index.html', total_pagar=total_pagar, total_receber=total_receber, contas_pagar=contas_pagar, contas_receber=contas_receber)

@app.route('/pagar_conta/<int:id>')
def pagar_conta(id):
    conta = Conta.query.get_or_404(id)
    conta.paga = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/editar_conta/<int:id>', methods=['POST'])
def editar_conta(id):
    conta = Conta.query.get_or_404(id)
    conta.valor = request.form['valor']
    conta.data_vencimento = request.form['data_vencimento']
    conta.descricao = request.form['descricao']
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/excluir_conta/<int:id>')
def excluir_conta(id):
    conta = Conta.query.get_or_404(id)
    db.session.delete(conta)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)