from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from app.database import database as connection
from app.database import User, Movie, Review
from app.schemas import UserModel

app = FastAPI(
    title = 'Proyecto para reseñar peliculas',
    description='En este proyecto seremos capaces de reseñar peliculas',
    version='0.1'
)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        
    connection.create_tables([User, Movie, Review]) #Para pdoer crear las tablas en la base de datos cuando se inicia una conexión, si ya existen no pasa nada, pero si no existen las crea

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        
        print ('Conexión cerrada')

@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')

@app.post('/users')
async def create_user(user: UserModel):
    
    if User.select().where(User.username == user.username).exists():
        return HTTPException(status_code=409, detail='El usuario ya existe', headers={'X-Error': 'El usuario ya existe'})
    
    hash_password = User.create_password(user.password)
    
    user = User.create(
        username=user.username,
        password=hash_password
        )
    
    return {
        'id': user.id,
        'username': user.username
    }