from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()


tipos = ["Fire"]
pokemons = Pokedex.encontrarPokemonPeloTipo(tipos)
writeAJson(pokemons, "pokemons_por_tipos")

charmander = Pokedex.encontrarPokemonPeloNome("Charmander")
writeAJson(charmander, "charmander")

chikorita = Pokedex.encontrarEvolucaoPokemon("Chikorita")
writeAJson(chikorita, "evolucao_do_pokemon")

fraquezas = ["Water","Poison"]
pokemonsFraq = Pokedex.encontrarFraquezas(fraquezas)
writeAJson(pokemonsFraq, "fraquezas_pokemons")

a = 0.2
b = 0.4


chanceSpawn = Pokedex.chanceDeSpawn(a, b)
writeAJson(chanceSpawn, "chance_spawn")