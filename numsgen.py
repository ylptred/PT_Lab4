import time
from random import randint


def XorShiftPlus(size: int) -> list:
    """
    XorShiftPlus method
    :param size: - selection length
    :return:
    """
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
    """
    LCG method
    :param size: - selection length
    :return:
    """
    result = []

    m = (1 << 40) - 1
    k = 1 << 40
    b = int(time.perf_counter_ns() // 100)
    if b == m:
        b -= 1
    r0 = 25

    for i in range(size):
        r0 = (k * r0 + b) % m
        result.append(r0 % 32768)

    return result


def standard(size: int) -> list:
    """
    standard method of Python
    :param size: - selection length
    :return:
    """
    result = []
    for i in range(size):
        result.append(randint(0, 32768))
    return result
