"""Знайти суму парних елементів масиву, що стоять на непарних індексах"""

n = int(input('Кількість елементів масиву : '))
a = list(range(0,n+1))
print('a : ', a)

s = 0
i = 1
f = True

while i < len(a):
    if f == True:
        if a[i] % 2 == 0:
            s = s + a[i]
    i = i + 1
    f = not f
print('sum = ', s)
