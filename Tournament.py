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
  n_repl: number of replicants of each species
  """
  def __init__(self, species, n_rounds, n_repl):
    self.species = species
    self.frequency = len(self.species) * [1.0/len(self.species)]
    self.population_size = n_repl * len(self.species)
    self.n_rounds = n_rounds
    self.repopulate()
    
  """
  Use discrete-time replicator dynamics to update species frequencies
  """
  def reproduce(self):
    
    # Calculate total score and number of members
    # of each species
    n = len(self.species) * [0]
    score = len(self.species) * [0.0]
    for ii, prisoner in enumerate(self.prisoners):
      for jj, species in enumerate(self.species):
        if prisoner == species:
          n[jj] += 1
          score[jj] += float(self.scores[ii])
    
    # Calculate fitness
    fitness = len(self.species) * [0.0]
    average_fitness = 0.0
    n_alive = 0
    for ii in range(len(fitness)):
      if n[ii] > 0:
          fitness[ii] = score[ii] / n[ii]
          average_fitness += n[ii] * fitness[ii]
          n_alive += n[ii]
      else:
          fitness[ii] = 0
    average_fitness = average_fitness / n_alive
    
    # Update frequencies
    for ii in range(len(self.frequency)):
      self.frequency[ii] = self.frequency[ii] * fitness[ii] / average_fitness
                
  """
  Re-populate prisoners based on species frequencies
  """
  def repopulate(self):
                
    # Update list of prisoners
    self.prisoners = []
    for ii, species in enumerate(self.species):
      nmembers = round(self.frequency[ii] * self.population_size)
      self.prisoners.extend(nmembers * [species])
    
    # Re-initialize scores
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
    (3,3) if both cooperate, 
    (1,1) if both defect, and 
    (5,0) or (0,5) if one cooperates and one defects
  """
  def score(self, strategy1, strategy2):
    
    if strategy1 and strategy2:
      return (3, 3)
    elif not strategy1 and strategy2:
      return (5, 0)
    elif strategy1 and not strategy2:
      return (0, 5)
    else:
      return (1, 1)
      
    
  """
  Play a single match
  
  Parameters
  ----------
  prisoner1: subclass of Prisoner
    First prisoner competing in the match
    
  prisoner2: subclass of Prisoner
    Second prisoner competing in the match
    
  n_rounds: int, optional
    Number of rounds in the match. If no value is
    provided, the number of rounds defaults to
    the default value for the tournament.
  
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
  Play a round robin
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
  Prints list of species sorted by population fraction
  """
  def __str__(self):

    # Sort species list by number of members
    population = list(zip(self.species, self.frequency))
    def sort_key(val):
      return val[1]
    population.sort(key = sort_key, reverse = True)
    
    # Create and return string representation
    string_repr = ""
    line_cols = 80
    for p in population:
      string_repr += ("%s %.2f " % (p[0].__name__, p[1]))
      num_hashes = round(80 * p[1]) - len(string_repr)
      if num_hashes < 0:
        num_hashes = 0
      string_repr += ("#" * num_hashes + "\n")
    return string_repr
