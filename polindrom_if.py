while True:
    a=input('Введіть слово поліндром? :')
    s=list(map(str,a))
    d=s[::-1]
    if s==d:
        print(s, " - Вітаємо!!! Це слово поліндром!")
    else:
        print(s, " - Нажаль, це НЕ слово поліндром!")
