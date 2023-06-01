import timeit

import numsgen
from mathstat import *
import pandas as pd
from numsgen import *
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)


if __name__ == "__main__":
    N = [50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]
    delta_time_LCG = []
    delta_time_xorshiftplus = []
    delta_time_standard = []
    for i in N:
        delta_time_LCG.append(timeit.Timer(lambda: LCG(i)).timeit(number=1))
        delta_time_xorshiftplus.append(timeit.Timer(lambda: XorShiftPlus(i)).timeit(number=1))
        delta_time_standard.append(timeit.Timer(lambda: standard(i)).timeit(number=1))
    d = {'Время генерации LCG': delta_time_LCG,
         'Время генерации XorShiftPlus': delta_time_xorshiftplus,
         'Время генерации стандартным методом ЯП': delta_time_standard}

    df = pd.DataFrame(data=d, index=N)
    print(df)

    for i in N:
        sample_lcg = numsgen.LCG(i)
        params(sample_lcg, "lcg")
        sample_xor = numsgen.XorShiftPlus(i)
        params(sample_xor, "xor")
