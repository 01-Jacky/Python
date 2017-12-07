players = ['p1','p2','p3','p4']
matches = []
size = 3

for player in players:
    opponents = players[:]
    opponents.remove(player)

    for opponent in opponents:
        matches.append((player,opponent))

print(matches)