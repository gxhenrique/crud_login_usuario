from sqlalchemy import Column, String,Integer, Date

from models.model_base import Model_basel


class Usuario(Model_basel):
    __tablename__ = 'usuarios'


    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(90), nullable=True)
    data_nascimento: Date = Column(Date)
    email: str = Column(String(90), nullable=True, unique=True)
    senha: str = Column(String(12), nullable=True, unique=True)

    
    def __repr__ (self) -> str:
        return f'Email: {self.email}'
