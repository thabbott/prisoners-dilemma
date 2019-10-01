[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/thabbott/prisoners-dilemma/master?urlpath=lab)

## General notes

I prepared this repository, which contains Python code for running an iterated prisoners dilemma tournament, for an informal seminar series held by graduate students in MIT's earth science department. The instructions below are specific to that seminar series, but the code should be relatively easy to repurpose. That being said, if you're searching for Python code for an iterated prisoners dilemma tournament, then [Axelrod](https://github.com/Axelrod-Python/Axelrod) is much better developed and may be a better option.

## The iterated prisoners' dilemma

The iterated prisoners' dilemma is a competition between prisoners that consists of a predetermined number of rounds (although, at least in this tournament, the prisoners do not know what that number is). During a single round, each prisoner must choose either to "cooperate" or "defect". If both prisoners choose to cooperate, each gets 3 points. If both prisoners choose to defect, each gets 1 point. If one prisoner chooses to defect and the other chooses to cooperate, the defector gets 5 points and the cooperator gets 0 points. The prisoners' goal is to develop a strategy that maximizes the number of points they receive over the course of a match.

## Tournament rules

This tournament was inspired by a [Radiolab episode](https://www.stitcher.com/podcast/wnycs-radiolab/e/63973084) that described a similar tournament run by [Robert Axelrod](https://en.wikipedia.org/wiki/Robert_Axelrod) in the 1960s---listen from 7:30 to about 17:40 for an overview of the motivation for the tournament and a description of the tournament itself.

In this tournament, prisoners compete as members of a "species" that specifies a strategy for them to follow. At the start of the tournament, each species is allocated an equal fraction of the total population of prisoners. The tournament then proceeds in two repeated phases:

1. **Round-robin competition**: every prisoner plays a match against every other prisoner, with points they win being assigned to their species. The round-robin includes matches between members of the same species, but prisoners are not alerted before these matches take place. (Note that points are rewarded such that members of the same species earn more points for their species when they both cooperate than when one cooperates and one defects.) Prisoners can retain memory of previous rounds over the course of a match but not between different matches.

2. **Evolution**: after each round-robin, the population fraction of each species is updated using discrete-time replicator dynamics, i.e. rescaled based on the ratio between the average fitness of members of that species and the average fitness of members of all species. Prisoners are then re-allocated between different species based on the total tournament population and population fractions, with non-integer numbers of prisoners rounded to the nearest integer. (This means that species go extinct when they no longer have a sufficient population fraction to receive at least half a prisoner.)

The tournament terminates when populations fractions reach a steady state (or, if some species use non-deterministic strategies, when populations appear to have reached a statistically steady state), and the species with the highest population fraction is the winner.

## Preparing submissions

To submit a strategy, create a subclass of the ``Prisoner`` class defined in ``Prisoner.py`` and override the ``__init__``, ``pick_strategy``, and ``process_results`` functions. ``Jesus.py``, ``Lucifer.py``, and ``TitForTat.py`` include example submissions corresponding to the Jesus, Lucifer, and tit-for-tat strategies mentioned for the podcast. I will submit all three of of them to the tournament, and in the meantime you can use them as reference strategies to test your submissions against.

I'm planning to run the tournament on Binder and have set up an environment that includes numpy, scipy, sklearn, and pandas in addition to the Python standard library. If there are other Python packages you want your strategy to be able to use, I'm happy to try to add them.

The functions that your strategy implements are used to play matches by passing your subclass to the following function:

```
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
```

In other words, ``__init__`` is called once at the start of a match; and in each round, ``pick_strategy`` is called to determine the strategies of each prisoner, the strategies are scored, and the strategies are passed back to ``process_results`` to allow each prisoner to store information to use in subsequent rounds.

Because this tournament style involves many round-robins, which involve many matches, which themselves involve many rounds, your strategies have to be fairly efficient: specifically, I ask that you submit a strategy that can play a 1000 round match against itself in less than 100 ms. (This provides a reasonable amount of leeway: the tit-for-tat strategy can play itself 1000 times in about 1 ms.) You can test this easily by passing two copies of your strategy to ``play_match`` and including ``n_rounds = 1000`` as a keyword argument---see ``validate.py`` for example code that times the ``Jesus``, ``Lucifer``, and ``TitForTat`` strategies.

To submit your strategy, email me a python source file containing your subclass **by 5PM on Monday, October 21**. I'll test your program by

1. Checking that it can play a 1000 round match against itself in less than 100 ms and
1. Checking that it can play long matches against Jesus, Lucifer, TitForTat, and randomly-generated strategies without producing exceptions.

If you want me to, I'm happy to test your implementation before the deadline so that you have time to fix any issues that come up, and I'll put the tests in a file in the repository that you all can use sometime soon.
