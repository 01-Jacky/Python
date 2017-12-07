import math
def get_biggest_power(num):
    power = 1
    base = 26

    if math.pow(base,power) < num:
        return power -1

def int_to_char(num):
    return chr(ord('a')+num-1)

def num_to_alphabet(num):


if __name__ == '__main__':
    print(get_biggest_power(100))
    my_lst = []
    for x in range(10):
        if x % 2 == 0:
            my_lst.append(x)

    my_lst = [x for x in range(10) if x%2 == 0]
    print(my_lst)



