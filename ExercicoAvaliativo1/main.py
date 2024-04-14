from database import Database
from motoristaDao import MotoristaDAO, MotoristaCLI
import motorista
import corrida
import passageiro

db = Database(database="ExercícioAvaliativo1", collection="motoristas")
#db.resetDatabase()

cli = MotoristaCLI(db)
cli.menu()
