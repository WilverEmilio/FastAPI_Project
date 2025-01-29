from peewee import * 
from datetime import datetime


database = MySQLDatabase('reseña_pelucula', 
                         user="root", 
                         password="123456789",
                         host="localhost",
                         port=3306)


# A continuación se muestra como se crea una o varias tablas en la base de datos
class User(Model):
    username = CharField(max_length=50, unique=True)
    password = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.username
    
    class Meta: 
        database = database
        table_name = 'users'
    
class Movie(Model):
    title = CharField(max_length=100)
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return self.title
    
    class Meta: 
        database = database
        table_name = 'movies'
        
class Review(Model):
    movie = ForeignKeyField(Movie, backref='reviews')
    user = ForeignKeyField(User, backref='reviews')
    review = TextField()
    score = IntegerField()
    created_at = DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
    
    class Meta: 
        database = database
        table_name = 'reviews'