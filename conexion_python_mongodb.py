import pymongo
from pymongo import MongoClient

# Reemplazar <connection string URI> con tu cadena de conexión
uri = "mongodb+srv://usuario:<clave>@cluster0.<codigo de clouster>.mongodb.net/"
client = MongoClient(uri)

try:
    # Accede a la base de datos y la colección
    database = client.get_database("nombre de la base de datos")
    peliculas = database.get_collection("nombre de la coleccion")
    print("Conexión exitosa")

except Exception as e:
    print(f"Error al conectar a MongoDB: {e}")

#Consulda de datos: nombre de la pelicula registrada en la base.
peliculas = peliculas.find({}, {"title": 1, "_id": 0})
for pelicula in peliculas:
    print(pelicula["title"])

# Insertar un solo documento
nuevo_documento = {
    "title": "Mi nueva película",
    "plot": "Una trama emocionante",
    "genres": ["Acción", "Aventura"],
    # y los demas camopos que se tenga
}

peliculas.insert_one(nuevo_documento)

# Para actualizar un documento por ejemplo el título.
filtro = {"title": "El nuevo titulo"}
nuevo_valor = {"$set": {"plot": "titulo registrado"}}
peliculas.update_one(filtro, nuevo_valor)

# Eliminar un documento
filtro = {"Id": "la identificació del documento"}
peliculas.delete_one(filtro)

client.close