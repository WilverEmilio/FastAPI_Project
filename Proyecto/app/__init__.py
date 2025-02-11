from fastapi import FastAPI, APIRouter, Depends
from app.database import database as connection
from app.database import User, Movie, Review
from starlette.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from starlette import status
from routes.common import create_token


#Nuevo codigo para las rutas
from routes import users_router, reviews_router

app = FastAPI(
    title = 'Proyecto para reseñar peliculas',
    description='En este proyecto seremos capaces de reseñar peliculas',
    version='0.1'
)

api_version = APIRouter(prefix='/api/v1')

api_version.include_router(users_router)
api_version.include_router(reviews_router)

#Esto es para la implementación de la autenticación utilizando OAuth2
@api_version.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
    
    if user: 
        return{
            'access_token': create_token(user),
            'token_type': 'Bearer'
    }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Usuario o contraseña incorrectos',
            headers={'WWW-Authenticate': 'Bearer'})

app.include_router(api_version)

@app.on_event('startup')
async def startup():
    if connection.is_closed():
        connection.connect()
        
    connection.create_tables([User, Movie, Review]) #Para pdoer crear las tablas en la base de datos cuando se inicia una conexión, si ya existen no pasa nada, pero si no existen las crea

@app.on_event('shutdown')
async def shutdown():
    if not connection.is_closed():
        connection.close()
        
        print ('Conexión cerrada')
        
#Ruta de inicio
@app.get('/')
async def inicio():
    return RedirectResponse(url='/docs/')


