import requests

URL = "http://localhost:8000/api/v1/reviews"
REVIEW = {
  "movie_id": 1,
  "user_id": 5,
  "review": 'Review creada con requests',
  "score": 3
}

response = requests.post(URL, json=REVIEW)

if response.status_code == 200:
    print('Reseña creada de forma exitosa')
    print(response.json())
else: 
    print(
        response.content
    )