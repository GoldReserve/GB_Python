"""1 - Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
приоритет операций стандартный. Функцию eval не использовать! Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
Пример: 1+2*3 => 7; (1+2)*3 => 9;
"""
# #Поскольку "Функцию eval не использовать!" а sympy это отдельная библиотека то :
# import sympy
# string_for_calc = input('Введите строку для вычислений:')
# print(sympy.sympify(string_for_calc))
import textwrap

"""2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные 
хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 
"""
# # Cоздаем файлик с текстом
# f = open('some_text.txt', 'w+')
# f.write("hhhhhhhhyyyyyyyyyyyytttvvvvvvvccccaaaaaaaaaaaaaaaeeemmmmmmmmnnnnnpppppppppppppooool")
# f.close()
#
# def encode(file:str):
#     encoded_message = ""
#     f = open(file, 'r')
#     for j in f:
#         encoded_message += j
#     message = encoded_message
#     encoded_message = ""
#     i = 0
#     f.close()
#     while (i <= len(message) - 1):
#         count = 1
#         ch = message[i]
#         j = i
#         while (j < len(message) - 1):
#             if (message[j] == message[j + 1]):
#                 count = count + 1
#                 j = j + 1
#             else:
#                 break
#         encoded_message = encoded_message + str(count) + ch
#         i = j + 1
#     f.close()
#     f = open('some_text_encoded.txt', 'w+')
#     f.write(f'{encoded_message}')
#     f.close()
#     return 'Название файла со сжатым текстом \'some_text_encoded.txt''\''
#
# print(textwrap.fill(encode('some_text.txt')))
# # print(textwrap.fill(text, width=60))

"""3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее 
в алфавите. ROT13 является примером шифра Цезаря. Создайте функцию, которая принимает строку и возвращает строку, 
зашифрованную с помощью Rot13 . Если в строку включены числа или специальные символы, они должны быть возвращены как 
есть. Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
 Не использовать функцию encode."""

# def rot13(x:str) -> str:
#     rot13 = bytes.maketrans(
#     b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
#     b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")
#     return x.translate(rot13)
#
# def rot13_1(x:str) -> str:
#     rot13_1 = bytes.maketrans(
#     b"nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM",
#     b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
#     return x.translate(rot13_1)
#
# z = 'I love2022 Python3.10'
# print(rot13(z), '\n', rot13_1(rot13(z)), sep='')
