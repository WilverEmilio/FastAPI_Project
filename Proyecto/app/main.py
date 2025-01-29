from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.database import database as connection
from app.database import User, Movie, Review


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
