from database import Database
from helper.writeAJson import writeAJson
from PA import ProductAnalyzer

db = Database(database="mercado", collection="compras")


totaldecompras = ProductAnalyzer.totaldeCompras()
writeAJson(totaldecompras,"Total de compras")

maisvendido = ProductAnalyzer.maisVendido()
writeAJson(maisvendido,"Mais vendido")

maisgastou = ProductAnalyzer.maisgastouCompras()
writeAJson(maisgastou,"Mais gastou")

unidade = ProductAnalyzer.maisDe1Vendido()
writeAJson(unidade,"Mais de 1 vendido")
