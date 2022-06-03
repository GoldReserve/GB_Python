"""1. Дан список чисел. Создать список, в который попадают числа, описываемые возрастающую последовательность.
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д. Порядок элементов менять нельзя
"""
from random import randint

#
# lst, lst1 = [randint(1, 20) for _ in range(1, 21)], []
# for i in lst:
#     if i == lst[0] and i not in lst1:
#         lst1.append(i)
#         continue
#     else:
#         if i > max(lst1):
#             lst1.append(i)
#
# print(lst1)


"""2. Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию"""

# f = open('random.txt', 'w')
# x = [str(i) for i in [randint(1, 999) for _ in range(1, 15)]]
# f.write(' '.join(x))
#
# f = open('random.txt', "r+")
# lst = sorted(map(int, list(f.read().split(' '))))
#
# print(f'Исходный список отсортирован \n{lst}')
#
# # f = open('random.txt', 'w')
# # f.write(' '.join([str(i) for i in lst]))
# # f.close()


"""3.Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие 
максимальное количество элементов.
Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
[5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
"""
# n = 20
# lst = [randint(1, 99) for i in range(n)]
# arr_storage = [[0] for i in range(n)]
# arr_storage_arr, index_shift = 0, 0
#
# for elem_arr_storage in range(0, len(lst)):
#     for num in lst:
#         if num > max(arr_storage[arr_storage_arr]) and lst.index(num) >= index_shift:
#             arr_storage[arr_storage_arr].append(num)
#     arr_storage_arr += 1
#     index_shift += 1
#
# max_arr, num_of_arr = 0, 0
# for arr in arr_storage:
#     if len(arr) > max_arr:
#         max_arr = len(arr)
#         num_of_arr = arr
# num_of_arr.remove(0)
# print(f"Изначальный набор чисел {lst}\nМаксимальная последовательность ---> {num_of_arr}, её длина {max_arr} символов")

"""1э.Определите функцию beeramid которая...."""

# def beeramid(a: int, d: int):
#     num_lst = [i**2 for i in range(1, round(a**0.5))]
#     levels, cash = 0, 0
#     while cash < a/d:
#         cash += num_lst[levels]
#         levels += 1
#     return levels - 1
#
# print(beeramid(1500, 2))

"""2э.Создать функцию, которая из списка чисел возвращает число, являющее суммой двух или нескольких других элементов, 
либо возвращающее None, если такого числа нет. """

# def amount(a: list):
#     for num in a:
#         for value in a:
#             if a.index(num) != a.index(value) and value + num in a:
#                 return num + value
#     return None
#
#
# print(amount([7, 4, 17, 1, 87]))

















