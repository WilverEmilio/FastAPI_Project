from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    email: str
    age: int
    
user = User(
    username="johndoe",
    password="secret",
    email="hola@gmail.com",
    age=25
)

print(user)