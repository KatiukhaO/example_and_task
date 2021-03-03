'''
*********************************************************************
Задача: є файл xml формату, перевірить чи він правильно написаний,
мають всі теги бути закриті і в правильній послідовності, вивести на 
екран повідомлення про помилку або її відсутність, назви тегів довільні, 
текст між тегами теж може бути довільний
*******************************************************************
'''

import re

file_xml = open('file_xml.xml', 'r')
text_xml = file_xml.read()
print(text_xml)

re_tags = r'\<(/?\w+)'
tags = re.findall(re_tags, text_xml)
print(tags)

stack = [tags.pop(0)]
flag = True
for tag in tags:
    if tag == '/' + stack[-1]:
        a = stack.pop()
    elif tag[0] == '/':
        flag = False
        break
    else:
        stack.append(tag)
    print(stack)

if len(stack) == 0 and flag == True:
    print('XML file is correct')
else:
    print('XML file is not correct')

file_xml.close()