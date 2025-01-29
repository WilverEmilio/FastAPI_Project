from pydantic import BaseModel, validator

class UserModel(BaseModel):
    username: str
    password: str
    
    class Config: 
         from_attributes = True  #Para que se pueda crear un objeto de la clase User a partir de un diccionario
         
    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('El nombre de usuario debe tener al menos 3 caracteres')
        
        return username