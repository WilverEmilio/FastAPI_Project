from pydantic import BaseModel, validator, ValidationError

class User(BaseModel):
    username: str
    password: str
    repeat_password: str
    email: str
    age: int
    
    class Config:
        orm_mode = True
        
    @validator("username")    
    def username_validation(cls, username: str):
        if len(username) < 4:
            raise ValueError("La longitud del username debe ser mayor a 4")
        
        if len(username) > 20:
            raise ValueError("La longitud del username debe ser menor a 20")
        
        return username

    @validator("repeat_password")
    def password_validation(cls, repeat_password, values):
        if 'password' in values and repeat_password != values['password']:
            raise ValueError("Las contraseñas no coinciden")
        
        return repeat_password

try: 
    user = User(
        username="Wilson",
        password="secret",
        repeat_password="hoal",
        email="hola@gmail.com",
        age=25
    )

    print(user)
except ValueError as e:
    print(e.json())