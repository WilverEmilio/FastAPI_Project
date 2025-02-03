from pydantic import BaseModel, field_validator
from typing import Any
from peewee import ModelSelect
from playhouse.shortcuts import model_to_dict

class ResponseModel(BaseModel):
    class Config:
        from_attributes = True  
    
    @classmethod
    def from_peewee(cls, peewee_instance):
        """ Convierte un objeto Peewee en un modelo Pydantic """
        return cls(**model_to_dict(peewee_instance, backrefs=True))  

class UserRequestModel(BaseModel):
    username: str
    password: str
    
    @field_validator('username')
    @classmethod
    def username_validator(cls, username):
        if not (3 <= len(username) <= 50):
            raise ValueError('El nombre de usuario debe tener entre 3 y 50 caracteres')
        return username


class UserResponseModel(ResponseModel):
    id: int
    username: str


class MovieResponseModel(ResponseModel):
    id: int
    title: str

class ReviewValidator:
    @field_validator('score')
    @classmethod
    def score_validator(cls, score):
        if not (1 <= score <= 5):
            raise ValueError('La puntuación debe ser entre 1 y 5')
        return score

class ReviewRequestModel(BaseModel, ReviewValidator): 
    movie_id: int
    user_id: int
    review: str
    score: int

class ReviewResponseModel(ResponseModel):
    id: int
    movie: MovieResponseModel
    review: str
    score: int

class ReviewRequestPutModel(BaseModel, ReviewValidator):
    review: str
    score: int
