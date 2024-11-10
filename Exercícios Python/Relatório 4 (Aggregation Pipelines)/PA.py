from database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")

class ProductAnalyzer:
    
    
    def __init__(self, database):
        self.connect(database)

    def totaldeCompras():
            
            return db.collection.aggregate([
             {"$unwind": "$produtos"},
             {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
             
        ])
        
    def maisgastouCompras():
        
        return db.collection.aggregate([
            
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
])

    def maisVendido():

        return db.collection.aggregate([
            
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
            
])
        
        
    def maisDe1Vendido():
        
        return db.collection.aggregate([
        
        {"$unwind": "$produtos"},
        {"$match": {"produtos.quantidade": {"$gt": 1}}},  # Modificado para considerar mais de uma unidade vendida
        {"$group": {
            "_id": "$cliente_id",
            "produtos_vendidos": {"$push": "$produtos"}, 
        }}
])
    
        
            