from Tournament import Tournament
from Jesus import Jesus
from Lucifer import Lucifer
from TitForTat import TitForTat
from Telepath import Telepath
from BahHumbug import BahHumbug
from FelizNavidad import FelizNavidad
from Inv_Judas import Inv_Judas
from Judas import Judas
from MasonPrisoner import MasonPrisoner
from Random import Random
from SchizophrenicRetribution import SchizophrenicRetribution
from TitForTat_Avg import TitForTat_Avg
from XmasTruce import XmasTruce
import time

# Create tournament
species = [Jesus, Lucifer, TitForTat, Telepath,
    BahHumbug, FelizNavidad, Inv_Judas, Judas,
    MasonPrisoner, Random, SchizophrenicRetribution,
    TitForTat_Avg, XmasTruce]
tournament = Tournament(species, 200, 10)

# Time species
valid = True
for sp in species:
    print("")
    s1 = 0
    s2 = 0
    start = time.thread_time()
    for ii in range(1000):
        (score1, score2) = tournament.play_match(sp, sp, 1000)
        s1 += score1
        s2 += score2
    end = time.thread_time()
    print("Validating %s" % sp.__name__)
    print("Scores against self: %d, %d" % (s1, s2))
    print("Time: %.2f ms" % (end - start))
    valid = valid and (end - start < 100)

# Print results
if valid:
    print("All species passed validation")
