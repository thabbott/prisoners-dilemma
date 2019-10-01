from Tournament import Tournament
from Jesus import Jesus
from Lucifer import Lucifer
from TitForTat import TitForTat

# Create tournament
species = [Jesus, Lucifer, TitForTat]
tournament = Tournament(species, 200, 10)

# Time species
valid = True
for sp in species:
    print("")
    s1 = 0
    s2 = 0
    start = time.thread_time()
    for ii in range(1000):
        (score1, score2) = self.play_match(sp, sp, 1000)
        s1 += score1
        s2 += score2
    end = time.thread_time()
    print("Validating %s" % species.__name__)
    print("Scores against self: %d, %d" % (s1, s2))
    print("Time: %.2f ms" % (end - start))
    valid = valid and (end - start < 100)

# Print results
if valid:
    print("All species passed validation")
