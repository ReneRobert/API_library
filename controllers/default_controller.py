# coding: utf-8
# importer le code/bibliothèque des fonctions python permettant de communiquer avec une base mongodb
import os
import pymongo
from pymongo import MongoClient

# importer le code/bibliothèque d'une fonction qui sera utile pour les tris
from operator import itemgetter

# declarer que notre programme sera un « client » de communication avec notre base mongodb
client = MongoClient('db', 27017)

# declarer une base de donnée
db = client.mylibrary

# declarer une collection, terminologie mongodb, qui va correspondre à une classe d’objet que l’on veut stocker
books = db.books


# operation CREATE qui utilisera un POST
def book_create(book) -> str:
# créer le livre, passé en paramètre, dans la base mongodb
    result = books.insert(book)
# renvoyer une réponse
    return 'ok : le livre dont le titre est '+book["title"]+' a été enregistré dans la base'

# operation DELETE qui utilisera un DELETE. A noter que l'on va, ici, supprimer éventuellement plusieurs livres qui aurait le même id
def book_delete(bookId) -> str:
    result = books.delete_many({"id": bookId})
# renvoyer une réponse
    return ('nombre de livres, ayant cet id, supprimés : '+ str(result.deleted_count))

# operation LIST qui utilisera un GET
def book_list() -> str:
# on va créer une liste en allant chercher dans la base, puis on va la trier
    book_list = []
    for book in books.find():
# pour chaque livre il faut enlever l'id interne de mongodb
      del book['_id']
      book_list.append(book)
# on fait le tri en fonction de la valeur des id
    sorted_book_list_by_id = sorted(book_list, key = itemgetter('id'))
# renvoyer la  liste en réponse
    return sorted_book_list_by_id

# operation PATCH qui utilisera un PATCH
def book_patch(bookId, book) -> str:
# mettre à jour le livre passé en paramètre dans la base mongodb
    result = books.update_one({"id":bookId}, {"$set": book})
# renvoyer dans la réponse de la requête le livre remplacé
    return 'ok : informations du livre mis à jour'

# operation UPDATE qui utilisera un PUT
def book_update(bookId, book) -> str:
# remplacer le livre passé en paramètre dans la base mongodb
# pour un PUT, tous les champs sont obligatoires (mêmes ceux optionnels)
    result = books.replace_one({"id":bookId}, book)
# renvoyer dans la réponse de la requête le livre remplacé
    return 'ok : livre remplacé'

# operation FIND by ID qui utilisera un GET
def bookfind_by_id(bookId) -> str:
# on va créer une liste en allant chercher dans la base, puis on va la trier
    book_list = []
    for book in books.find({"id":bookId}):
# pour chaque livre il faut enlever l'id interne de mongodb
      del book['_id']
      book_list.append(book)
# on fait le tri
    sorted_book_list_by_id = sorted(book_list, key = itemgetter('id'))
# renvoyer la  liste en réponse
    return sorted_book_list_by_id


