from database import db
from sqlalchemy import Column, Integer, String, Boolean

class Conta(db.Model):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    valor = Column(Integer)
    data_vencimento = Column(String)
    descricao = Column(String)
    paga = Column(Boolean)
    tipo = Column(String)  # Adicionado o campo tipo

    def __init__(self, valor, data_vencimento, descricao, paga=False, tipo=None):
        self.valor = valor
        self.data_vencimento = data_vencimento
        self.descricao = descricao
        self.paga = paga
        self.tipo = tipo