from Tournament import Tournament
from Jesus import Jesus
from Lucifer import Lucifer
from TitForTat import TitForTat

# Create tournament
species = [Jesus, Lucifer, TitForTat]
tournament = Tournament(species, 200, 10)

# Validate species
valid = True
for sp in species:
    print("")
    success = tournament.test_species(sp, species)
    if not success:
        print("%s failed validation" % sp.__name__)
        valid = False
if valid:
  print("All species passed validation")
