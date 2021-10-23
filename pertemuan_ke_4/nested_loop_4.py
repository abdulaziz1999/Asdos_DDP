a = 5
s = a-1

for i in range(0,a):
    for j in range(0,s):
        print(' ', end='')
    s-=1
    for j in range(0,i+1):
        print('* ', end='')
    print('')

a = 5
s = 0 # for spaces
for i in range(0, a):
    for j in range(0, s):
        print(' ',end='')
    s += 1
    for j in range(0, a):
        print('* ' , end='')
    a -= 1
    print('')