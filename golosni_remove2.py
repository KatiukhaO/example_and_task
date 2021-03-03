while True:
    array_slv = input('Введіть слово :')
    slv = list(map(str,array_slv))

    i = 0
    while i < len(slv):
        if slv[i]=='a' or slv[i]=='e' or slv[i]=='u' or slv[i]=='o':
            j = i
            while j < len(slv)-1:
                slv[j] = slv[j + 1]    
                j = j + 1
            slv[len(slv) - 1 ] = ' '
        else:
            i = i + 1
            
    print(slv)

    str_slv=''.join(slv) #переведення списка в строку
    print(str_slv)