while True:
    array_slv=input('Введіть слово :')
    slv=list(map(str,array_slv))

    i=0
    while i < len(slv):
        if slv[i]=='a' or slv[i]=='e' or slv[i]=='u' or slv[i]=='o':
            del slv[i]
        else:
            i = i + 1
    print(slv)

    str_slv=''.join(slv) #переведення списка в строку
    print(str_slv)