from fastapi import FastAPI, APIRouter
from app.database import database as connection
from app.database import User, Movie, Review
from starlette.responses import RedirectResponse


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

app.include_router(api_version)

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
        
#Ruta de inicio
@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')