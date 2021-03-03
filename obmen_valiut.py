print('Для виходу натисніть Y')

while True:
    val = input('Введіть суму в гривнях : ')
    if val.lower() == 'y':
        break
    elif val.isdigit():
        val = int(val)
        cache = val // 29
        cent = round((val / 29 - cache) * 100)
        if cache == 1 or cache % 10 == 1:
            print('Отримайте', cache, 'долар', cent, 'центів')
        elif cache == 2 or cache ==3  or cache == 4:
            print('Отримайте', cache, 'долари', cent, 'центів')
        elif 5 <= cache <= 20 and cache != 10:
            print('Отримайте', cache, 'доларів', cent, 'центів')
        elif cache % 22 == 0 or cache % 23 == 0  or cache % 24 == 0:
            print('Отримайте', cache, 'долари', cent, 'центів')
        elif cache % 32 == 0 or cache % 33 == 0  or cache % 34 == 0:
            print('Отримайте', cache, 'долари', cent, 'центів')
        else:
            print('Отримайте', cache, 'доларів', cent, 'центів')
    else:
       print('Помилка вводу! Введіть числове значення!')
       continue

print('Робота обмінного пункту завершена!)')

    #elif val.lower() != 'y' and type(val) == int and type(val) == str:
     #   print('Помилка вводу! Введіть числове значення!')