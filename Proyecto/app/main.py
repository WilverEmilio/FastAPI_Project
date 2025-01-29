from fastapi import FastAPI
from starlette.responses import RedirectResponse
from database import database as connection


app = FastAPI(
    title = 'Proyecto para reseñar peliculas',
    description='En este proyecto seremos capaces de reseñar peliculas',
    version='0.1'
)

@app.on_event('startup')
def startup():
    print('Iniciando el servidor')

@app.on_event('shutdown')
def shutdown():
    print('Apagando el servidor')

@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')
