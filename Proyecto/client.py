import requests

#----Petición del cliente en la que se pueden crear reseñas-----

# URL = "http://localhost:8000/api/v1/reviews"
# REVIEW = {
#   "movie_id": 1,
#   "user_id": 5,
#   "review": 'Review creada con requests',
#   "score": 3
# }

# response = requests.post(URL, json=REVIEW)

# if response.status_code == 200:
#     print('Reseña creada de forma exitosa')
#     print(response.json())
# else: 
#     print(
#         response.content
#     )

#----Petición del cliente para poder actualizar y eliminar las reseñas-----

# REVIEW_ID = 2
# URL = f"http://localhost:8000/api/v1/reviews/{REVIEW_ID}"
# REVIEW = {
    
#     "review": "BAD",
#     "score": 5
    
# }

# request = requests.put(URL, json=REVIEW)

# if request.status_code == 200:
#     print('Reseña actualizada de forma exitosa')
#     print(request.json())
# else:
#     print(
#         request.content
#     )

# request = requests.delete(URL)

# if request.status_code == 200:
#     print('Reseña eliminada de forma exitosa')
#     print(request.json())
# else:
#     print(
#         request.content
#     )


#---Petición para que el cliente pueda tener cookies y poder hacer login-----


URL = "http://localhost:8000/api/v1/users/login"
USER = {
  "username": "Bob",
  "password": "1234"
}

response = requests.post(URL, json=USER)

if response.status_code == 200:
    print('Usuario logeado de forma exitosa')
    print(response.json())
    print(response.cookies) # Aquí se puede ver la cookie
    print(response.cookies.get_dict()) # Aquí se puede ver la cookie
    
    user_id = response.cookies.get_dict().get('user_id')
    print(user_id)
else:
    print(
        response.content 
    )