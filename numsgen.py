import time
from random import randint

def XorShift(size: int) -> list:
    result = []
    for i in range(size):
        s0 = 1
        s1 = 2
        x, y = s0, s1
        x = x ^ ((x << 23) & 0xFFFFFFFFFFFFFFFF)  # 64bit
        x = (x ^ (x >> 17)) ^ (y ^ (y >> 26))
        s0, s1 = y, x
        result.append(s0 + s1)
    return result

def LCG(size: int) -> list:
    result = []
    m = (1 << 63) - 1
    k = 1 << 63
    b = int(time.perf_counter_ns() // 100)
    if b == m:
        b -= 1
    r0 = 13
    for i in range(size):
        r0 = (k * r0 + b) % m
        result.append(r0 % 16384)
    return result

def standard(size: int) -> list:
    result = []
    for i in range(size):
        result(randint(0, 16384))