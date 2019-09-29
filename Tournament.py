from itertools import combinations
from random import shuffle

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
  """
  def __init__(self, prisoners, n_rounds):
    self.prisoners = prisoners
    self.n_rounds = n_rounds
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
  
  """
  def play_match(prisoner1, prisoner2):
    
    # Create instances of each prisoner
    p1 = prisoner1()
    p2 = prisoner2()
    
    # Initialize scores
    score1 = 0
    score2 = 0
    
    # Play all rounds
    for n in range(self.n_rounds):
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
  Play a round robin tournament
  
  Parameters
  ----------
  n_rounds: number of rounds per match
  """
  def round_robin(self, n_rounds):
    
    # Create a list of all combinations of prisoners
    matches = combinations(range(len(self.prisoners)), 2)
    
    # Pay all matches
    for match in shuffle(matches):
      (score1, score2) = self.play_match(prisoner[match[0]], prisoner[match[1]], n_rounds)
      self.scores[match[0]] += score1
      self.scores[match[1]] += score2
