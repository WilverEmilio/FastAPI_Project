from fastapi import HTTPException, APIRouter, Response, Cookie, Depends
from fastapi.security import HTTPBasicCredentials
from app.database import User
from app.schemas import UserRequestModel, UserResponseModel
from typing import List
from app.schemas import ReviewResponseModel
from routes.common import oauth2_scheme,get_current_user

router = APIRouter(prefix='/users', tags=['Users'])

@router.post('', response_model=UserResponseModel)
async def create_user(user: UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        raise HTTPException(status_code=409, detail='El usuario ya existe', headers={'X-Error': 'El usuario ya existe'})
    
    hash_password = User.create_password(user.password)
    
    user = User.create(
        username=user.username,
        password=hash_password
        )
    
    return UserResponseModel(id = user.id, username = user.username)


@router.post('/login', response_model=UserResponseModel)
async def login(credentials: HTTPBasicCredentials, response: Response):
    
    user = User.select().where(User.username == credentials.username).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail='El usuario no existe', headers={'X-Error': 'El usuario no existe'})
    
    if user.password != User.create_password(credentials.password):
        raise HTTPException(status_code=401, detail='La contraseña es incorrecta', headers={'X-Error': 'La contraseña es incorrecta'})
    
    response.set_cookie(key='user_id', value=str(user.id))
    return user

# @router.get('/reviews', response_model=List[ReviewResponseModel])
# async def get_reviews(user_id: int = Cookie(None)):

#     user = User.select().where(User.id == user_id).first()

#     if user is None:
#         raise HTTPException(status_code=404, detail='El usuario no existe', headers={'X-Error': 'El usuario no existe'})

#     reviews = list(user.reviews)

#     return [user_review for user_review in reviews]



#Esto es para la implementación de la autenticación utilizando OAuth2, es decir que se necesita un token para poder acceder a las reseñas
# @router.get('/reviews')
# async def get_reviews(token: str = Depends(oauth2_scheme)):
#     return{
#         token
#     }


#Para saber que usuario esta autenticado y asi poder mostrar sus reseñas
@router.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews(user: User = Depends(get_current_user)):
    reviews = list(user.reviews)

    return [user_review for user_review in reviews]