import numpy as np
from math import log2, floor
from const import *


def aver(arr: list) -> float:
    """
    Выборочное среднее

    :param arr: выборка значений
    :type: arr: list
    :return: возвращает выборочное среднее
    :rtype: float
    """

    return sum(arr)/len(arr)


def var(arr: list) -> float:
    """
    Выборочная дисперсия

    :param arr: выборка значений
    :type arr: list
    :return: возвращает выборочную дисперсию
    :rtype: float
    """

    med = aver(arr)
    summ = 0
    for i in arr:
        summ += (i - med) * (i - med)

    return summ / len(arr)


def chi_2(arr: list) -> tuple:
    """
    Критерий хи-квадрат

    :param arr: выборка
    :type arr: list
    :return: значение статистики
    :rtype: tuple
    """

    a = 0
    theta = 32768
    N = len(arr)
    k = 1 + floor(log2(N))
    intervals = np.arange(a, a+theta, (theta-1)/k)

    probability_intervals = []
    for i in range(len(intervals)-1):
        left = np.ceil(intervals[i])
        right = np.floor(intervals[i + 1])
        if intervals[i + 1] == right and right != 32767:
            right -= 1
        probability_intervals.append((right - left + 1) / theta)
    intervals[-1] += 1

    intervals_count = [0]*k
    for i in arr:
        for j in range(len(intervals)-1):
            if intervals[j] <= i < intervals[j + 1]:
                intervals_count[j] += 1
    summary = 0
    for j in range(k):
        summary += intervals_count[j] ** 2 / (N * probability_intervals[j])

    v = summary - N
    sig_level_line = chi_table[k - 1]
    if v < sig_level_line[0]:
        return (f"Принимается: уровень значимости >= {max(significance_level)}", "Отвергается", v)
    elif v > sig_level_line[2]:
        return ("Отвергается", "Отвергается", v)

    st = ""
    for i in range(
        len(significance_level) - 1):
        if sig_level_line[i] <= v <= sig_level_line[i + 1]:
            st = f": уровень значимости ({significance_level[i + 1]}, {significance_level[i]}]"
        return ("Принимается " + st, "Принимается " + st, v)


def params(arr: list, type: str):

    """
    Параметры выборки

    :param type: ГПСЧ
    :param arr: выборка
    :type arr: list
    """

    normalized_lst = [i/32767 for i in arr]
    mean = aver(normalized_lst)
    dispersion = var(normalized_lst)
    standart_deviation = dispersion ** (1/2)
    var_coefficient = standart_deviation/mean
    r1, r2, val = chi_2(arr)
    if type == "lcg":
        print("LCG method\n")
    elif type == "xor":
        print("XorShiftPlus method\n")
    print(
    f"Размер выборки: {len(arr)}",
    f"Среднее: {round(mean, 6)}",
    f"Дисперсия: {round(dispersion, 6)}",
    f"Отклонение: {round(standart_deviation, 6)}",
    f"Коэффициент вариации: {round(var_coefficient, 6)}",
    f"Значение статистики: {round(val, 6)}",
    f"Равномерность: {r1}",
    f"Случайность: {r2}\n",
    sep = "\n")

