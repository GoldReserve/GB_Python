# """1.Найти НОК двух чисел"""
# import math
#
# def common_multiple(a:int, b:int):
#     """
#     :param a: First int number
#     :param b: Second int number
#     :return: Least common multiple
#     """
#     return f"Наименьший общий делитель чисел {a} и {b} " \
#            f"равен {math.gcd(a, b)}"
#
#
# print(common_multiple(8, 24))
#
# """2.Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
#  """
#
# def accuracy(a, b):
#     x = input('Введите точность вычисления:')
#     return round(a/b, int(x))
#
# print(accuracy(14, 9))

# """3. Составить список простых множителей натурального числа N"""
#
# def Factor(num:int):
#     lst = []
#     divider = 2
#     while divider * divider <= num:
#         if num % divider == 0:
#             lst.append(divider)
#             num //= divider
#         else:
#             divider += 1
#     if num > 1:
#         lst.append(num)
#     return lst
#
# print(Factor(14))
#
#
# """4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]"""
#
# def unique(a):
#     return list(set(a))
#
# print(unique([1, 2, 3, 5, 1, 5, 3, 10]))