from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

Base = declarative_base()

engine = create_engine('sqlite:///C:/Users/Ageu4/Área de Trabalho/FinControl/database.db')


Session = sessionmaker(bind=engine)

class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    valor = Column(Integer)
    data_vencimento = Column(String)
    descricao = Column(String)
    paga = Column(Boolean)

Base.metadata.create_all(engine)
print("Tabelas criadas com sucesso!")
