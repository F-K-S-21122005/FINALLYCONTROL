

f = open('mat_dv.txt', 'r')

lst = [i for i in f]
eight = []
nine = []
ten = []
elevn= []


def winner_in_class(lst):
    summ = []
    for i in lst:
        summ.append(int(i[2]) + int(i[3]))
    for i in lst:
        if max(summ) == int(i[2]) + int(i[3]):
            print(f'{i[2]}: {i[0]} {i[1]}')

for i in lst:
    c = i.split()
    alg = []
    geo= []
    
    alg.append(int(c[3]))
    geo.append(int(c[4]))
    
    if int(c[2]) == 8:
        eight.append(c)
    elif int(c[2]) == 9:
        nine.append(c)
    elif int(c[2]) == 10:
        ten.append(c)
    elif int(c[2]) == 11:
        elevn.append(c)



for i in lst:
    pers = i.split()
    if max(alg) == int(pers[3]):
        print(' '.join(pers[:3]))
    if max(geo) == int(pers[4]):
        print(' '.join(pers[:3]))
    


print(winner_in_class(eight))
print(winner_in_class(nine))
print(winner_in_class(ten))
print(winner_in_class(elevn))

f.close()