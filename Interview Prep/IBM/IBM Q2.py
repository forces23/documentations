'''
A group of friends is playing a video game where players earn points. At the end of a round, players who achieve at least rank k can "level up" their characters. Given the scores of players at the end of the round, determine how many players will level up. 

Notes: Players with equal scores share the same rank, and the next player with a lower score takes the subsequent rank position. For instance, if four players finish with scores ranking them as 1, 1, 1, and 4, the first three players tie for first place, and the next player is ranked fourth. No player with a score of 0 can level up, regardless of rank. 

Example 
n = 4 
k = 3 
scores = [1100, 50, 50, 25] 

These players' ranks are [1, 2, 2, 4]. Because the players need to have a rank of at least k = 3 to level up, only the first three players qualify. Therefore, the answer is 3. 

Function Description Complete the function numPlayers in the editor with the following parameters: 
int k: the cutoff rank to level up a player's character 
int scores(n): the players' scores 
Returns int: the number of players who can level up after this round 

'''

from typing import List

def numPlayers(k: int, scores: List[int]) -> int:
    # type code here ...
    pass
    

# Example 1
print(numPlayers(3, [100, 50, 50, 25]))  # Expected: 3

# Example 2: tie at cutoff
print(numPlayers(3, [100, 50, 50, 50, 25]))  # Expected: 4 (3rd and 4th tied)

# Example 3: all scores positive, no ties
print(numPlayers(2, [80, 70, 60, 50]))  # Expected: 2

# Example 4: zero scores present
print(numPlayers(3, [100, 50, 0, 0]))  # Expected: 2

# Example 5: everyone has same score
print(numPlayers(3, [10, 10, 10, 10]))  # Expected: 3