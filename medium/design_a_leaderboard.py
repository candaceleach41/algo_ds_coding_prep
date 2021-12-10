"""
Design a Leaderboard class, which has 3 functions:

1.) addScore(playerId, score): Update the leaderboard by adding score to the given player's score.
If there is no player with such id in the leaderboard, add him to the leaderboard with the
given score.

2.) top(K): Return the score sum of the top K players.

3.) reset(playerId): Reset the score of the player with the given id to 0 (in other words
erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard
before calling this function.

Initially, the leaderboard is empty.
"""

from heapq import heappush, heappop
from collections import defaultdict


class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def add_score(self, player_id, score):
        if player_id not in self.scores:
            self.scores[player_id] = score
        else:
            self.scores[player_id] += score

    def top(self, K):
        # heap = []
        # for x in self.scores.values():
        #     heappush(heap, x)
        #     if len(heap) > K:
        #         heappop(heap)
        # result = 0
        # while heap:
        #     result += heappop(heap)
        # return result
        return sum(sorted(self.player_score.values(), reverse=True)[:K])

    def reset(self, player_id):
        # del self.scores[playerId]
        self.scores[player_id] = 0


if __name__ == "__main__":
    leaderboard = Leaderboard()
    leaderboard.add_score(1, 73)
    leaderboard.add_score(2, 56)
    leaderboard.add_score(3, 39)
    leaderboard.add_score(4, 51)
    leaderboard.add_score(5, 4)
    leaderboard.top(1)
    leaderboard.reset(1)
    leaderboard.reset(2)
    leaderboard.add_score(2, 51)
    leaderboard.top(3)
