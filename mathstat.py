import numsgen
import timeit
import numpy as np
from math import log2, floor

significance_level = [0.99, 0.95, 0.90]
chi_table = {
    5:  [0.55, 1.15 , 1.61 ],
    6:  [0.87, 1.64 , 2.20 ],
    7:  [1.24, 2.18 , 2.83 ],
    8:  [1.65, 2.73 , 3.49 ],
    9:  [2.09, 3.33 , 4.17 ],
    10: [2.56, 3.94 , 4.87 ],
    11: [3.05, 4.57 , 5.58 ],
    12: [3.57, 5.23 , 6.30 ],
    13: [4.11, 5.89 , 7.04 ],
    14: [4.66, 6.57 , 7.78 ],
    15: [5.23, 7.26 , 8.5  ],
    16: [5.81, 7.98 , 9.31 ],
    17: [6.41, 8.67 , 10.09],
    18: [7.02, 9.39 , 10.87],
    19: [7.63, 10.1 , 11.7 ],
    20: [8.26, 10.9 , 12.4 ],
    21: [8.90, 11.56, 13.2 ],
    22: [9.54, 12.34, 14.04],
}


def average(lst: list) -> float:

    """
    Вычисление выборочного среднего

    :param lst: выборка значений
    :type: lst: list
    :return: возвращает выборочное среднее
    :rtype: float
    """

    return sum(lst)/len(lst)


def variance(lst: list) -> float:
    """
    Вычисление выборочной дисперсии

    :param lst: выборка значений
    :type lst: list
    :return: возвращает выборочную дисперсию
    :rtype: float
    """
    m = average(lst)
    summary = 0
    for i in lst:
        summary += (i - m) * (i - m)

    return summary / len(lst)

def chi_2(lst: list) -> tuple:
    """
    Используя критерий хи-квадрат, определяем случайность и равномерность распределения

    :param sample: выборка
    :type sample: list
    :return: значение статистики, а также строковые описания
    :rtype: tuple
    """

    a = 0
    theta = 16384
    N = len(lst)
    k = 1 + floor(log2(N))
    intervals = np.arange(a, a+theta, (theta-1)/k)

    probability_inetrvals = []
    for i in range(len(intervals)-1):
        left = np.ceil(intervals[i])
        right = np.floor(intervals[i + 1])
        if intervals[i + 1] == right and right != 16383:
            right -= 1
        probability_inetrvals.append((right - left + 1) / theta)
    intervals[-1] += 1

    intervals_count = [0]*k
    for i in lst:
        for j in range(len(intervals)-1):
            if intervals[j] <= i < intervals[j + 1]:
                intervals_count[j] += 1
    summary = 0
    for j in range(k):
        summary += intervals_count[j] ** 2 / (N * probability_inetrvals[j])

    v = summary - N
    sig_level_line = chi_table[k - 1]
    if v < sig_level_line[0]:  # Если уровень значимости больше 0.99, то выборка равномерна и не случайна
        return (f"Принимается: уровень значимости >= {max(significance_level)}", "Отвергается", v)
    elif v > sig_level_line[2]:  # Если уровень значимости меньше 0.90, то выборка не равномерна и не случайна
        return ("Отвергается", "Отвергается", v)

    st = ""
    for i in range(
        len(significance_level) - 1):  # Если уровень значимости между 0.99 и 0.90, то выборка равномерна и случайна
        if sig_level_line[i] <= v <= sig_level_line[i + 1]:
            st = f": уровень значимости ({significance_level[i + 1]}, {significance_level[i]}]"
        return ("Принимается " + st, "Принимается " + st, v)


def do_smth(lst: list, type: int):

    """
    Вычисляет параметры выборки и, использую критерий хи-квадрат, определяется
                                     случайность и равномерность распределения

    :param sample: выборка
    :type sample: list
    """

    normalized_lst = [i/16353 for i in lst]
    mean = average(normalized_lst)
    dispersion = variance(normalized_lst)
    standart_deviation = dispersion ** (1/2)
    var_coefficient = standart_deviation/mean
    r1, r2, val = chi_2(lst)
    if type == 0:
        print("LCG method\n")
    else:
        print("Middle compostions method\n")
    print(
    f"Размер выборки: {len(lst)}",
    f"Среднее: {round(mean, 6)}",
    f"Дисперсия: {round(dispersion, 6)}",
    f"Отклонение: {round(standart_deviation, 6)}",
    f"Коэффициент вариации: {round(var_coefficient, 6)}",
    f"Значение статистики: {round(val, 6)}",
    f"Равномерность: {r1}",
    f"Случайность: {r2}\n",
    sep = "\n")

