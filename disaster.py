from Tournament import Tournament
from Jesus import Jesus
from Lucifer import Lucifer
from TitForTat import TitForTat

class Jesus2(Jesus):
    pass

species = [Jesus, Jesus2, Lucifer, TitForTat]
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
