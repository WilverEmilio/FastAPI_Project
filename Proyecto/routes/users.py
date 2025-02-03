from fastapi import HTTPException, APIRouter
from app.database import User
from app.schemas import UserRequestModel, UserResponseModel


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
