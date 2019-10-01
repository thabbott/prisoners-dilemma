[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/thabbott/prisoners-dilemma/master?urlpath=lab)

## General notes

I prepared this repository, which contains Python code for running an iterated prisoners dilemma tournament, for an informal seminar series held by graduate students in MIT's earth science department. The instructions below are specific to that seminar series, but the code should be relatively easy to repurpose. That being said, if you're searching for Python code for an iterated prisoners dilemma tournament, then [Axelrod](https://github.com/Axelrod-Python/Axelrod) is much better developed and may be a better option.

## The iterated prisoners' dilemma

The iterated prisoners' dilemma is a competition between prisoners that consists of a predetermined number of rounds (although, at least in this tournament, the prisoners do not know what that number is). During a single round, each prisoner must choose either to "cooperate" or "defect". If both prisoners choose to cooperate, each gets 3 points. If both prisoners choose to defect, each gets 1 point. If one prisoner chooses to defect and the other chooses to cooperate, the defector gets 5 points and the cooperator gets 0 points. The prisoners' goal is to develop a strategy that maximizes the number of points they receive over the course of a match.

## Tournament rules

This tournament was inspired by a [Radiolab episode](https://www.stitcher.com/podcast/wnycs-radiolab/e/63973084) that described a similar tournament run by [Robert Axelrod](https://en.wikipedia.org/wiki/Robert_Axelrod) in the 1960s---listen from 7:30 to --:-- for an overview of the motivation for the tournament and a description of the tournament itself.

In this tournament, prisoners compete as members of a "species" that specifies a strategy for them to follow. At the start of the tournament, each species is allocated an equal fraction of the total population of prisoners. The tournament then proceeds in two repeated phases:

1. **Round-robin competition**: every prisoner plays a match against every other prisoner, with points they win being assigned to their species. The round-robin includes matches between members of the same species, but prisoners are not alerted before these matches take place. (Note that points are rewarded such that members of the same species earn more points for their species when they both cooperate than when one cooperates and one defects.) Prisoners can retain memory of previous rounds over the course of a match but not between different matches.

2. **Evolution**: after each round-robin, the population fraction of each species is updated using discrete-time replicator dynamics, i.e. rescaled based on the ratio between the average fitness of members of that species and the average fitness of members of all species. Prisoners are then re-allocated between different species based on the total tournament population and population fractions, with non-integer numbers of prisoners rounded to the nearest integer. (This means that species go extinct when they no longer have a sufficient population fraction to receive at least half a prisoner.)

The tournament terminates when populations fractions reach a steady state (or, if some species use non-deterministic strategies, when populations appear to have reached a statistically steady state), and the species with the highest population fraction is the winner.

## Preparing submissions
