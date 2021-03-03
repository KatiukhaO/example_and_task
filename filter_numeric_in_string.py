"""Дана строка, содержащая натуральные числа и слова. Необходимо сформировать список 
из чисел, содержащихся в этой строке. Например, задана строка "abc83 cde7 1 b 24".
 На выходе мы должны получить список [83, 7, 1, 24]."""
string = input('input string: ')

numeric = list()
num = ''
for symbol in string:
    if symbol.isdigit():
        num = num + symbol
    elif num != '':
        numeric.append(int(num))
        num = ''
if num != '':
    numeric.append(int(num))
print(numeric)

'''для подібних задач на практиці часто використовуються регулярні вирази'''
''' в даному випадку вираз для цілих чисел'''
'''nums = re.findall(r'\d*\.\d+|\d+', s) - для дійсних чисел'''

import re

line = input('input string :')

numeric_list = re.findall(r'\d+', line)
print(numeric_list)
numeric_list = [int(numeric) for numeric in numeric_list]

print('Numeric List :', numeric_list)