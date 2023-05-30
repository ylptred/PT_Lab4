import numsgen
import timeit
from mathstat import *
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 400)


if __name__ == "__main__":
    N = [50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000]
    delta_time_LCG = []
    delta_time_mid_compositions = []
    delta_time_standart = []
    for i in N:
        delta_time_LCG.append(timeit.Timer(lambda: numsgen.LCG(i)).timeit(number=1))
        delta_time_mid_compositions.append(timeit.Timer(lambda: numsgen.mid_compositions(i)).timeit(number=1))
        delta_time_standart.append(timeit.Timer(lambda: numsgen.standart_random(i)).timeit(number=1))
    d = {'Время генерации LCG': delta_time_LCG,
         'Время генерации методом серединных произведений': delta_time_mid_compositions,
         'Время генерации стандартным способом': delta_time_standart}

    df = pd.DataFrame(data=d, index=N)
    print(df)

    for i in N:
        sample_lcg = numsgen.LCG(i)
        do_smth(sample_lcg, 0)
        sample_mid_c = numsgen.mid_compositions(i)
        do_smth(sample_mid_c, 1)
