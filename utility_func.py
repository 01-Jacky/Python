def _int2bin(self, i):
    """ Returns string representation of binary value using bitwise operation """
    if i == 0:
        return "0"

    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i = i / 2           # shifts bits down one, e.g. 101 -> 10

    return s