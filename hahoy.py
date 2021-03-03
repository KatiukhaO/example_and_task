''' Ханойські Башні рекурсивний алгоритм'''

def move(n, start=1, finish=3):
    if n == 0:
        pass
    else:
        tmp = 6 - start - finish
        move(n-1, start, tmp)
        print(n, start, finish)
        move(n-1, tmp, finish)

n = int(input())
move(n)

