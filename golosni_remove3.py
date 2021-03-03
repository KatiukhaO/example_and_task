while True:
    array_slv = input('Введіть слово :')
    slv = list(map(str,array_slv))

    b = []
    i = 0
    while i < len(slv):
        if slv[i] !='a' and slv[i] !='e' and slv[i] !='u' and slv[i] !='o' and slv[i] !='i':
            b.append(slv[i])
        i = i + 1

              
    print('b =', b)
    str_slv = ''.join(b) #переведення списка в строку
    print(str_slv)