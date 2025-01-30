from pydantic import BaseModel, validator
from pydantic.utils import GetterDict
from typing import Any
from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res

class UserRequestModel(BaseModel):
    username: str
    password: str
    
    class Config: 
         from_attributes = True  #Para que se pueda crear un objeto de la clase User a partir de un diccionario
         
    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('El nombre de usuario debe tener al menos 3 caracteres')
        
        return username
    
class UserResponseModel(BaseModel):
    id : int
    username: str
    
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict