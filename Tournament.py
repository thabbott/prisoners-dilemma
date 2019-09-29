from itertools import combinations
from random import shuffle
import time

"""
Prisoners' dilemma tournament
"""
class Tournament():

  """
  Initialize the tournament
  
  Parameters
  ----------
  prisoners: list of competing Prisoner subclasses
  n_rounds: rounds per match
  n_repl: number of initial replicants of each prisoner
  """
  # TODO: support non-zero number of replicants
  def __init__(self, species, n_rounds, n_repl):
    self.species = species
    self.fitness = len(self.species) * [n_repl]
    self.total_prisoners = len(self.species) * n_repl
    self.n_rounds = n_rounds
    self.repopulate()
    
  """
  Evaluate fitness of each species, proceeding as follows:
  
  - Tally the total number of points earned each round
  as well as the total number of points per species
  
  - Calculate the number of points required to earn a prisoner
  for the next round as
    (points from previous round) // (population of the tournament)
  
  - Allocate a whole number of prisoners to each species, rounding down
  """
  def evaluate_fitness(self):
    
    # Tally total score for each species
    total_score = 0
    self.fitness = len(self.species) * [0]
    for ii, prisoner in enumerate(self.prisoners):
      for jj, species in enumerate(self.species):
        if prisoner == species:
          self.fitness[jj] += self.scores[ii]
          total_score += self.scores[ii]
          
    # Calculate points per prisoner
    points_per_prisoner = total_score // self.total_prisoners
    
    # Catch some corner cases
    if points_per_prisoner < 1:
        points_per_prisoner = 1
    
    # Convert scores to prisoners
    for ii, species in enumerate(self.species):
      self.fitness[ii] = self.fitness[ii] // points_per_prisoner   
  
  """
  Repopulate prisoners: one per unit fitness of each species
  """
  def repopulate(self):
    self.prisoners = []
    for ii in range(len(self.species)):
        self.prisoners.extend(self.fitness[ii] * [self.species[ii]])
    self.scores = len(self.prisoners) * [0]
    
  """
  Score a single round
  
  Parameters
  ----------
  strategy1: bool
    First Prisoner's strategy
    
  strategy2: bool
    Second Prisoner's strategy
    
  Returns
  -------
  (score1, score2): (int, int)
    (1,1) if both cooperate, 
    (0,0) if both defect, and 
    (2,0) or (0,2) if one cooperates and one defects
  """
  def score(self, strategy1, strategy2):
    
    if strategy1 and strategy2:
      return (1, 1)
    elif not strategy1 and strategy2:
      return (2, 0)
    elif strategy1 and not strategy2:
      return (0, 2)
    else:
      return (0, 0)
      
    
  """
  Play a single match
  
  Parameters:
  prisoner1: subclass of prisoner
  prisoner2: subclass of prisoner
  n_rounds: number of rounds
  
  Returns
  -------
  (int, int): scores for prisoner1 and prisoner2
  """
  def play_match(self, prisoner1, prisoner2, n_rounds = None):
    
    # Create instances of each prisoner
    p1 = prisoner1()
    p2 = prisoner2()
    
    # Initialize scores
    score1 = 0
    score2 = 0
    
    # Play all rounds
    if not n_rounds:
      n_rounds = self.n_rounds
    for n in range(n_rounds):
      strategy1 = p1.pick_strategy()
      strategy2 = p2.pick_strategy()
      scores = self.score(strategy1, strategy2)
      score1 += scores[0]
      score2 += scores[1]
      p1.process_results(strategy1, strategy2)
      p2.process_results(strategy2, strategy1)
      
    # Return scores
    return (score1, score2)

  """
  Pre-tournament testing: model must play itself 1000 times
  in less than 1/100 s and succesfully play Jesus, Lucifer,
  and TitForTat
  """
  def test_species(self, species):
    
    # Time species playing against itself
    s1 = 0
    s2 = 0
    start = time.thread_time()
    for ii in range(1000):
        (score1, score2) = self.play_match(species, species, 1000)
        s1 += score1
        s2 += score2
    end = time.thread_time()
    print("Validating %s" % species.__name__)
    print("Scores against self: %d, %d" % (s1, s2))
    print("Time: %.2f ms" % (end - start))
    success = (end - start < 10)
    
    # Test that species can play against others
    for other in [Jesus, Lucifer, TitForTat]:
        try:
            self.play_match(species, other, 1000)
            print("Successfully played %s" % other.__name__)
        except:
            success = False
            print("Failed against %s" % other.__name__)
    return success
    
  """
  Play a round robin tournament
  
  Parameters
  ----------
  n_rounds: number of rounds per match
  """
  def round_robin(self):
    
    # Create a list of all combinations of prisoners
    matches = list(combinations(range(len(self.prisoners)), 2))
    shuffle(matches)
    
    # Pay all matches
    for match in matches:
      
      (score1, score2) = self.play_match(
        self.prisoners[match[0]], 
        self.prisoners[match[1]])
      self.scores[match[0]] += score1
      self.scores[match[1]] += score2
      
  """
  Override __str__ for display in REPL.
  Prints list of species sorted by number of members
  """
  def __str__(self):
    
    # Tally number of members per species
    tally = []
    for ii, species in enumerate(self.species):
      num_members = 0
      for prisoner in self.prisoners:
        if prisoner == species:
          num_members += 1
      tally.append((species.__name__, num_members))
    
    # Sort species list by number of members
    def sort_key(val):
      return val[1]
    tally.sort(key = sort_key, reverse = True)
    
    # Create string representation
    max_members = tally[0][1]
    line_cols = 75
    members_per_hash = float(max_members) / line_cols
    string_repr = ""
    for t in tally:
      string_repr += ("%s " % t[0])
      num_hashes = 0
      if members_per_hash > 0:
        num_hashes = round(float(t[1]) / members_per_hash) - len(t[0]) - 1
      if num_hashes < 0:
        num_hashes = 0
      string_repr += ("#" * num_hashes)
      string_repr += " %d\n" % t[1]
      
    return string_repr
