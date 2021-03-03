'''Розвертає слово '''

N=str(input('Ввведіть слово N : '))
P=list(map(str,N))
l=len (P)
i=0
print(P)
while i<l:
    print(P[l-1-i], end=" ")
    i=i+1
    

