# скачать git
# print(a,b,c sep='t') - между a b c будет t
# print(a,b,c end='t') - после a b c будет t
# a.find('o') - скажет индекс элемента
# a = list(map(int, input().split()))
#           A = ['a','2','3']
#           print('!!!'.join(A))
# f = open('yyyy', 'r')  # r - чтение, а - дописать в конец, w - переписать



#--------------------------------УРОК 1----------------------------------------------------------------------------------

#     №4
'''f = open('input.txt').readlines()
a = f[0].split()
k=int(a[0])
for i in a[1:]:
    if f[1]=='+':
        k+=int(i)
    elif f[1] == '*':
        k*=int(i)
    elif f[1] == '-':
        k-=int(i)'''

#     №5
'''N = int(input())
b = int(input('только <= 10'))
c = int(input('только <= 10'))
N10 = int(str(N), b)
Nc = ''
while N10 > 0:
    Nc += str(N10%c)
    N10 //= c
print(Nc)'''


#            №6
'''f = open('input.txt', 'r+').readlines()
masiv_chisla = f[0].split()

base = f[-1]
masiv_nov = []

for i in masiv_chisla:
    chislo10 = int(i, int(base))
    masiv_nov.append(chislo10)

pervoe = masiv_nov[0]

for i in masiv_nov[1:]:
    r = int(str(i), int(base))
    if f[1].strip() == '+':
        pervoe += r
    elif f[1].strip() == '*':
        pervoe *= r
    elif f[1].strip() == '-':
        pervoe -= r
res_base = ''

while pervoe > 0:
    res_base += str(pervoe%int(base))
    pervoe //= int(base)
res_base = res_base[::-1]

with open('output.txt', 'w') as f:
    f.write(res_base)'''


#--------------------------------УРОК 2----------------------------------------------------------------------------------

# Упражнение 1
'''vvod = '5 1 3 4' #input("Введите: ")
chislo = vvod[0]
cards = list(map(int, vvod[2:].split()))
for i in range(1, int(vvod[0]) + 1):
    if i in cards:
        continue
    else:
        print(i)'''

# Упражнение 2
'''a = 'ABCDEFGHI' #3 по 3
m = 3 #количесвто разбиений
n = len(a)//m
l1 = [[],[],[]]
for i in range(m):
    for k in range(n):
        index = i * n + k
        l1[i].append(a[index])
print(l1)'''

'''def group_rev(g, s):
    n = len(s) // g
    return ''.join(s[i:i+n][::-1] for i in range(0, len(s), n))
print(group_rev(3, 'ABCEHSHSH'))'''

# Упражнение 3

'''a = input()
a1 = a.replace('3', 'E').replace('L', 'J').replace('2', 'S').replace('5', 'Z')
mir = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']
p = ['E', 'J', 'S', 'Z']
fp = True
fm = True
for i in range(len(a)//2):
    if a[i] == a[len(a)-i-1]:
        if a[i] not in p and a[i] not in mir:
            fm = False
    else:
        fp = False
        if a1[i] not in p:
            fm = False
if a[len(a)//2] not in mir:
    fm = False
if fp:
    if fm:
        print(f'{a} is a mirrored palindrome.')
    else:
        print(f'{a} is a regular palindrome.')
else:
    if fm:
        print(f'{a} is a mirrored string.')
    else:
        print(f'{a} is not a palindrome.')'''

# Упражнение 4
'''a = [1, 2, 3, 4, 5]
for i in range(0, len(a)-1, 2): a[i], a[i+1] = a[i+1], a[i]
print(*a)'''

# Упражнение 5
'''a = list(map(int, input().split()))
a[1:], a[0] = a[:-1], a[-1]
print(*a)'''

# Упражнение 6
'''a = list(map(int, input().split()))
for x in a:
    if a.count(x) == 1:
        print(x)'''

# Упражнение 7
'''a = list(map(int, input().split()))
max = -10000
c = a[0]
for x in a:
    if a.count(x) > max:
        c = x
        max = a.count(x)
print(c)'''

# Упражнение 8
'''a = int(input())
n = list(map(int, input().split()))
for x in n:
    less = sum(1 for y in n if y < x)
    if less == a//2:
        print(x)
        break'''

# Упражнение 9
'''a = open('input.txt', 'r').read()
k = 0
i = 0
while i < len(a):
    if a[i] in ('!?.'):
        k += 1
        while i < len(a) and a[i] in ('!?.'):
            i+=1
        continue
    i += 1
print(k)'''

#--------------------------------УРОК 3----------------------------------------------------------------------------------

# Упражнение 1
'''def fibonacci(N, cache = {0:0, 1:1}):
    if N in cache:
        return cache[N]
    else:
        cache[N] = fibonacci(N-1, cache) + fibonacci(N-2, cache)
        return cache[N]
print(fibonacci(100))'''

'''def fibonacci(N):
    if N <= 1:
        return N
    a = 1
    b = 0
    for i in range(N-1):
        a,b = a+b, a
    return a'''

'''def fib(N):
    res = [0]*N
    res[1] = 1
    for i in range(2, N):
        res[i] = res[i-2] + res[i-1]
    return res[N-1]
print(fib(7))'''


# Упражнение 2
a = 10
def pr_mn(n, i = 2):
    while(i*i <= n):
        if n%i:
            i += 1
        else:
            return [i] + pr_mn(n//i,i)
    return [n]

# Упражнение 4
'''def tr(size, symb):
    if size % 2 == 1:
        for i in range(size//2+1):
            print((i+1)*symb)
        for i in range(size):
            print((size//2 - i)*symb)
    else:
        for i in range(size//2):
            print((i+1)*symb)
        for i in range(size):
            print((size//2 - i)*symb)
tr(4,'W')'''



















