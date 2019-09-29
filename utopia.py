from Tournament import Tournament
from Jesus import Jesus
from Lucifer import Lucifer
from TitForTat import TitForTat

class TitForTat2(TitForTat):
    pass

species = [Jesus, Lucifer, TitForTat, TitForTat2]
tournament = Tournament(species, 200, 10)
print(tournament)

while True:
    inp = input("Press Enter to start the next round")
    if inp.lower() == "done":
        break
    print("\n")
    tournament.round_robin()
    tournament.evaluate_fitness()
    tournament.repopulate()
    print("Results:")
    print(tournament)
