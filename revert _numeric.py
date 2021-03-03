'''розвертає число'''

n = int(input())
while n > 0:
    digit = n % 10
    print(digit, end = '')
    n //= 10
print()

"""вводимо число і виводимо найбільше і найменшу цифру даного числа"""
m = int(input())
minDigit = 10
maxDigit = -1
while m > 0:
    digit = m % 10
    minDigit = min(minDigit, digit)
    maxDigit = max(maxDigit,digit)
    m //= 10
print(minDigit, maxDigit)

    
    