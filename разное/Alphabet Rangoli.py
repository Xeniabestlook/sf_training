
alpha = 'abcdefghijklmnopqrstuvwxyz'

n = 5
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    #print(s)
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    #print(L)
print('\n'.join(L[:0:-1]+L))


def gen(n):
    for i in range(n * 2 - 1):
        yield n - abs(i - n + 1)

        
n = 3
for i in gen(n):
    print('-'.join(chr(ord('a') + n - j) for j in gen(i)).center(n * 4 - 3, '-'))