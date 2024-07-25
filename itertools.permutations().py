
from itertools import permutations

I, k = input().split(' ')

P = list(permutations(I, int(k)))
for p in sorted(P):
    print(*p, sep='')
