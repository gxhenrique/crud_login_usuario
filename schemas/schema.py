from pydantic import BaseModel
from datetime import date

class SchemaUsuario(BaseModel):
    nome: str 
    data_nascimento: date 
    email: str
    senha: str 

    class Config:
        orm_mode = True


class SchemaLogin(BaseModel):
    email: str
    senha: str

    class Config:
        orm_mode = True
