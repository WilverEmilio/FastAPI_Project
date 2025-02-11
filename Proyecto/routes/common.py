#agrgar todas las variables comúnes en un archivo common.py que va a utilizar el cliente/proyecto
import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'CodigoFacilito2021'

def create_token(user, days=7):
    data = {
        'user_id': user.id,
        'username': user.username,
        'exp': datetime.utcnow() + timedelta(days=days)
    }
    return jwt.encode(data, SECRET_KEY, algorithm='HS256')