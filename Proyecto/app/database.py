from peewee import * 

database = MySQLDatabase('reseña_pelicula', 
                         user='root', 
                         password=123456789,
                         host='localhost',
                         port=3306)