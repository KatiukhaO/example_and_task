while True:
    a=input('Введіть слово? :')
    if a=='exit': 
        break
    s=list(map(str,a))
    l=len(s)
    i=0
    bool=False
    while i<l/2:
        if s[i]==s[l-1-i]:
            bool=True
        else:
            bool=False
            break
        i=i+1
    if bool==True:
        print('Вітаю! Ви знайшли слово поліндром')
    else:
        print('Нажаль, це слово НЕ поліндром')
