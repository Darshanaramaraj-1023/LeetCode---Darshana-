# Last updated: 9/15/2026, 3:27:49 PM
1class Solution:
2    def findWinners(self, matches):
3        losses = {}
4        players = set()
5
6        for winner, loser in matches:
7            players.add(winner)
8            players.add(loser)
9
10            losses[loser] = losses.get(loser, 0) + 1
11
12        zero_loss = []
13        one_loss = []
14
15        for player in players:
16            if losses.get(player, 0) == 0:
17                zero_loss.append(player)
18
19            elif losses[player] == 1:
20                one_loss.append(player)
21
22        zero_loss.sort()
23        one_loss.sort()
24
25        return [zero_loss, one_loss]