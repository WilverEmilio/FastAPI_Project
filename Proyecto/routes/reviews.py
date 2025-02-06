from fastapi import HTTPException, APIRouter
from app.schemas import ReviewRequestModel, ReviewResponseModel, ReviewRequestPutModel, MovieResponseModel
from app.database import User, Movie, Review
from typing import List

router = APIRouter(prefix='/reviews', tags=['Reviews'])


@router.get('', response_model=List[ReviewResponseModel])
async def get_reviews(page: int = 1 , limit: int = 10):
    reviews = Review.select().paginate(page, limit) #Seleccionamos todas las reseñas de la base de datos
    
    return reviews

@router.get('/{review_id}', response_model=ReviewResponseModel)
async def get_review(review_id: int):
    review = Review.select().where(Review.id == review_id).first()
    
    if review is None:
        raise HTTPException(status_code=404, detail='La reseña no existe', headers={'X-Error': 'La reseña no existe'})
    
    return review

@router.post('', response_model=ReviewResponseModel)
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
    movie = Movie.select().where(Movie.id == user_review.movie_id).first()  # Obtener la película
    movie_response = MovieResponseModel(id=movie.id, title=movie.title)  # Convertir a Pydantic

    return ReviewResponseModel(id=user_review.id, movie=movie_response, review=user_review.review, score=user_review.score)


@router.put('/{review_id}', response_model=ReviewResponseModel)
async def update_review(review_id: int, review_data: ReviewRequestPutModel):
    review = Review.select().where(Review.id == review_id).first()
    
    if review is None:
        raise HTTPException(status_code=404, detail='La reseña no existe', headers={'X-Error': 'La reseña no existe'})
    
    review.review = review_data.review
    review.score = review_data.score
    
    review.save()
    
    return review

@router.delete('/{review_id}')
async def deleta_review(review_id: int):
    review = Review.select().where(Review.id == review_id).first()
    
    if review is None:
        raise HTTPException(status_code=404, detail='La reseña no existe', headers={'X-Error': 'La reseña no existe'})
    
    review.delete_instance()
    
    return {'message': 'La reseña ha sido eliminada'}

