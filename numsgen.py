import time
from random import randint


def XorShiftPlus(size: int) -> list:
    result = []
    s0 = 1
    s1 = 2
    for i in range(size):
        x, y = s0, s1
        x = x ^ ((x << 17) & 0xFFFFFFFFFFFFFFFF)
        x = (x ^ (x >> 12)) ^ (y ^ (y >> 22))
        s0, s1 = y, x
        result.append(s0 + s1)
    return result


def LCG(size: int) -> list:
    x0 = 5
    m = 7
    a = 3
    c = 3
    result = [0] * size
    result[0] = x0

    for i in range(1, size):
        result[i] = ((result[i - 1] * a) + c) % m

    return result


def standard(size: int) -> list:
    result = []
    for i in range(size):
        result.append(randint(0, 16384))
    return result
