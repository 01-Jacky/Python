from random import*

# Print half the dice and mirror it
r = randrange(6)
C = 'o '
s = '-----\n'
s = s + '|' + C[r<1] + ' ' + C[r<3] + '|\n'
s = s + '|' + C[r<5]

print s + C[r & 1] + s[::-1]
