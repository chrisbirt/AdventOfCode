import hashlib

def findhash(input, prefix):

    ret = 0
    hash = ''

    while not hash.startswith(prefix):
        ret += 1
        hash = hashlib.md5 ((input + str(ret)).encode('utf-8')) .hexdigest()

    return ret

def solve():

    p1, p2, day = 0, 0, 4
    hash = ''

    with open('input04') as f:
        input = f.read()

    p1 = findhash(input, '00000')
    p2 = findhash(input, '000000')

    print(f'Day {day}, part one: {p1}')
    print(f'Day {day}, part two: {p2}')


solve()