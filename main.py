from fastapi import FastAPI, Depends, HTTPException

from conf.db_session import create_session

from models.usuario import Usuario
from sqlalchemy.orm import Session

from schemas.schema import SchemaUsuario
from schemas.schema import SchemaLogin

from fastapi.middleware.cors import CORSMiddleware




def get_db():
    db = create_session()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.get('/usuarios')
def get_usuarios(db: Session = Depends(get_db)):
    usuario = db.query(Usuario).all()
    return usuario

@app.get('/usuario/{id_usuario}')
def get_id_usuario(id_usuario:int,  db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id_usuario).one_or_none()
    return usuario


@app.post('/usuarios/cadastro')
def post_usuario(usuario: SchemaUsuario, db: Session = Depends(get_db)):
    novo_usuario: Usuario = Usuario(
        nome = usuario.nome,
        data_nascimento = usuario.data_nascimento,
        email = usuario.email,
        senha = usuario.senha
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return {'mensagem': 'Usuario adionado com sucesso'}



@app.post('/usuarios/login')
def login_usuario(login: SchemaLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == login.email).first()

    if not usuario or usuario.senha != login.senha:
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")

    return {"message": "Login realizado com sucesso!", "usuario": usuario.nome}



@app.put('/usuarios/atualizar/{id_usuario}')
def put_usuario(id_usuario:int, novo_usuario:SchemaUsuario, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id_usuario).one_or_none()

    if usuario:
        usuario.nome = novo_usuario.nome
        usuario.senha = novo_usuario.senha
        usuario.email = novo_usuario.email
        usuario.data_nascimento = novo_usuario.data_nascimento
        db.commit()
        db.refresh(usuario)
    else:
        raise {'mensagem': 'usuario não encontrado'}

    
    return usuario


@app.delete('/usuarios/delete/{id_usuario}')
def delete_usuario(id_usuario:int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id_usuario).one_or_none()
    if usuario:
        db.delete(usuario)
        db.commit()
    else:
        raise {'mensagem': 'usuario não encontrado'}
    
    return {'Mensagem': 'Usuario deletado com sucesso'}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou ["http://127.0.0.1:5500"] se usar o Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
