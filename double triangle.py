for i in range(6):
    for j in range(i):
        print('*',end='')
    for k in range(10-2*i,0,-1):
        print(' ',end='')
    for l in range(i):
        print('*',end='')
    print()