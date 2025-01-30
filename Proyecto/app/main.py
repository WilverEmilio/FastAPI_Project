from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from app.database import database as connection
from app.database import User, Movie, Review
from app.schemas import UserRequestModel, UserResponseModel, ReviewRequestModel, ReviewResponseModel

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

@app.post('/users', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(status_code=409, detail='El usuario ya existe', headers={'X-Error': 'El usuario ya existe'})
    
    hash_password = User.create_password(user.password)
    
    user = User.create(
        username=user.username,
        password=hash_password
        )
    
    return UserResponseModel(id = user.id, username = user.username)

@app.post('/reviews', response_model=ReviewResponseModel)
async def create_review(user_review: ReviewRequestModel):
    
    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code=404, detail='El usuario no existe', headers={'X-Error': 'El usuario no existe'})
    
    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(status_code=404, detail='La pelicula no existe', headers={'X-Error': 'La pelicula no existe'})
    
    user_review = Review.create(
        movie_id = user_review.movie_id,
        user_id = user_review.user_id,
        review = user_review.review,
        score = user_review.score
        )
    
    return ReviewResponseModel(id=user_review.id,movie_id = user_review.movie_id, review = user_review.review, score = user_review.score)
